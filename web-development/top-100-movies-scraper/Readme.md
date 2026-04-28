# 🎬 Top 100 Movies Scraper

A Python web scraper that pulls Empire Online's **Top 100 Movies of All Time** from a Wayback Machine snapshot and saves them in ascending order (1 → 100) to a `.txt` file.

## 📁 Project Structure

```
top-100-movies-scraper/
├── main.py       # Scraper script
├── movies.txt    # Output file (generated on run)
└── README.md
```

## ⚙️ How It Works

1. Sends an HTTP GET request to an archived Empire Online page via the Wayback Machine
2. Parses the HTML using **BeautifulSoup**
3. Extracts all `<h3 class="title">` elements (movie titles)
4. Reverses the list (page orders #100 → #1; we want #1 → #100)
5. Writes the result to `movies.txt`

## 🚀 Getting Started

### Prerequisites

```bash
pip install requests beautifulsoup4
```

### Run

```bash
python main.py
```

Output will be saved to `movies.txt` in the same directory.

## 🛠️ Tech Stack

- **Python 3**
- **requests** — HTTP requests
- **BeautifulSoup4** — HTML parsing

## 📄 Sample Output (`movies.txt`)

```
1. Citizen Kane
2. Casablanca
3. The Godfather
...
```

## 📌 Notes

- The scraper targets a static Wayback Machine snapshot to avoid issues with the live site changing over time.
- No API key or authentication required.
