import requests

playlist_url = input("Enter Spotify playlist URL: ")

html = requests.get(playlist_url).text

# Collect all track links found in HTML
links = set()
for part in html.split('"'):
    if "open.spotify.com/track/" in part:
        links.add(part)

# Save links to file
with open("links.txt", "a") as f:
    for link in links:
        f.write(link + "\n")

print(f"Extracted {len(links)} links")
