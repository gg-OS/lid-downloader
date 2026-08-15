@echo off
echo Building LID Downloader for Windows...
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
)

REM Clean previous builds
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist

REM Build using spec file
echo.
echo Building executable...
pyinstaller lid_downloader.spec

REM Check if build succeeded
if exist "dist\LID_Downloader\LID_Downloader.exe" (
    echo.
    echo ========================================
    echo Build successful!
    echo Executable location: dist\LID_Downloader\LID_Downloader.exe
    echo.
    echo IMPORTANT: Make sure ffmpeg.exe is in the ffmpeg\ folder
    echo ========================================
) else (
    echo.
    echo Build failed. Check errors above.
)

pause
