# ⚡ Speed Keys: WPM Typing Test ⌨️

A fun, terminal-based typing speed test application built with Python and curses library. Challenge yourself to improve your typing speed and accuracy!

## 📋 Features

- 🚀 Real-time WPM (Words Per Minute) calculation
- ✅ Instant visual feedback with color-coded characters
- 📚 Library of pangrams and typing challenges
- 🎯 Accuracy tracking with highlighting of mistakes
- 🔄 Restart functionality for continuous practice
- ⏱️ Timer starts only after your first keystroke

## 🛠️ Requirements

- Python 3.x
- curses library (built-in with Python on Unix/Linux/macOS, requires windows-curses on Windows)

## 🚀 Installation

1. Clone the repository:
   ```
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/game-development/speed-keys
   ```

2. Make sure you have Python installed.

3. If you're on Windows, install the windows-curses package:
   ```
   pip install windows-curses
   ```

## 🎮 How to Play

1. Run the program:
   ```
   python wpm_typing_test.py
   ```

2. Press any key to begin the typing test.

3. Type the displayed text as quickly and accurately as possible.

4. The program shows your WPM in real-time as you type.

5. Green text indicates correct keystrokes, while red text indicates errors.

6. Once you complete the text, you can press any key to try again or ESC to quit.

## 📑 Text Source

The program randomly selects a text from `text.txt`, which contains a collection of pangrams (sentences using every letter of the alphabet) and other typing challenges.

## 🎛️ Controls

- **Typing keys**: Input characters
- **Backspace**: Delete the previous character
- **ESC**: Exit the current test
- **Any key**: Start a new test after completing one

## 🛠️ Customization

You can customize the typing challenges by editing the `text.txt` file. Add your own sentences, quotes, or paragraphs to practice with different types of content.

## 📈 Development

This project is part of the DevVault collection, showcasing practical programming projects. Feel free to fork and extend with additional features such as:

- User accounts and high score tracking
- Different difficulty levels
- Timed challenges
- Online leaderboards

## 📝 License

[MIT License](LICENSE)

---

Happy typing! 🚀⌨️
