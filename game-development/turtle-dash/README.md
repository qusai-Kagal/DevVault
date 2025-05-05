# 🐢 Turtle Dash

A fun and interactive racing game built with Python's turtle module where colorful turtles compete to reach the finish line!

*Part of the [DevVault](https://github.com/qusai-Kagal/DevVault) collection of development projects.*

[![GitHub Repository](https://img.shields.io/badge/GitHub-DevVault-brightgreen)](https://github.com/qusai-Kagal/DevVault/tree/main/game-development/turtle-dash)

## 📋 Description

Turtle Dash is an exciting Python game that simulates a race between 2-10 turtles. Players choose how many racers they want, and then watch as the turtles move forward by random distances in each turn, creating an unpredictable and thrilling race to the finish line. The game leverages Python's built-in turtle graphics module to provide a colorful visual experience.

## ✨ Features

- Select between 2-10 colorful racers
- Randomized movement creates unique races every time
- Visual race track with a clear finish line
- Simple, intuitive interface that's perfect for all ages
- Instant winner announcement

## 🛠️ Requirements

- Python 3.x
- Standard Python libraries (all included in default installation):
  - turtle
  - random
  - time

## 🚀 Installation & Running

```bash
# Clone the DevVault repository
git clone https://github.com/qusai-Kagal/DevVault.git

# Navigate to the turtle-dash project directory
cd DevVault/game-development/turtle-dash

# Run the game
python turtle_race_game.py
```

## 🎮 How to Play

1. Launch the game following the instructions above
2. When prompted, enter a number between 2 and 10 to select the number of racers
3. Watch the exciting race as turtles move toward the finish line
4. The first turtle to reach the top of the screen wins!
5. The winner's color will be displayed in the console


## 🧩 How It Works

The game works through these key components:

- **Turtle Setup**: Creates a race track and initializes turtle racers
- **Race Logic**: Each turtle moves forward a random distance (1-20 pixels) per turn
- **Win Detection**: Checks if any turtle has crossed the finish line
- **User Input**: Validates player input for number of racers
- **Randomization**: Ensures unpredictable and exciting races

## 🔄 Future Enhancements

- Implement a betting system to guess the winning turtle
- Add multiple race tracks with different themes
- Create obstacles that turtles must navigate around
- Add a tournament mode with multiple races
- Include sound effects for more immersion
- Design a graphical user interface for game settings
- Add turtle animations and victory celebrations

## 🐞 Known Issues

None reported yet. If you find any bugs, please [open an issue](https://github.com/qusai-Kagal/DevVault/issues) and mention "turtle-dash" in the title!

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The Python turtle module development team
- Thanks to everyone who has provided feedback and suggestions
- Inspiration from classic arcade racing games
