# 🎯 CodeBreaker

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Game](https://img.shields.io/badge/Game-Logic%20Puzzle-orange.svg)]()

> 🧩 **Test your deduction skills in this classic code-breaking puzzle!**

CodeBreaker is a Python implementation of the classic Mastermind game where you must crack a secret color code using logic, deduction, and a bit of luck. Can you break the code before you run out of attempts?

## 🎮 Game Overview

In CodeBreaker, the computer generates a secret 4-color code using 6 different colors. Your mission: guess the exact sequence and position of colors within 10 attempts. Each guess provides feedback to help you narrow down the possibilities!

### 🎯 Objective
Crack the secret 4-color code in 10 attempts or fewer using logical deduction and the feedback from each guess.

## ✨ Features

### 🎲 Core Gameplay
- 🔴 **6 Colors Available**: Red, Green, Blue, Yellow, White, Orange
- 🎯 **4-Position Code**: Secret sequence of 4 colors
- ⏱️ **10 Attempts**: Limited tries to crack the code
- 🔍 **Smart Feedback**: Detailed hints after each guess

### 🧠 Feedback System
After each guess, you receive three types of feedback:
- ✅ **Correct Positions**: Right color in the right spot
- 🔄 **Correct Colors, Wrong Position**: Right color, wrong location  
- ❌ **Incorrect Colors**: Colors not in the secret code

### 🎪 Game Features
- 🎨 **Color-coded Interface**: Easy-to-read terminal output
- ✅ **Input Validation**: Prevents invalid guesses
- 📊 **Attempt Tracking**: Shows progress through the game
- 🏆 **Win/Lose Conditions**: Clear game endings

## 🚀 Quick Start

### Prerequisites
- 🐍 Python 3.6 or higher (uses only built-in libraries!)

### Installation & Running

1. **Clone the repository**
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/game-development/CodeBreaker
   ```

2. **Run the game**
   ```bash
   python mastermind.py
   ```

3. **Start playing!** 🎉

## 🎮 How to Play

### 🎯 Game Setup
- The computer generates a secret 4-color code
- Colors can repeat (e.g., `R R G B` is valid)
- You have 10 attempts to guess correctly

### 🎨 Available Colors
| Color | Code |
|-------|------|
| 🔴 Red | `R` |
| 🟢 Green | `G` |
| 🔵 Blue | `B` |
| 🟡 Yellow | `Y` |
| ⚪ White | `W` |
| 🟠 Orange | `O` |

### 📝 Making Guesses
1. Enter 4 colors separated by spaces: `R G B Y`
2. Use only the color codes: `R`, `G`, `B`, `Y`, `W`, `O`
3. Colors can be repeated in your guess

### 🔍 Understanding Feedback
```
Example: Secret code is R G B Y, Your guess is R B G W

Correct Positions: 1        (R is correct and in position 1)
Correct Colors, Wrong Position: 2  (G and B are correct but in wrong positions)
Incorrect Colors: 1         (W is not in the secret code)
```

### 🏆 Winning
- Guess all 4 colors in the correct positions
- Game ends immediately when you win
- Shows your winning attempt number

## 📖 Example Gameplay

```
Welcome to Mastermind!
Try to guess the secret code made of 4 colors from ['R', 'G', 'B', 'Y', 'W', 'O'].
You have 10 tries to guess correctly.

Attempt 1:
Enter your guess (4 colors, space-separated like R G B Y): R G B Y
Correct Positions: 1 | Correct Colors in Wrong Positions: 2 | Incorrect Colors: 1

Attempt 2:
Enter your guess (4 colors, space-separated like R G B Y): R B G W
Correct Positions: 1 | Correct Colors in Wrong Positions: 2 | Incorrect Colors: 1

Attempt 3:
Enter your guess (4 colors, space-separated like R G B Y): R O G B
Correct Positions: 4 | Correct Colors in Wrong Positions: 0 | Incorrect Colors: 0

Congratulations! You guessed the code ROGB correctly in 3 attempts!
```

## 🧠 Strategy Tips

### 🎯 Beginner Strategies
1. **Start with variety** - Use 4 different colors in your first guess
2. **Use feedback wisely** - Track which colors are confirmed in/out
3. **Position matters** - Pay attention to correct vs. misplaced colors
4. **Eliminate systematically** - Rule out impossible combinations

### 🏆 Advanced Techniques
1. **Information theory** - Maximize information gained per guess
2. **Constraint satisfaction** - Use logical deduction between attempts
3. **Pattern recognition** - Look for common code patterns
4. **Frequency analysis** - Consider which colors appear most often

## 🛠️ Technical Details

### Code Structure
```python
🎲 generate_code()     # Creates random 4-color secret code
🎮 guess_code()        # Handles user input and validation
🔍 check_code()        # Compares guess to secret code
🎯 game()              # Main game loop and logic
```

### Key Algorithms
- **Random Code Generation**: Uses Python's `random.choice()`
- **Feedback Calculation**: Position-aware color matching algorithm
- **Input Validation**: Comprehensive error checking and user guidance

### Game Constants
- `COLORS`: Available color set (`['R', 'G', 'B', 'Y', 'W', 'O']`)
- `TRIES`: Maximum attempts allowed (`10`)
- `CODE_LENGTH`: Length of secret code (`4`)

## 🔧 Customization

Want to modify the game? Here are easy tweaks:

```python
# Make it harder/easier
TRIES = 15          # More attempts
CODE_LENGTH = 5     # Longer code

# Add more colors
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O', 'P', 'K']  # Purple, Black

# Debug mode (see the secret code)
# Uncomment line 50: print(f"DEBUG: Secret code is {''.join(code)}")
```

## 🚀 Future Enhancements

### 🎨 Potential Features
- 🖥️ **GUI Version**: Tkinter or Pygame interface
- 🏆 **Difficulty Levels**: Easy (3 colors), Normal (4), Hard (5+)
- 📊 **Statistics Tracking**: Win rate, average attempts
- 🎵 **Sound Effects**: Audio feedback for wins/losses
- 🌈 **Visual Colors**: Actual color display instead of letters
- 💾 **Save System**: Resume interrupted games
- 🤖 **AI Solver**: Computer attempts to solve codes
- 🌐 **Multiplayer**: Two-player code creation/solving

### 🔧 Code Improvements
- Object-oriented design
- Configuration file support
- Unit tests
- Performance optimizations

## 🤝 Contributing

Love CodeBreaker? Here's how you can help improve it:

1. 🍴 Fork the repository
2. 🌟 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

### 💡 Contribution Ideas
- 🎨 GUI implementation
- 🎵 Sound and music
- 🏆 Scoring systems
- 🤖 AI solvers
- 📱 Mobile version
- 🌐 Web version

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎮 Game History

Mastermind was invented in 1970 by Mordecai Meirowitz. This digital version brings the classic board game experience to your terminal, maintaining the original's challenging logical puzzle gameplay while adding modern programming conveniences.

## 🙏 Acknowledgments

- 🎯 Mordecai Meirowitz for creating the original Mastermind game
- 🐍 Python community for excellent built-in libraries
- 🧠 Logic puzzle enthusiasts worldwide
- 🎮 Classic board game preservation efforts

## 📬 Contact

**Qusai Kagal** - Game Developer & Puzzle Enthusiast

- 💼 GitHub: [@qusai-Kagal](https://github.com/qusai-Kagal)

---

⭐ **Star this repo if you enjoyed cracking codes with CodeBreaker!** ⭐

*Made with 🧠 and lots of logical thinking!*
