#!/bin/bash
for word in $(cat ytlinks.txt); do
	if [[ $word == "song" ]]; then
		path="$1/songs"
	elif [[ $word == "video" ]]; then
		path="$1/videos"
	else
		python3 yt-dlp -x $word -P $path
	fi
done

for word in $(cat nfslinks.txt); do
	python3 yt-dlp -x $word -P $1/songs/nf
done

for word in $(cat nfvlinks.txt); do
	python3 yt-dlp -x $word -P $1/videos/nf
done
