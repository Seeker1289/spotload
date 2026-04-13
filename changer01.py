import requests
from ytmusicapi import YTMusic

yt = YTMusic()

with open("notFound.txt", "r") as file:
    links = file.readlines()

with open("nfslinks.txt", "w", encoding="utf-8") as out1:
    with open("nfvlinks.txt", "w", encoding="utf-8") as out2:
        for url in links:
            url = url.strip()
            html = requests.get(url).text

            start = html.find('property="og:title" content="')
            if start != -1:
                start += len('property="og:title" content="')
                end = html.find('"', start)
                song_name = html[start:end]

            start = html.find('property="og:description" content="')
            if start != -1:
                start += len('property="og:description" content="')
                end = html.find('"', start)
                desc = html[start:end]
                if "·" in desc:
                    artist = desc.split("·")[0].strip()

                song = f"{song_name} - {artist}\n"
                print("Saved:", song_name, artist)

                search = yt.search(song.strip(), filter = "songs")
                if search:
                    out1.write(f"https://music.youtube.com/watch?v={search[0]['videoId']}\n")
                    print("searched")
                else:
                    print("Not present in songs")

                search = yt.search(song.strip(), filter = "videos")
                if search:
                    out2.write(f"https://music.youtube.com/watch?v={search[0]['videoId']}\n")
                    print("searched")
                else:
                    print("Not present in vids")

            else:
                print("Failed:", url)
