from pytubefix import Playlist

def playlist_lister(playlist_url):

    playlist = Playlist(playlist_url)

    playlist_all_urls = []

    for url in playlist.video_urls:
        playlist_all_urls.append(url)

    return playlist_all_urls