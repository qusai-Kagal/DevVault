# 🎲 Pig Dice Game

A simple command-line implementation of the classic Pig dice game written in Python.

## 📜 Game Rules

Pig is a traditional dice game that combines luck with strategic decision-making:

- **Players:** 2-4 players
- **Goal:** Be the first player to reach 50 points
- **Gameplay:**
  - Players take turns rolling a six-sided die
  - On each turn, a player can roll as many times as they want
  - Each roll (except 1) adds to the player's turn total
  - If a player rolls a 1, they lose all points accumulated during that turn
  - Players can choose to "hold" (end their turn) at any time to add their turn points to their total score
  - The first player to reach 50 points wins

## ✨ Features

- 🎮 Interactive command-line gameplay
- 👥 Support for 2-4 players
- ✅ Input validation for better user experience
- 🎯 Turn-based scoring system
- 🎲 Randomized dice rolls
- 🏆 Automatic winner detection

## 🚀 How to Run

```bash
python pig.py
```

## 🎮 How to Play

1. Run the game using the command above
2. Enter the number of players (2-4)
3. Each player takes turns rolling the die
4. On your turn:
   - Type 'y' to roll the die
   - Type anything else to hold and end your turn
5. Continue playing until someone reaches 50 points

## 🛠️ Requirements

- Python 3.x
- No additional packages required (uses only standard library)

## 🔧 Customization

You can modify the game by changing:
- `max_score` variable to adjust the winning score
- `min_value` and `max_value` in the roll function to use a different die

## 📝 Example Gameplay

```
How many players? (2 - 4): 2

 Player number 1 's turn has just started.
Your current score is: 0 

Do you want to roll? (y)? y
You rolled a: 4
Your score is: 4
Do you want to roll? (y)? y
You rolled a: 6
Your score is: 10
Do you want to roll? (y)? n
Your total score is: 10

 Player number 2 's turn has just started.
Your current score is: 0 

...
```

## 🔜 Future Improvements

- Add an option for computer-controlled players
- Implement a graphical user interface
- Add different game modes with modified rules
- Save and load game progress

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.
