# ⏰ TimeMinder

> A simple yet powerful command-line countdown timer with audio alerts! ⏱️

## 📋 Overview

TimeMinder is a lightweight Python script that helps you stay on track with your tasks by providing a visual countdown and audio notification when time is up. Perfect for timing your work sessions, cooking, workouts, or any time-sensitive activity!

## ✨ Features

- 🔢 Simple command-line interface
- ⏱️ Countdown display in minutes and seconds
- 🔄 Real-time updating timer
- 🔊 Audio alert when countdown completes
- 🧹 Clean terminal display

## 🛠️ Requirements

- Python 3.6+
- `playsound` library
- An audio file named "alarm.mp3" in the same directory

## 📥 Installation

1. Ensure you have Python installed on your system
2. Install the required dependency:
   ```
   pip install playsound
   ```
3. Place an "alarm.mp3" file in the same directory as the script
4. You're ready to go! ✅

## 🚀 Usage

Run the script with:

```bash
python alarm.py
```

Then follow the prompts:
1. Enter the number of minutes ⌛
2. Enter the number of seconds ⏱️
3. Watch the countdown and wait for the alarm! 🔔

## 📝 Example

```
$ python alarm.py
Enter the number of minutes: 5
Enter the number of seconds: 30
```

The timer will count down from 5:30 and play your alarm sound when complete!

## 🔍 How It Works

TimeMinder uses ANSI escape codes to clear the terminal and provide a clean updating display. The countdown is updated every second, and the playsound library handles the audio alert when the timer reaches zero.

## 🤝 Contributing

Feel free to fork this repository and make your own improvements! Some ideas:
- Add multiple alarm sounds
- Create a config file for default settings
- Add a pause/resume feature
- Implement a GUI interface

## 📜 License

This project is part of the DevVault repository and is licensed under the [MIT License](../../LICENSE).

---

⭐ **Created with ❤️ as part of [DevVault](https://github.com/qusai-Kagal/DevVault)** ⭐
