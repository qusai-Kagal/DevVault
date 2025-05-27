# 🤖 Reeborg Maze Solver

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Reeborg's World](https://img.shields.io/badge/Reeborg's_World-Educational-green?style=for-the-badge)](https://reeborg.ca/reeborg.html)
[![100 Days of Code](https://img.shields.io/badge/100_Days_of_Code-Day_6-blue?style=for-the-badge)](https://www.udemy.com/course/100-days-of-code/)
[![AI/ML](https://img.shields.io/badge/AI/ML-Pathfinding-orange?style=for-the-badge)](https://github.com/qusai-Kagal/DevVault/tree/main/ai-ml)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

🐍 A Python solution for navigating mazes in Reeborg's World using the right-hand rule algorithm 🧭

## 📖 About

🎓 This project is part of **Angela Yu's 100 Days of Code** course (Day 6), focusing on algorithmic thinking and robot navigation. The solution demonstrates autonomous pathfinding using a classic maze-solving algorithm.

### 🏷️ Tags
`python` `robotics` `pathfinding` `algorithms` `ai-basics` `maze-solver` `reeborg` `100-days-of-code` `angela-yu` `education`

## 🎯 Problem

🏃‍♂️ Navigate Reeborg the robot through various maze configurations to reach the goal position using only basic movement and sensing commands.

## 🧠 Algorithm: Right-Hand Rule

The solution implements the **right-hand wall-following algorithm** 🧱➡️:

1. **🔄 Always try right first** - If the right side is clear, turn right and move
2. **⬆️ Go straight if possible** - If right is blocked, move forward if path is clear  
3. **↩️ Turn left as last resort** - If both right and front are blocked, turn left

✅ This algorithm guarantees finding the exit in any simply-connected maze.

## 💻 Code

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

## 🔧 How It Works

1. **🔄 Custom Function**: `turn_right()` - Since Reeborg only has `turn_left()`, we create turn right by turning left three times
2. **🔁 Main Loop**: Continues until robot reaches the goal
3. **🌳 Decision Tree**: Prioritizes right turns, then forward movement, then left turns
4. **👁️ Sensors**: Uses `right_is_clear()` and `front_is_clear()` to make decisions

## 🚀 Features

- ✅ Works on any simply-connected maze
- ✅ Efficient pathfinding strategy
- ✅ Clean, readable code
- ✅ No hardcoded moves - fully algorithmic
- ✅ Handles various maze configurations

## 🚀 Usage

1. 🌐 Visit [Reeborg's World](https://reeborg.ca/reeborg.html)
2. 🎮 Select a maze challenge (Day 6 levels)
3. 📋 Copy and paste the code into the editor
4. ▶️ Run and watch Reeborg solve the maze!

## 🧩 Key Concepts Learned

- **🧠 Algorithmic Thinking**: Breaking down complex problems into simple rules
- **🤖 Robot Navigation**: Basic autonomous movement strategies
- **🎯 Decision Making**: Using sensors to make intelligent choices
- **♻️ Code Reusability**: Creating helper functions for common operations

## 📚 Part of Learning Journey

This project represents foundational concepts in:
- **🤖 Robotics**: Autonomous navigation and pathfinding
- **🧠 AI**: Rule-based decision making systems
- **⚙️ Algorithms**: Classic maze-solving techniques

## 🎓 Course Context

**📅 100 Days of Code - Day 6**
- **👩‍🏫 Instructor**: Angela Yu
- **🎯 Focus**: Functions, loops, and algorithmic problem solving
- **🌐 Platform**: Reeborg's World educational environment

## 🏆 Why This Matters

The right-hand rule is more than just a coding exercise - it's a fundamental algorithm used in:
- 🤖 Robot navigation systems
- 🎮 Game AI pathfinding
- 📊 Graph traversal problems
- 🏛️ Real-world maze solving

## 📈 Next Steps

This foundational work opens doors to:
- 🗺️ More complex pathfinding algorithms (A*, Dijkstra)
- 🦾 Advanced robotics navigation
- 🧠 Machine learning applications in navigation
- 🎯 Game development AI

---

💻 *Built with ❤️ as part of my coding journey in DevVault*

### 🔗 Connect & Follow
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/qusai-Kagal)
[![DevVault](https://img.shields.io/badge/DevVault-Main_Repo-blue?style=for-the-badge)](https://github.com/qusai-Kagal/DevVault)
