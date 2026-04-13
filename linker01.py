import requests

playlist_url = input("Enter Spotify playlist URL: ")

html = requests.get(playlist_url).text

links = set()
for part in html.split('"'):
    if "open.spotify.com/track/" in part:
        links.add(part)

with open("links.txt", "a") as f:
    for link in links:
        f.write(link + "\n")

print(f"Extracted {len(links)} links")
