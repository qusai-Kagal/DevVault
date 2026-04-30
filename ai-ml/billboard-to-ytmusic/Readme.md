# 🎵 Billboard to YouTube Music

> *Enter a date. Get a playlist. Time-travel through music.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Web%20Scraping-59666C?style=flat)
![YouTube Music](https://img.shields.io/badge/YouTube%20Music-API-FF0000?style=flat&logo=youtube&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## 📖 Table of Contents

- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [About the Developer](#-about-the-developer)

---

## 💡 Why This Project?

Ever wondered what the world was listening to on your birthday? Or on a historic day in music history?

**Billboard to YouTube Music** solves exactly that. It bridges two platforms — Billboard's historical chart archive and YouTube Music's streaming library — to let you relive any era through its top songs. No manual searching, no playlist building. Just enter a date and hit play.

This project demonstrates real-world skills in web scraping, API integration, and automation — built to solve a genuine, relatable problem.

---

## ✨ Features

- 📅 **Date-based playlist generation** — input any date (YYYY-MM-DD) to pull that day's Billboard Hot 100
- 🔍 **Smart search matching** — queries YouTube Music by song title + artist for accurate results
- 📋 **Auto playlist creation** — creates a private YouTube Music playlist named after the date
- ⚠️ **Graceful error handling** — skips unavailable tracks without crashing; logs every action
- 🔐 **Authenticated access** — uses your own YouTube Music session via `ytmusicapi` browser auth
- 🧠 **Minimal dependencies** — no heavy frameworks, clean and readable Python

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Web Scraping | `requests`, `BeautifulSoup4` |
| Music API | `ytmusicapi` (YouTube Music) |
| HTML Parsing | `html.parser` |
| Auth | Browser-based session (`browser.json`) |

---

## 📁 Project Structure

```
billboard-to-ytmusic/
│
├── main.py          # Core script — scraping + playlist creation
├── browser.json     # YouTube Music auth session (user-generated, gitignored)
├── requirements.txt # Python dependencies
└── README.md
```

---

## ✅ Prerequisites

- Python 3.8 or higher
- A YouTube Music account
- `ytmusicapi` installed and authenticated

---

## 🚀 Installation

**1. Clone the repository**
```bash
git clone https://github.com/qusai-Kagalwala/billboard-to-ytmusic.git
cd billboard-to-ytmusic
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Authenticate with YouTube Music**

Run the following command and follow the browser-based setup:
```bash
ytmusicapi browser
```
This generates a `browser.json` file in your project directory — keep it private and never commit it.

---

## 🎮 Usage

```bash
python main.py
```

When prompted, enter a date in `YYYY-MM-DD` format:

```
Enter date (YYYY-MM-DD): 2005-08-12
```

The script will:
1. Scrape Billboard Hot 100 for that date
2. Search YouTube Music for each song
3. Create a private playlist named `2005-08-12 Billboard 100`
4. Add all found tracks automatically

**Sample output:**
```
Created playlist: 2005-08-12 Billboard 100
Added: We Belong Together - Mariah Carey
Added: Cha Cha Slide - DJ Casper
Not found: Some Rare Track
Skipped: Another Track | <error details>
```

---

## ⚙️ How It Works

```
User Input (Date)
       │
       ▼
Scrape Billboard Hot 100  ──►  BeautifulSoup parses song titles + artists
       │
       ▼
YouTube Music Auth  ──►  ytmusicapi loads browser.json session
       │
       ▼
Create Playlist  ──►  Named after date, set to PRIVATE
       │
       ▼
Search + Add Songs  ──►  For each track, search YTM, grab videoId, insert
```

> **Note:** Billboard's HTML structure may change over time. If scraping breaks, inspect the live page and update the CSS selectors in `main.py` (Step 4).

---

## 🔭 Future Improvements

- [ ] **GUI / Web Interface** — browser-based input instead of CLI
- [ ] **Spotify support** — generate Spotify playlists via Spotipy
- [ ] **Retry logic** — smarter fallback search when the first result misses
- [ ] **Top N songs** — option to pick fewer than 100 songs
- [ ] **Export to CSV** — save the chart as a local file
- [ ] **Error report** — summary of skipped/not-found tracks at the end
- [ ] **Selector auto-detection** — handle Billboard HTML changes gracefully

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add: your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please keep code clean, commented, and consistent with the existing style.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 About the Developer

**Qusai Kagalwala** — Full-Stack Developer & AI Enthusiast

I'm a CS student at KC College Mumbai with 60+ projects spanning web development, backend systems, AI integrations, and developer tooling. I build things that solve real problems — from Billboard playlist generators to enterprise automation tools.

**Achievements:**
- 🥇 1st Place — Prompt Craft Competition, Cyberstrike'25
- 🥈 2nd Place — Pitch an App/Website, Fiestron '24–25
- 🎯 Event Head — Hackathon at Fiestron

**Connect:**

[![GitHub](https://img.shields.io/badge/GitHub-qusai--Kagalwala-181717?style=flat&logo=github)](https://github.com/qusai-Kagalwala)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Qusai%20Kagalwala-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/qusai-kagalwala/)
[![Portfolio](https://img.shields.io/badge/Portfolio-DevVault-6e40c9?style=flat&logo=github)](https://github.com/qusai-Kagal/DevVault)

---

<p align="center">Built with 🎵 and Python by <a href="https://github.com/qusai-Kagalwala">Qusai Kagalwala</a></p>
