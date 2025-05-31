# 🎯 Number Guessing Game

[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://www.python.org/)
[![DevVault](https://img.shields.io/badge/DevVault-Game%20Development-purple.svg)](https://github.com/qusai-Kagal/DevVault)
[![100 Days of Code](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2011-orange.svg)](https://github.com/qusai-Kagal/DevVault)

> **Part of [DevVault](https://github.com/qusai-Kagal/DevVault) 🚀 - Game Development Collection**

A classic console-based number guessing game where players attempt to guess a randomly generated number between 1-100. Features multiple difficulty levels and interactive feedback system.

## 🎮 Game Overview

This is a simple yet engaging guessing game that demonstrates fundamental game development concepts:
- 🎲 Random number generation
- 🎚️ Difficulty scaling
- 💬 Player feedback systems
- 🔄 Game loop mechanics

### 🎯 Gameplay Features

| Feature | Description |
|---------|-------------|
| 🟢 **Easy Mode** | 10 attempts to guess the number |
| 🔴 **Hard Mode** | 5 attempts to guess the number |
| 🎯 **Smart Hints** | "Too high" or "Too low" feedback |
| 🎨 **ASCII Art** | Beautiful game logo display |
| 📊 **Turn Tracking** | Visual countdown of remaining attempts |

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.6+ required
python --version

# Install art library for ASCII graphics
pip install art
```

### Running the Game
```bash
# Navigate to the game directory
cd game-development/number-guessing

# Run the game
python main.py
```

## 🎮 How to Play

1. **🎬 Game Start**: The game displays a welcome message and ASCII logo
2. **⚙️ Choose Difficulty**: Select 'easy' (10 attempts) or 'hard' (5 attempts)
3. **🎯 Make Guesses**: Enter numbers between 1-100
4. **📢 Get Feedback**: Receive "too high", "too low", or success messages
5. **🏆 Win Condition**: Guess correctly before running out of attempts!

### 📝 Sample Gameplay
```
🎯 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy

You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.

You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.
...
```

## 🏗️ Code Architecture

### 📁 File Structure
```
number-guessing/
├── main.py          # Main game logic
├── README.md        # This documentation
└── requirements.txt # Dependencies (optional)
```

### 🔧 Core Functions

| Function | Purpose |
|----------|---------|
| `game()` | Main game loop and initialization |
| `set_difficulty()` | Handles difficulty selection logic |
| `check_answer()` | Compares guesses and provides feedback |

### 🎨 Key Concepts Demonstrated

- **🎲 Random Generation**: Using `randint()` for unpredictable gameplay
- **🔄 Game Loops**: While loops for continuous gameplay
- **📊 State Management**: Tracking turns and game progress
- **🎯 Input Validation**: Handling user input safely
- **🎮 Game Flow**: Structured game states and transitions

## 🎓 Learning Outcomes

This project demonstrates mastery of:

- ✅ **Function Design**: Creating reusable, single-purpose functions
- ✅ **Control Flow**: Implementing conditional logic and loops
- ✅ **User Interaction**: Managing input/output effectively
- ✅ **Game Logic**: Building engaging player experiences
- ✅ **Code Organization**: Structuring code for readability

## 🚧 Future Enhancements

### 🎯 Version 2.0 Ideas
- [ ] 🏆 **High Score System**: Track best performances
- [ ] 🔢 **Custom Ranges**: Let players choose number boundaries
- [ ] 📈 **Statistics**: Game analytics and performance metrics
- [ ] 🎵 **Sound Effects**: Audio feedback for actions
- [ ] 🌐 **GUI Version**: Transition to tkinter or pygame
- [ ] 👥 **Multiplayer Mode**: Two-player competitive guessing

### 🎮 Game Development Evolution
- [ ] **Text Adventures**: Story-based decision games
- [ ] **Puzzle Games**: Logic and strategy challenges  
- [ ] **Action Games**: Real-time interactive experiences

## 🔗 Related DevVault Projects

Explore more from the **Game Development** collection:
- 🎮 [Other Games](../README.md) - More gaming projects
- 🧠 [AI/ML Games](../../ai-ml/README.md) - Intelligent game mechanics
- 🎨 [Web Games](../../web-development/README.md) - Browser-based games

## 📚 Part of 100 Days of Code Journey

**Day 11 Focus**: Functions with inputs, outputs, and game development fundamentals

This project is part of Angela Yu's 100 Days of Code Python Bootcamp, emphasizing:
- 🎯 Clean function design
- 🎮 Interactive program development  
- 📊 Logic flow management

## 🤝 Contributing to DevVault

Found a bug or have an enhancement idea? 
1. 🍴 Fork the [DevVault repository](https://github.com/qusai-Kagal/DevVault)
2. 🌿 Create a feature branch
3. 💻 Make your improvements
4. 📤 Submit a pull request

## 📄 License

This project is part of DevVault and is licensed under the MIT License.

---

## 🔗 Connect & Explore

**🏠 Main Repository**: [DevVault](https://github.com/qusai-Kagal/DevVault)  
**👨‍💻 Developer**: [@qusai-Kagal](https://github.com/qusai-Kagal)  
**📂 Game Development**: [Browse All Games](../README.md)

---

<div align="center">

**⭐ Star DevVault if this helped you learn! ⭐**

*Building the future, one game at a time* 🎮

</div>
