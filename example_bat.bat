@echo off
setlocal enabledelayedexpansion

set base=%1
set path=

for %%w in (%CD%\ytlinks.txt) do (
    set word=%%w

    if "!word!"=="song" (
        set path=%base%\songs
    ) else if "!word!"=="video" (
        set path=%base%\videos
    ) else (
        python -m yt_dlp -x "!word!" -P "!path!"
    )
)

for %%w in (%CD%\nfslinks.txt) do (
    python -m yt_dlp -x "%%w" -P "%base%\songs\nf"
)

for %%w in (%CD%\nfvlinks.txt) do (
    python -m yt_dlp -x "%%w" -P "%base%\videos\nf"
)

endlocal
