
# Temporary Spotload

### Step 1:

Install selenium, requests, ytmusicapi modules for python.<br>
Also add an environment variable for python (for windows)

### Step 2:

Download linker01.py, linker02.py, changer01.py and yt-dlp from https://github.com/yt-dlp/yt-dlp

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

Run the example_bash.sh or example_bat.bat like<br>**./example_bash.sh \</full/path/to/directory/where/you/want/to/download>**

### Step 7:

Manually delete the extra songs loaded, songs in the video section if there are any interruptions in between, songs in the nf folder which don't match.
