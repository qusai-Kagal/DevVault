# 🎯 Python Hangman Game

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![100 Days of Code](https://img.shields.io/badge/100%20Days%20of%20Code-Day%207-orange.svg)](https://www.udemy.com/course/100-days-of-code/)
[![DevVault](https://img.shields.io/badge/DevVault-Game%20Development-purple.svg)](https://github.com/qusai-Kagal/DevVault)

> **Part of the [DevVault](https://github.com/qusai-Kagal/DevVault) Collection** 🗃️  
> A curated collection of development projects and learning resources

## 📖 Overview

A classic terminal-based hangman word-guessing game featuring beautiful ASCII art and an engaging user interface. This project demonstrates fundamental Python programming concepts and game development principles.

**🎓 Learning Context:** Angela Yu's 100 Days of Code Python Bootcamp - Day 7

## ✨ Game Features

- 🎲 **Random Word Selection** - 200+ challenging words from diverse categories
- 🎨 **Progressive ASCII Art** - 7-stage hangman gallows animation
- 💖 **Lives System** - Strategic 6-life gameplay
- 🔄 **Smart Input Handling** - Duplicate guess prevention
- 🏆 **Clear Win/Lose States** - Immediate feedback and outcomes
- 📱 **Clean Terminal UI** - Intuitive user experience

## 🚀 Quick Start

```bash
# Navigate to the hangman directory
cd game-development/python-hangman

# Run the game
python main.py
```

## 🎮 How to Play

1. **Start**: The game displays a mystery word as underscores (`_ _ _ _`)
2. **Guess**: Enter one letter at a time
3. **Progress**: Correct guesses reveal letter positions
4. **Stakes**: Wrong guesses draw the hangman and cost lives
5. **Win**: Complete the word before losing all 6 lives!
6. **Lose**: The hangman is fully drawn - game over!

## 📁 File Structure

```
python-hangman/
│
├── main.py           # 🎮 Core game logic and main loop
├── hangman_art.py    # 🎨 ASCII art assets (logo + gallows stages)
├── hangman_words.py  # 📚 Curated word database
└── README.md         # 📖 This documentation
```

## 💻 Game Preview

```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

Word to guess: _ _ _ _ _ _ _
****************************6/6 LIVES LEFT****************************
Guess a letter: t

Word to guess: t _ _ _ _ _ _
****************************6/6 LIVES LEFT****************************
Guess a letter: e

Word to guess: t e _ _ _ _ e
```

## 🛠️ Technical Implementation

### Core Technologies
- **Python 3.6+** - Primary language
- **Random Module** - Word selection algorithm
- **String Manipulation** - Display logic
- **Control Flow** - Game state management

### Key Programming Concepts Demonstrated
- 🔁 **While Loops** - Game loop implementation
- 📋 **List Operations** - Word and letter management  
- 🔀 **Conditionals** - Game logic branching
- 🎯 **Functions** - Modular code organization
- 📝 **String Methods** - Input processing

## 🎯 Learning Outcomes

This project reinforces essential programming fundamentals:

- **Game Development Basics** - State management, user input, win conditions
- **Python Data Structures** - Lists, strings, and their methods
- **Logic Flow** - Nested conditionals and loop control
- **User Experience** - Clear feedback and intuitive interfaces
- **Code Organization** - Separation of concerns across modules

## 🔧 Customization Ideas

Want to extend the game? Try these enhancements:

- 🏅 **Scoring System** - Points based on word difficulty and remaining lives
- 🎯 **Difficulty Levels** - Word length and complexity categories  
- 📊 **Statistics** - Track wins, losses, and favorite letters
- 🎵 **Sound Effects** - Audio feedback for correct/incorrect guesses
- 🌐 **Categories** - Themed word lists (animals, countries, movies)
- 💾 **Save Progress** - Resume interrupted games

## 🌟 Part of DevVault

This hangman game is part of the **DevVault collection** - a comprehensive repository showcasing various development projects, learning exercises, and coding challenges. 

**🔗 Explore More Projects:**
- [🏠 DevVault Home](https://github.com/qusai-Kagal/DevVault)
- [🎮 Game Development](https://github.com/qusai-Kagal/DevVault/tree/main/game-development)
- [📚 Other Learning Projects](https://github.com/qusai-Kagal/DevVault)

## 📚 Educational Value

Perfect for:
- 🐍 **Python Beginners** - Practical application of basic concepts
- 🎮 **Game Development** - Introduction to game logic and state management
- 📖 **Code Reading** - Well-commented, beginner-friendly code structure
- 🏗️ **Project Structure** - Understanding modular programming

## 🤝 Contributing to DevVault

Found a bug or have an enhancement idea? Contributions are welcome!

1. Fork the [DevVault repository](https://github.com/qusai-Kagal/DevVault)
2. Create your feature branch (`git checkout -b feature/hangman-enhancement`)
3. Commit your changes (`git commit -m 'Add cool new feature'`)
4. Push to the branch (`git push origin feature/hangman-enhancement`)
5. Open a Pull Request

## 📄 License

This project is part of the DevVault collection and follows the repository's licensing terms.

## 🙏 Acknowledgments

- **Angela Yu** - Exceptional Python instruction and course design
- **100 Days of Code Community** - Motivation and learning support
- **Python Community** - Continuous inspiration and best practices

---

⭐ **If you found this helpful, consider starring the [DevVault repository](https://github.com/qusai-Kagal/DevVault)!** ⭐
