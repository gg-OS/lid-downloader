from urllib.parse import parse_qs, urlparse

from pytubefix import Playlist, extract
from pytubefix.innertube import InnerTube


MAX_CONTINUATION_PAGES = 50


def normalize_playlist_url(playlist_url):
    raw_url = playlist_url.strip()
    parsed = urlparse(raw_url)

    if parsed.scheme and parsed.netloc:
        playlist_id = parse_qs(parsed.query).get("list", [None])[0]
    else:
        playlist_id = raw_url

    if not playlist_id:
        raise ValueError("Playlist URL must include a 'list=' parameter")

    return f"https://www.youtube.com/playlist?list={playlist_id}"


def _append_unique(target, urls):
    seen = set(target)
    for url in urls:
        if url not in seen:
            target.append(url)
            seen.add(url)


def _extract_visitor_data(data):
    try:
        return data["responseContext"]["webResponseContextExtensionData"]["ytConfigData"]["visitorData"]
    except (KeyError, TypeError):
        return None


def _extract_continuation_tokens(data):
    tokens = []

    def add_token(token):
        if token and token not in tokens:
            tokens.append(token)

    def walk(node):
        if isinstance(node, dict):
            continuation_command = node.get("continuationCommand")
            if isinstance(continuation_command, dict):
                add_token(continuation_command.get("token"))

                innertube_command = continuation_command.get("innertubeCommand")
                if isinstance(innertube_command, dict):
                    add_token(innertube_command.get("token"))

            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return tokens


def _extract_watch_endpoint_urls(data, playlist_id):
    urls_by_index = {}
    seen_without_index = []

    def walk(node):
        if isinstance(node, dict):
            endpoint = node.get("watchEndpoint")
            if isinstance(endpoint, dict):
                video_id = endpoint.get("videoId")
                endpoint_playlist_id = endpoint.get("playlistId")

                if video_id and (not endpoint_playlist_id or endpoint_playlist_id == playlist_id):
                    url = f"https://www.youtube.com/watch?v={video_id}&list={playlist_id}"
                    index = endpoint.get("index")
                    if isinstance(index, int):
                        urls_by_index[index] = url
                    elif url not in seen_without_index:
                        seen_without_index.append(url)

            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)

    ordered_urls = [url for _, url in sorted(urls_by_index.items())]
    for url in seen_without_index:
        if url not in ordered_urls:
            ordered_urls.append(url)

    return ordered_urls


def _extract_paginated_urls(initial_data, playlist_id):
    playlist_urls = _extract_watch_endpoint_urls(initial_data, playlist_id)
    visitor_data = _extract_visitor_data(initial_data)
    pending_tokens = _extract_continuation_tokens(initial_data)
    processed_tokens = set()
    innertube = InnerTube("WEB")
    pages_loaded = 0

    while pending_tokens and pages_loaded < MAX_CONTINUATION_PAGES:
        token = pending_tokens.pop(0)
        if token in processed_tokens:
            continue

        processed_tokens.add(token)
        response = innertube.browse(continuation=token, visitor_data=visitor_data)
        pages_loaded += 1

        _append_unique(playlist_urls, _extract_watch_endpoint_urls(response, playlist_id))

        if not visitor_data:
            visitor_data = _extract_visitor_data(response)

        for next_token in _extract_continuation_tokens(response):
            if next_token not in processed_tokens and next_token not in pending_tokens:
                pending_tokens.append(next_token)

    return playlist_urls


def playlist_lister(playlist_url):
    normalized_url = normalize_playlist_url(playlist_url)
    playlist_id = parse_qs(urlparse(normalized_url).query)["list"][0]
    playlist = Playlist(normalized_url)

    playlist_all_urls = list(playlist.video_urls)

    if not playlist_all_urls:
        playlist_all_urls = [
            video.watch_url
            for video in playlist.videos
            if getattr(video, "watch_url", None)
        ]

    if not playlist_all_urls:
        playlist_all_urls = _extract_paginated_urls(extract.initial_data(playlist.html), playlist_id)

    if not playlist_all_urls:
        raise ValueError("No videos were found. The playlist may be empty, unavailable, or YouTube changed its page structure.")

    return playlist_all_urls
