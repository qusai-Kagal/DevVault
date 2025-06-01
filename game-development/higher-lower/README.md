# 📈 Higher Lower Followers Game 📉

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![DevVault](https://img.shields.io/badge/DevVault-Game%20Development-purple.svg)](https://github.com/qusai-Kagal/DevVault)
[![Day](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2014-red.svg)]()
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)

> 🎯 **Part of [DevVault](https://github.com/qusai-Kagal/DevVault) Game Development Collection**  
> Can you guess who has more followers? Test your knowledge of social media popularity!

## 🎮 Game Overview

A fun console-based guessing game where you compare follower counts of celebrities, brands, and organizations. Keep guessing correctly to build your score streak – one wrong answer ends the game!

### 🌟 Game Features

- 🎲 **50+ Celebrity Accounts** - From Cristiano Ronaldo to NASA
- 🏆 **Score Streak System** - How many can you get right in a row?
- 🎨 **ASCII Art Interface** - Beautiful terminal graphics
- 🔄 **Smart Account Rotation** - Seamless gameplay flow
- 🌍 **Global Diversity** - Accounts from around the world

## 🚀 Quick Play

### Run the Game
```bash
# From DevVault root directory
cd game-development/higher-lower
python main.py
```

### Gameplay
1. 📺 Compare two accounts (A vs B)
2. 🤔 Guess who has more followers
3. ⌨️ Type 'A' or 'B'
4. ✅ Correct = Score +1, continue playing
5. ❌ Wrong = Game over, final score shown

## 📸 Game Preview

```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/

Compare A: Instagram, a Social media platform, from United States.
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Cristiano Ronaldo, a Footballer, from Portugal.
Who has more followers? Type 'A' or 'B': 
```

## 🔧 Technical Implementation

### File Structure
```
higher-lower/
├── main.py          # 🎮 Game logic and main loop
├── art.py           # 🎨 ASCII art (logo & VS display)
├── game_data.py     # 📊 Account database (50+ entries)
└── README.md        # 📖 This documentation
```

### Key Functions
- **`format_data()`** - Formats account info for display
- **`check_answer()`** - Validates user guesses
- **Game Loop** - Handles account rotation and scoring

### 🎪 Sample Data
```python
{
    'name': 'Cristiano Ronaldo',
    'follower_count': 215,  # millions
    'description': 'Footballer',
    'country': 'Portugal'
}
```

## 💡 Learning Outcomes

This project demonstrates:
- 🧩 **Modular Code Design** - Separated data, art, and logic
- 🔄 **Game Loop Implementation** - Continuous gameplay mechanics  
- 🎨 **User Experience** - Screen clearing and visual feedback
- 📊 **Data Management** - Working with structured datasets
- 🎯 **Conditional Logic** - Score tracking and game state

## 🛠️ Customization Ideas

Want to extend this game? Try:
- 📊 Add more account categories (YouTubers, TikTokers)
- 🏆 Implement high score persistence
- 🎨 Create themed ASCII art variations
- 🌐 Add difficulty levels (easy/medium/hard)
- 📱 Build a GUI version with tkinter

## 🎓 100 Days of Code - Day 14

This project is part of Angela Yu's 100 Days of Code Python course, focusing on:
- Higher order functions
- Python dictionaries
- Game development fundamentals
- Code organization and modularity

## 🔗 DevVault Integration

This game is part of my [DevVault](https://github.com/qusai-Kagal/DevVault) coding collection:
- 🎮 **Game Development** - Interactive entertainment projects
- 🧠 **Learning Journey** - Skill development documentation
- 🚀 **Portfolio Showcase** - Demonstrating Python proficiency

## 📞 Connect & Collaborate

**Qusai Kagal** - Building the future, one game at a time!

🔗 **DevVault**: [github.com/qusai-Kagal/DevVault](https://github.com/qusai-Kagal/DevVault)  
🎮 **This Game**: [DevVault/game-development/higher-lower](https://github.com/qusai-Kagal/DevVault/tree/main/game-development/higher-lower)

---

⬆️ **[Back to DevVault](https://github.com/qusai-Kagal/DevVault)** | 🎮 **[More Games](../README.md)** | 🚀 **[All Projects](../../README.md)**
