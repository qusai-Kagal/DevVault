# 🧠 Trivia Quiz Game

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)
![Game](https://img.shields.io/badge/Type-Terminal%20Game-green?style=for-the-badge)
![OOP](https://img.shields.io/badge/Concept-OOP-purple?style=for-the-badge)
![Course](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2017-orange?style=for-the-badge)

> **Part of [DevVault](../../) Game Development Collection**

An interactive terminal-based quiz game demonstrating object-oriented programming principles. Test your computer science knowledge with 10 carefully curated True/False questions!

## 🎮 Game Features

- 🎯 **Interactive Gameplay** - Terminal-based question-answer format
- 📊 **Live Score Tracking** - See your progress after each question  
- 💻 **CS-Themed Questions** - Computer science trivia from Open Trivia Database
- ✅ **Instant Feedback** - Know immediately if you're right or wrong
- 🏆 **Final Results** - Complete score summary at the end

## 🚀 Quick Start

```bash
# Navigate to the game directory
cd game-development/trivia-quiz

# Run the game
python main.py
```

**That's it!** Answer with `True` or `False` and test your knowledge! 🧠

## 📁 File Structure

```
trivia-quiz/
├── main.py           # 🎮 Game entry point & orchestration
├── question_model.py # 📝 Question data structure
├── quiz_brain.py     # 🧠 Game logic & flow control
├── data.py          # 📊 Question database with HTML decoding
└── README.md        # 📖 This documentation
```

## 🎯 How to Play

1. **Start the game** by running `python main.py`
2. **Read each question** carefully
3. **Type your answer**: `True` or `False` (case doesn't matter!)
4. **Press Enter** to submit
5. **View feedback** and your current score
6. **Continue** until all 10 questions are complete
7. **See your final score** and celebrate! 🎉

## 🛠️ Technical Implementation

### 🏗️ Architecture Overview

This project demonstrates clean **Object-Oriented Design**:

```python
# Three main components working together
Question()    # Data model for storing questions
QuizBrain()   # Game engine managing flow & logic  
main.py       # Orchestrator bringing it all together
```

### 🔧 Key OOP Concepts

- **📦 Encapsulation** - Data and methods bundled in classes
- **🎯 Single Responsibility** - Each class has one clear purpose
- **🔄 Method Design** - Logical separation of functionality
- **📊 State Management** - Tracking score and progress

### 💡 Code Highlights

```python
# Clean class design
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
```

## 📋 Sample Questions

Test yourself with questions like:
- 💾 RAM stands for Random Access Memory
- 🌐 JavaScript derives from a later version of Java  
- 👩‍💻 Ada Lovelace is considered the first computer programmer
- 📝 HTML stands for Hypertext Markup Language

## 🎓 Learning Outcomes

Building this game teaches:
- ✅ Python class creation and instantiation
- ✅ Object method design and interaction
- ✅ Game loop implementation
- ✅ User input validation and handling
- ✅ Data structure management
- ✅ HTML entity decoding for clean text display

## 🔮 Potential Enhancements

- [ ] 🎲 **Random question order** for replayability
- [ ] ⏱️ **Timer functionality** for added challenge  
- [ ] 🏅 **High score persistence** with file storage
- [ ] 🌐 **Multiple categories** (History, Science, Sports)
- [ ] 🎨 **Colorful terminal output** with rich library
- [ ] 📱 **GUI version** using tkinter or PyQt

## 🎯 Part of DevVault

This project is part of my **[DevVault](../../)** collection - a comprehensive coding portfolio showcasing projects across:

- 🌐 Web Development
- 📱 App Development  
- 🤖 AI/ML Projects
- 📊 Data Science
- 🎮 **Game Development** ← *You are here!*
- 🛠️ Scripts & Utilities

## 📚 Course Context

- **Course**: 100 Days of Code - Python Bootcamp by Angela Yu
- **Day**: 17 - Object-Oriented Programming
- **Focus**: Classes, Objects, and Method Design
- **Level**: Beginner to Intermediate

## 👨‍💻 About the Developer

**Qusai Kagalwala** - Passionate about creating clean, educational code

[![GitHub](https://img.shields.io/badge/GitHub-qusai--Kagal-181717?style=flat&logo=github)](https://github.com/qusai-Kagal)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-qusai--kagalwala-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/qusai-kagalwala/)

---

⭐ **Enjoyed this game? Star the [DevVault repo](../../) and check out other projects!** ⭐
