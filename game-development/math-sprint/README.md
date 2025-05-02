# 🧮 Math Sprint

⏱️ A challenging command-line math quiz game to test and improve your calculation speed!

## 📖 Description

Math Sprint is part of the [DevVault](https://github.com/qusai-Kagal/DevVault) collection, specifically under the game-development category. This engaging command-line game challenges players to solve arithmetic problems as quickly as possible, helping to improve mental calculation skills while tracking performance metrics.

## ✨ Features

- 🧮 Random arithmetic problems (addition, subtraction, multiplication)
- ⏱️ Performance timing from start to finish
- 🔄 Immediate feedback on incorrect answers
- 📊 Performance tracking (total time, wrong attempts, final score)
- 🎯 Adjustable difficulty through operand value ranges

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Running the Game

1. Clone the DevVault repository:
   ```
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/game-development/math-sprint
   ```

2. Run the game:
   ```
   python timed_quiz_game.py
   ```

## 🎮 How to Play

1. Press Enter to start the quiz
2. Solve each arithmetic problem as quickly as possible
3. Enter your answer and press Enter
4. If your answer is incorrect, you'll be prompted to try again
5. After completing all 10 problems, view your total time, number of wrong attempts, and final score

## 📝 Example

```
Press Enter to start the quiz...
-- Start of the quiz --
Problem #1: 8 + 5 = 13
Problem #2: 7 * 10 = 70
Problem #3: 12 - 4 = 8
...
-- End of the quiz --
Nice work! You finished the quiz in 42.68 seconds!
Wrong attempts: 2
Your score is 80 %
```

## 🛠️ Customization

The following constants can be modified in the code to adjust game difficulty:

- `OPERATORS`: Available arithmetic operations
- `MIN_OPERANDS`: Minimum value for operands
- `MAX_OPERANDS`: Maximum value for operands
- `TOTAL_PROBLEMS`: Number of problems in the quiz

## 📊 Scoring

Your score is calculated as: (Number of problems - Wrong attempts) * 10%

Perfect score: 100% (no wrong attempts)

## 💡 Potential Enhancements

- Add division problems
- Implement difficulty levels
- Add a high score tracking system
- Create a graphical user interface
- Add a timer countdown for each problem

## 🤝 Contributing

Contributions to DevVault are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📜 License

This project is part of the DevVault collection and is available under its licensing terms.

---

*Part of the [DevVault](https://github.com/qusai-Kagal/DevVault) collection - A repository of developer resources and projects.*
