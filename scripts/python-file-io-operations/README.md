# 🐍 Python File I/O Operations

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

> 📁 A comprehensive collection of Python file input/output operations demonstrating practical applications of file handling, data persistence, and text processing.

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [🚀 Projects](#-projects)
- [🛠️ Installation](#️-installation)
- [📖 Usage](#-usage)
- [🏗️ Project Structure](#️-project-structure)
- [🔧 Features](#-features)
- [📝 Examples](#-examples)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Overview

This repository contains Python projects that demonstrate various file I/O operations including:

- **File Reading & Writing** 📖✍️
- **Data Persistence** 💾
- **Text Processing** 🔤
- **Template Systems** 📄
- **Score Management** 🏆

Perfect for learning file handling concepts and practical applications in Python development.

## 🚀 Projects

### 1. 📬 Mail Merge System
**Automated personalised letter generation**

- **File**: `main.py` (Mail Merge)
- **Purpose**: Generate personalised invitation letters from templates
- **Features**:
  - Template-based letter generation
  - Bulk processing from name lists
  - Automated file creation
  - Placeholder replacement system

### 2. 🐍 Snake Game with Persistence
**Classic Snake game with high score tracking**

- **Files**: `main.py`, `snake.py`, `food.py`, `scoreboard.py`
- **Purpose**: Demonstrate game state persistence and score management
- **Features**:
  - Persistent high score storage
  - Real-time score tracking
  - File-based data management
  - Game state reset functionality

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- turtle module (included with Python)

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/qusai-Kagal/DevVault.git

# Navigate to the project directory
cd DevVault/scripts/python-file-io-operations

# Run the mail merge system
python main.py

# Or run the Snake game
python snake_game/main.py
```

## 📖 Usage

### Mail Merge System

1. **Prepare your files**:
   - Add names to `Input/Names/invited_names.txt`
   - Customise template in `Input/Letters/starting_letter.txt`

2. **Run the program**:
   ```bash
   python main.py
   ```

3. **Find generated letters**:
   - Check `Output/ReadyToSend/` folder
   - Each person gets a personalised letter

### Snake Game

1. **Start the game**:
   ```bash
   python snake_game/main.py
   ```

2. **Controls**:
   - ⬆️ **Up Arrow**: Move up
   - ⬇️ **Down Arrow**: Move down
   - ⬅️ **Left Arrow**: Move left
   - ➡️ **Right Arrow**: Move right

3. **High Score**:
   - Automatically saved to `data.txt`
   - Persists between game sessions

## 🏗️ Project Structure

```
python-file-io-operations/
├── 📁 mail-merge/
│   ├── main.py                 # Mail merge main script
│   ├── 📁 Input/
│   │   ├── 📁 Names/
│   │   │   └── invited_names.txt
│   │   └── 📁 Letters/
│   │       └── starting_letter.txt
│   └── 📁 Output/
│       └── 📁 ReadyToSend/
│           └── (generated letters)
├── 📁 snake-game/
│   ├── main.py                 # Game main loop
│   ├── snake.py                # Snake class
│   ├── food.py                 # Food class
│   ├── scoreboard.py           # Score management
│   └── data.txt                # High score storage
└── README.md                   # This file
```

## 🔧 Features

### 📧 Mail Merge Features
- ✅ **Template Processing**: Dynamic placeholder replacement
- ✅ **Bulk Operations**: Process multiple recipients at once
- ✅ **File Management**: Organised input/output structure
- ✅ **Error Handling**: Robust file operation handling

### 🎮 Snake Game Features
- ✅ **Score Persistence**: High scores saved between sessions
- ✅ **Game State Management**: Automatic reset functionality
- ✅ **File I/O Operations**: Read/write score data
- ✅ **Data Validation**: Proper file handling and error management

## 📝 Examples

### Mail Merge Template
```text
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Qusai
```

### Names File Format
```text
Alra Benn
Emme
Ibran Bay
Maysa
Amel Mamo
```

### Generated Output
```text
Dear Alra Benn,

You are invited to my birthday this Saturday.

Hope you can make it!

Qusai
```

## 🎯 Learning Objectives

After exploring these projects, you'll understand:

- **File Operations**: Reading from and writing to files
- **Data Persistence**: Maintaining data between program runs
- **Text Processing**: String manipulation and template systems
- **Error Handling**: Proper file operation error management
- **Project Structure**: Organising file-based applications

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### 💡 Ideas for Contributions
- Add more file format support (JSON, CSV, XML)
- Implement additional template features
- Add error logging functionality
- Create GUI versions of the applications
- Add unit tests for file operations

## 📞 Contact

**Qusai Kagalwala**
- 📧 Email: qusai.kagalwala53@gmail.com
- 💼 LinkedIn: [qusai-kagalwala](https://www.linkedin.com/in/qusai-kagalwala/)
- 🐙 GitHub: [qusai-Kagal](https://github.com/qusai-Kagalwala)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 🌟 Show Your Support

If you found this project helpful, please consider:
- ⭐ **Starring** the repository
- 🍴 **Forking** it for your own use  
- 📢 **Sharing** it with others
- 🐛 **Reporting** any issues you find

**Happy Coding!** 🚀
