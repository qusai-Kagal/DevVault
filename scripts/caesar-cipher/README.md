# 🔐 Caesar Cipher

*Part of the DevVault Scripts Collection*

A simple and interactive Python implementation of the classic Caesar cipher encryption technique. This script demonstrates fundamental cryptographic concepts through an easy-to-use command-line interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![100 Days of Code](https://img.shields.io/badge/100%20Days%20of%20Code-Day%208-orange?style=flat-square)

## 📋 Overview

The Caesar cipher is one of the simplest and most widely known encryption techniques, where each letter in the plaintext is shifted a certain number of places down or up the alphabet. This implementation was created as part of **Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** (Day 8).

## ✨ Features

- 🔒 **Encrypt** messages with customizable shift values
- 🔓 **Decrypt** messages back to original text
- 🎨 **ASCII Art Logo** for enhanced user experience
- 🔤 **Preserves Special Characters** (spaces, numbers, punctuation)
- 🔄 **Continuous Operation** - perform multiple encryptions without restart
- 📝 **Case Insensitive** input handling

## 🚀 Quick Start

### Prerequisites
```bash
pip install art
```

### Usage
```bash
python main.py
```

### Example Session
```
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode

Type your message:
> secret message

Type the shift number:
> 3

Here is the encoded result: vhfuhw phvvdjh

Type 'yes' if you want to go again. Otherwise, type 'no'.
> no
Goodbye
```

## 🔧 How It Works

The algorithm follows these steps:

1. **Input Processing**: Convert message to lowercase
2. **Character Mapping**: Find each letter's position in the alphabet (a=0, b=1, ..., z=25)
3. **Shift Application**: Add shift value to position
4. **Modulo Wrapping**: Use `position % 26` to wrap around alphabet
5. **Character Reconstruction**: Convert back to letters
6. **Special Character Preservation**: Keep non-alphabetic characters unchanged

### Algorithm Example
```
Original alphabet: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Shift +3:          D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

"hello" with shift 3 → "khoor"
```

## 📁 File Structure

```
caesar-cipher/
├── main.py          # Main program with Caesar cipher logic
├── art.py           # ASCII art logo (if separate)
└── README.md        # This documentation
```

## 🔑 Key Concepts Demonstrated

- **Function Design**: Modular code with parameters
- **String Manipulation**: Character-by-character processing  
- **List Operations**: Using alphabet arrays for mapping
- **Modulo Arithmetic**: Wrapping values within bounds
- **User Input Handling**: Interactive command-line interface
- **Control Flow**: Loops and conditional statements

## 💡 Educational Value

This project is perfect for learning:
- Basic cryptography concepts
- Python string and list operations
- Function parameter usage
- Interactive program design
- Mathematical operations in programming

## 🔗 Related Scripts

*Check out other scripts in the [DevVault](../../) collection for more development tools and learning projects.*

## 📚 References

- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Angela Yu's 100 Days of Code](https://www.udemy.com/course/100-days-of-code/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---

*⭐ Part of the DevVault Scripts Collection - Building one script at a time!*
