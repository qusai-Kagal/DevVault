import os
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

# -------------------------------
# Step 1: Check authentication file
# -------------------------------
# 'browser.json' contains your authenticated session
# for ytmusicapi (YouTube Music access)
if not os.path.exists("browser.json"):
    print("browser.json not found. Run: ytmusicapi browser")
    exit()

# -------------------------------
# Step 2: Take user input (date)
# -------------------------------
# Format: YYYY-MM-DD (e.g., 2005-08-12)
date = input("Enter date (YYYY-MM-DD): ")

# -------------------------------
# Step 3: Fetch Billboard Hot 100 page
# -------------------------------
# Using headers to mimic a real browser request
url = f"https://www.billboard.com/charts/hot-100/{date}"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------------
# Step 4: Extract song names and artists
# -------------------------------
# NOTE: These selectors depend on Billboard's HTML structure
# and may break if the site updates its layout

# Extract song titles
song_names = [
    tag.getText(strip=True)
    for tag in soup.select("li ul li h3")
]

# Extract artist names
artists = [
    tag.getText(strip=True)
    for tag in soup.select("li ul li span")
]

# -------------------------------
# Step 5: Authenticate YouTube Music
# -------------------------------
# Using ytmusicapi with saved browser headers
yt = YTMusic("browser.json")

# -------------------------------
# Step 6: Create a new playlist
# -------------------------------
playlist_name = f"{date} Billboard 100"

playlist_id = yt.create_playlist(
    playlist_name,
    f"Top songs from {date}",
    privacy_status="PRIVATE"  # Playlist visibility
)

print(f"Created playlist: {playlist_name}")

# -------------------------------
# Step 7: Search and add songs
# -------------------------------
# Loop through each song + artist pair
for song, artist in zip(song_names, artists):

    # Combine song and artist for better search accuracy
    query = f"{song} {artist}"

    try:
        # Search YouTube Music for the song
        results = yt.search(query, filter="songs", limit=1)

        # If results found, add first match to playlist
        if results:
            video_id = results[0]["videoId"]
            yt.add_playlist_items(playlist_id, [video_id])
            print(f"Added: {song} - {artist}")
        else:
            # No matching result found
            print(f"Not found: {song}")

    except Exception as e:
        # Catch unexpected errors (API issues, parsing errors, etc.)
        print(f"Skipped: {song} | {e}")
