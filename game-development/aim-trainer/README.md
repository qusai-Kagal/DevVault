# 🎯 Aim Trainer

A fast-paced target practice game built with Python and Pygame to help improve your mouse accuracy and reaction time.

## 🎮 Game Overview

Challenge yourself with this arcade-style aim trainer where targets appear randomly on screen and grow/shrink dynamically. Click them before they disappear to score points, but be careful - you only have 3 lives!

### Key Features
- **Dynamic Targets**: Targets grow and shrink with smooth animations
- **Lives System**: 3 lives to maintain your streak
- **Real-time Stats**: Track your speed (targets/second), accuracy, and hits
- **Clean UI**: Minimalist design with clear statistics display
- **End Screen**: Detailed performance summary at game over

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Pygame library

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/game-development/aim-trainer
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python aim_trainer.py
   ```

## 🎯 How to Play

1. **Start the Game**: Run the script to launch the aim trainer
2. **Target Practice**: Click on the red and white bullseye targets as they appear
3. **Beat the Clock**: Targets grow then shrink - click them before they disappear
4. **Track Your Stats**: Monitor your performance in the top bar
5. **Stay Alive**: You lose a life when a target disappears - game ends at 0 lives

### Controls
- **Mouse**: Aim and click targets
- **Any Key**: Exit end screen
- **Close Window**: Quit game

## 📊 Game Mechanics

### Target Behavior
- Targets spawn at random locations every 400ms
- Each target grows to maximum size then shrinks until it disappears
- Hitting a target removes it immediately and adds to your score

### Scoring System
- **Hits**: Total targets successfully clicked
- **Speed**: Targets hit per second
- **Accuracy**: Percentage of clicks that hit targets
- **Lives**: Start with 3, lose 1 for each missed target

### Game Area
- **Resolution**: 800x600 pixels
- **Safe Zones**: Targets spawn away from screen edges
- **Top Bar**: Reserved for statistics display

## 🛠️ Technical Implementation

### Built With
- **Python 3**: Core programming language
- **Pygame**: Graphics and game engine library

### Code Structure
- `Target` class: Handles target creation, animation, and collision detection
- Game loop: Manages events, updates, and rendering at 60 FPS
- Statistics tracking: Real-time performance calculations
- End screen: Final results display with centered text

### Key Functions
- `draw()`: Renders all game elements
- `draw_top_bar()`: Updates statistics display
- `end_screen()`: Shows final performance summary
- `format_time()`: Converts seconds to MM:SS.mmm format

## 🎨 Customization Options

Want to modify the game? Here are some easy tweaks:

```python
# Target settings
TARGET_INCREMENT = 400    # Spawn rate (milliseconds)
Target.MAX_SIZE = 30      # Maximum target size
Target.GROWTH_RATE = 0.2  # Animation speed

# Game settings
LIVES = 3                 # Starting lives
WIDTH, HEIGHT = 800, 600  # Window dimensions
BG_COLOR = (0, 25, 40)    # Background color
```

## 📈 Performance Tips

- **Warm Up**: Start with a few practice rounds
- **Focus**: Keep your eyes moving across the screen
- **Rhythm**: Find a consistent clicking pattern
- **Accuracy vs Speed**: Balance quick reactions with precise aiming

## 🔧 Troubleshooting

**Game won't start?**
- Ensure Python 3.6+ is installed
- Verify Pygame installation: `python -c "import pygame"`

**Performance issues?**
- Close other applications to free up system resources
- Check that your system meets minimum requirements

## 📝 Future Enhancements

Potential improvements for future versions:
- [ ] Difficulty levels with varying target speeds
- [ ] Power-ups and special targets
- [ ] Sound effects and background music
- [ ] High score persistence
- [ ] Different target shapes and patterns
- [ ] Multiplayer competition mode

## 🤝 Contributing

This project is part of my personal learning journey, but suggestions and improvements are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Share your high scores!

## 📄 License

This project is licensed under the MIT License - see the main [DevVault LICENSE](../../LICENSE) for details.

## 🎯 Challenge Yourself!

Can you achieve:
- ✨ 95%+ accuracy?
- ⚡ 5+ targets per second?
- 🔥 50+ consecutive hits?

Share your best scores and compete with friends!

---

*Part of the [DevVault](https://github.com/qusai-Kagal/DevVault) collection - building skills one project at a time! 🚀*
