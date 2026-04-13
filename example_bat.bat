@echo off
setlocal enabledelayedexpansion

set "path="

for /f "usebackq tokens=*" %%L in ("ytlinks.txt") do (
    for %%w in (%%L) do (
        if "%%w"=="song" (
            set "path=%~1\songs"
        ) else if "%%w"=="video" (
            set "path=%~1\videos"
        ) else (
            python yt-dlp -x %%w -P "!path!"
        )
    )
)

for /f "usebackq tokens=*" %%L in ("nfslinks.txt") do (
    for %%w in (%%L) do (
        python yt-dlp -x %%w -P "%~1\songs\nf"
    )
)

for /f "usebackq tokens=*" %%L in ("nfvlinks.txt") do (
    for %%w in (%%L) do (
        python yt-dlp -x %%w -P "%~1\videos\nf"
    )
)

endlocal
