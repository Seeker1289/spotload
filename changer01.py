import requests
from ytmusicapi import YTMusic

yt = YTMusic()

def entity(x):
    x = x.replace("&quot;", '"')
    x = x.replace("&#x27;", "'")
    return x

with open("links.txt", "r") as file:
    links = file.readlines()

notFound = []

with open("ytlinks.txt", "w", encoding="utf-8") as out:
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
                
                n = song_name.find("(From")
                if n != -1:
                    n = song_name.find("[From")
                    if n != -1:
                        song_name = song_name[0:n-1]
                        
            song_name = entity(song_name)
            song = f"{song_name} - {artist}"
            #print(f"Saved: {song_name}, {artist}")
            search = yt.search(song.strip(), filter = "songs")
            
            if search:
                ytsong = search[0]['title']
                if song_name.lower() in ytsong.lower():
                    print(f"{song} in songs")
                    out.write(f"song https://music.youtube.com/watch?v={search[0]['videoId']}\n")
                else:
                    search = yt.search(song.strip(), filter = "videos")
                    if search:
                        ytsong = search[0]['title']
                    if song_name.lower() in ytsong.lower():
                        print(f"{song} in videos")
                        out.write(f"video https://music.youtube.com/watch?v={search[0]['videoId']}\n")
                    else:
                        print(f"{song} not found")
                        notFound.append(url)
            
        else:
            print("failed")

with open("notFound.txt", "w", encoding="utf-8") as out:
    for i in notFound:
        out.write(f"{i}\n")
