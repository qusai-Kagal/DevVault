# 🔐 Password Generator

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![DevVault](https://img.shields.io/badge/DevVault-Scripts-purple.svg)
![Security](https://img.shields.io/badge/Security-Tool-red.svg)

A simple yet effective password generator script that's part of the DevVault developer tools collection. Create customizable passwords with user-defined character counts and ordering options.


## ✨ Features

🔤 **Custom Character Counts**: Specify exact numbers of letters, symbols, and numbers  
🎯 **Two Generation Modes**: Easy (ordered) or Hard (shuffled) arrangement  
🔐 **Secure Character Sets**: Letters (a-z, A-Z), symbols, and digits  
💻 **Interactive CLI**: Simple prompts for user input  
⚡ **Instant Generation**: Fast password creation  
🎲 **Randomized Selection**: Uses Python's random module for character selection  
🔄 **Flexible Output**: Choose between predictable or randomized character order  

## 🚀 Quick Start

### Prerequisites

- 🐍 Python 3.6 or higher
- Standard library modules (no external dependencies)

### Installation

1. Clone the DevVault repository:
```bash
git clone https://github.com/qusai-Kagal/DevVault.git
cd DevVault/scripts/password-generator
```

2. Run the password generator:
```bash
python main.py
```

### Usage

Simply run the script and follow the interactive prompts:

```bash
python main.py
```

## 📖 Usage Examples

### Interactive Session
```bash
$ python main.py

Choose password type: Type 'easy' for ordered or 'hard' for shuffled: hard
How many letters would you like in your password? 8
How many symbols would you like? 4
How many numbers would you like? 2

Your password is: a2!bK#c$dF1efgh
```

### Mode Examples

**Easy Mode** (ordered arrangement):
```
Input: 6 letters, 3 symbols, 2 numbers
Output: abcdef!#$12
Pattern: [letters][symbols][numbers]
```

**Hard Mode** (shuffled arrangement):
```
Input: 6 letters, 3 symbols, 2 numbers  
Output: 2a!bF#c$1def
Pattern: Completely randomized order
```

## 🛠️ How It Works

### User Input Process
1. **Mode Selection**: Choose 'easy' (ordered) or 'hard' (shuffled)
2. **Character Count**: Specify number of letters, symbols, and numbers
3. **Generation**: Script creates password based on your preferences

### Character Sets Used
- **Letters**: `string.ascii_letters` (a-z, A-Z) - 52 characters
- **Symbols**: `['!', '#', '$', '%', '&', '(', ')', '*', '+']` - 9 characters  
- **Numbers**: `string.digits` (0-9) - 10 characters

### Generation Logic
- **Easy Mode**: Concatenates characters in order (letters + symbols + numbers)
- **Hard Mode**: Shuffles all characters using `random.shuffle()` for maximum randomization

## 🎯 Technical Implementation

### Core Dependencies
```python
import random      # For character selection and shuffling
import string      # For pre-defined character sets
```

### Key Functions
- **Character Generation**: List comprehensions with `random.choice()`
- **Mode Handling**: Conditional logic for easy/hard modes
- **Input Processing**: `int()` conversion with user prompts
- **Output Formatting**: `''.join()` for string concatenation

### Algorithm Overview
1. Collect user preferences (mode and character counts)
2. Generate separate lists for each character type
3. Combine lists and apply mode-specific processing
4. Output final password string

## 🔧 Technical Details

### Dependencies
```python
import random   # Built-in module for randomization
import string   # Built-in module for character sets
```

### Core Implementation
- **List Comprehensions**: Efficient character generation
- **Random Selection**: `random.choice()` for secure character picking
- **Conditional Logic**: Mode-based password arrangement
- **String Operations**: Joining and concatenation methods

### Code Structure
```python
# Character pool setup
letters = list(string.ascii_letters)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = list(string.digits)

# Generation with list comprehensions
password_letters = [random.choice(letters) for _ in range(num_letters)]

# Mode-based output
if mode == 'hard':
    random.shuffle(password_chars)
```

## 📁 File Structure

```
password-generator/
│
├── main.py                 # Main password generator script
├── README.md              # This documentation
└── examples/              # Usage examples and demos
    └── sample_output.txt
```

## 🧪 Testing

Test the script with different inputs:

```bash
# Test easy mode
python main.py
# Enter: easy, 5, 3, 2

# Test hard mode  
python main.py
# Enter: hard, 8, 4, 3

# Edge cases
python main.py
# Enter: hard, 0, 10, 0  (symbols only)
```

## 🤝 Contributing to DevVault

![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

This script is part of the DevVault project. To contribute:

1. 🍴 Fork the [DevVault repository](https://github.com/qusai-Kagal/DevVault)
2. 🌟 Create a feature branch (`git checkout -b feature/password-enhancement`)
3. 💾 Make your changes in the `scripts/password-generator/` directory
4. 🧪 Add tests for new functionality
5. 📤 Submit a pull request to the main DevVault repository

## 💡 Enhancement Ideas

- 🎨 Add GUI interface using tkinter
- 📋 Copy to clipboard functionality  
- 🔄 Generate multiple passwords in one session
- 📊 Password strength estimation
- 💾 Save passwords to file option
- 🚫 Option to exclude ambiguous characters (0, O, l, 1)
- ⚙️ Command-line argument support
- 🔐 Integration with `secrets` module for cryptographic randomness

## 🔗 Related DevVault Tools

Check out other security tools in the DevVault collection:
- `scripts/hash-generator/` - Generate various hash types
- `scripts/encryption-tools/` - File encryption utilities  
- `scripts/network-scanner/` - Network security scanner
- `scripts/log-analyzer/` - Security log analysis

## 📄 License

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file in the DevVault repository for details.

## 👨‍💻 Author

**Qusai Kagal**
- GitHub: [@qusai-Kagal](https://github.com/qusai-Kagal)
- DevVault: [Repository](https://github.com/qusai-Kagal/DevVault)

## 🙏 Acknowledgments

- 🔐 OWASP for password security guidelines
- 💡 The cybersecurity community for best practices
- 🛠️ DevVault contributors and users

---

![DevVault](https://img.shields.io/github/stars/qusai-Kagal/DevVault?style=social)

⭐ **Star the DevVault repository if you found this tool helpful!** ⭐

**Part of DevVault - Developer Tools Collection** 🧰
