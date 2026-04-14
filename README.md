
# Temporary Spotload

### Step 1:

Install selenium, requests, ytmusicapi modules for python.<br>
Also add an environment variable for python (for windows)

### Step 2:

Download linker01.py, linker02.py and changer01.py<br>
From https://github.com/yt-dlp/yt-dlp download yt-dlp (for linux) or yt-dlp.exe (for windows)

### Step 3:

For Linux, download the example_bash.sh<br>
For Windows, download the example_bat.bat

### Step 4:

Run linker01.py if the playlist has less than 31 songs.<br>

Run linker02.py otherwise, after the browser is opened, scroll down slowly till the end (to load all songs)<br>
Take a screenshot of the recommended songs or note them down (those extra songs also get loaded)

### Step 5:

Run changer01.py

### Step 6:

Run the example_bash.sh or example_bat.bat like<br>
**./example_bash.sh /home/username/Music**<br>
**example_bat.bat C:\Users\username\Music**

### Step 7:

Manually delete the extra songs loaded, songs in the video section if there are any interruptions in between, songs in the nf folder which don't match.
