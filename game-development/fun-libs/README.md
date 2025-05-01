# 📝 Fun-Libs: A Mad Libs Story Generator 🤣

## 📖 Overview

Fun-Libs is a simple yet entertaining Mad Libs-style story generator written in Python. It takes a template story containing placeholders and prompts users to fill in words, creating hilariously unpredictable stories each time!

## ✨ Features

- 🔄 Dynamically identifies all placeholders in story templates
- 🧠 Intelligently asks for each unique word type only once
- 📚 Works with any story template that uses `<placeholder>` format
- 😂 Creates fun, personalized stories based on user input
- 🎭 Includes sample story templates to get you started
- 🎮 Perfect for game nights or classroom activities

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- No external dependencies required! 🎉

### Installation

1. Clone the DevVault repository:
   ```
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/game-development/fun-libs
   ```

2. Create a story template file (example: `story.txt`) with placeholders in the format `<word_type>`:
   ```
   Once upon a time, there was a <adjective> <animal> who loved to <verb> in the <adjective> forest.
   ```

3. Run the script:
   ```
   python madlibs_generator.py
   ```

4. Follow the prompts and enjoy your hilarious story!

## 🎮 How It Works

1. The script reads a story template from `story.txt`
2. It identifies all placeholders within `< >` tags
3. It prompts you to enter words for each placeholder type
4. It replaces the placeholders with your words
5. It displays your completed, often hilarious, story

## 📝 Creating Story Templates

Create your own story templates in a text file named `story.txt` or add them to the `templates` folder. Use angle brackets to define placeholders:

- `<noun>` - Will prompt for a noun
- `<adjective>` - Will prompt for an adjective
- `<verb>` - Will prompt for a verb
- `<proper_noun>` - Will prompt for a "proper noun"
- `<animal>` - Will prompt for an animal
- `<place>` - Will prompt for a place

Example:
```
The <adjective> <animal> went to the <place> to <verb> with a <adjective> <noun>.
```

### 📚 Sample Templates

The project includes several ready-to-use templates in the `templates` folder to get you started!

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new story templates to the `templates` folder
- Improve the code functionality
- Suggest new features

Please follow the contribution guidelines in the main [DevVault repository](https://github.com/qusai-Kagal/DevVault).

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by the classic Mad Libs word game
- Thanks to all contributors and users who share their funny stories!

---

Made with ❤️ and 😂 by [Qusai Kagal](https://github.com/qusai-Kagal)
