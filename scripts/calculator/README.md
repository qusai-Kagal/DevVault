# 🧮 Calculator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![100 Days of Code](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2010-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-success?style=flat-square)

A functional Python calculator program from **Day 10** of Angela Yu's 100 Days of Code course. Features basic arithmetic operations with ASCII art interface and chain calculation capabilities.

## ✨ Features

- 🔢 **Basic Operations**: Addition, Subtraction, Multiplication, Division
- 🎨 **ASCII Art Display**: Beautiful calculator interface
- 🔄 **Chain Calculations**: Continue with results or start fresh
- 💻 **Interactive**: User-friendly prompts and clear output

## 🚀 Quick Start

```bash
# Navigate to calculator directory
cd scripts/calculator

# Run the calculator
python main.py
```

## 📋 Usage Example

```
What is the first number?: 15
+
-
*
/
Pick an operation: *
What is the next number?: 3
15.0 * 3.0 = 45.0
Type 'y' to continue calculating with 45.0, or type 'n' to start a new calculation: y
```

## 📁 Files

- `main.py` - Main calculator program with all functionality
- `art.py` - ASCII art logo for visual appeal

## 🎯 Learning Objectives

- ✅ **Function Creation**: Modular arithmetic operations
- ✅ **Dictionary Usage**: Mapping symbols to functions  
- ✅ **Control Flow**: While loops and conditionals
- ✅ **User Interaction**: Input handling and validation
- ✅ **Code Organization**: Separating logic and display

## 🛠️ Code Structure

```python
# Function-based arithmetic operations
def add(n1, n2): return n1 + n2

# Dictionary mapping for clean operation selection
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# Main calculator loop with accumulation logic
calculator()
```

## 📚 Part of DevVault

This calculator is part of the [DevVault](https://github.com/qusai-Kagal/DevVault) collection - a comprehensive coding vault containing projects across web development, AI/ML, data science, and more.

---

**Built with ❤️ during 100 Days of Code Challenge**
