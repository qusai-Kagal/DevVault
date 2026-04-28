# top-100-movies-scraper
# Scrapes Empire Online's "Best Movies" list from a Web Archive snapshot
# and saves the movies ranked #1 to #100 (ascending order) to a text file.

import requests
from bs4 import BeautifulSoup

# Archived URL of Empire Online's Top 100 Movies list (via Wayback Machine)
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch the webpage content
response = requests.get(URL)
website_html = response.text  # Raw HTML as a string

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Find all movie title elements — they're wrapped in <h3 class="title"> tags
all_movies = soup.find_all(name="h3", class_="title")

# Extract plain text from each tag (strips surrounding HTML)
movie_titles = [movie.getText() for movie in all_movies]

# The page lists movies from #100 down to #1, so reverse for ascending order
movies = movie_titles[::-1]

# Write the sorted movie list to a text file, one title per line
# encoding="utf-8" prevents UnicodeEncodeError on Windows (default is cp1252)
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
