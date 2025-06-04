# ☕ Coffee Machine OOP

> A Python-based coffee vending machine simulator built with Object-Oriented Programming principles

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![OOP](https://img.shields.io/badge/Programming-OOP-green.svg)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![100 Days of Code](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2016-orange.svg)](https://www.udemy.com/course/100-days-of-code/)

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Classes & Methods](#-classes--methods)
- [Menu Options](#-menu-options)
- [Screenshots](#-screenshots)
- [Learning Objectives](#-learning-objectives)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

This coffee machine simulator demonstrates Object-Oriented Programming concepts through a real-world application. The program models a coffee vending machine that can make different types of coffee drinks, handle payments, manage resources, and provide reports.

**Built as part of Angela Yu's 100 Days of Code - Day 16 Challenge**

## ✨ Features

- 🍵 **Multiple Coffee Options**: Latte, Espresso, and Cappuccino
- 💰 **Coin Payment System**: Accepts quarters, dimes, nickels, and pennies
- 📊 **Resource Management**: Tracks water, milk, and coffee supplies
- 💵 **Change Calculation**: Automatically calculates and returns change
- 📈 **Profit Tracking**: Monitors total earnings
- 🔍 **Resource Reports**: View current supplies and profit
- ⚠️ **Error Handling**: Alerts for insufficient resources or payment

## 📁 Project Structure

```
coffee-machine-oop/
├── main.py           # Main program file with game loop
├── coffee_maker.py   # CoffeeMaker class - handles resources & brewing
├── menu.py          # Menu & MenuItem classes - manages drink options
├── money_machine.py # MoneyMachine class - handles payments
└── README.md        # Project documentation
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/scripts/coffee-machine-oop
   ```

2. **Ensure Python 3.7+ is installed**
   ```bash
   python --version
   ```

3. **Run the program**
   ```bash
   python main.py
   ```

## 🎮 Usage

1. **Start the program**: Run `python main.py`
2. **Choose your drink**: Type `latte`, `espresso`, or `cappuccino`
3. **Insert coins**: Follow prompts to add quarters, dimes, nickels, and pennies
4. **Enjoy your coffee**: The machine will brew your drink and return change
5. **Special commands**:
   - Type `report` to see current resources and profit
   - Type `off` to turn off the machine

### Example Session
```
What would you like (latte/espresso/cappuccino/): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

## 🏗️ Classes & Methods

### 🏭 CoffeeMaker Class
- `__init__()`: Initialize resources (water: 300ml, milk: 200ml, coffee: 100g)
- `report()`: Display current resource levels
- `is_resource_sufficient(drink)`: Check if ingredients are available
- `make_coffee(order)`: Brew coffee and deduct resources

### 📋 Menu & MenuItem Classes
**MenuItem Class:**
- `__init__(name, water, milk, coffee, cost)`: Create drink with recipe and price

**Menu Class:**
- `__init__()`: Initialize menu with available drinks
- `get_items()`: Return formatted string of all menu options
- `find_drink(order_name)`: Find and return specific drink object

### 💳 MoneyMachine Class
- `__init__()`: Initialize profit tracker and money receiver
- `report()`: Display total profit earned
- `process_coins()`: Collect and calculate coin input
- `make_payment(cost)`: Handle payment processing and change

## 📖 Menu Options

| Drink | Water | Milk | Coffee | Cost |
|-------|-------|------|--------|------|
| ☕ Latte | 200ml | 150ml | 24g | $2.50 |
| ☕ Espresso | 50ml | 0ml | 18g | $1.50 |
| ☕ Cappuccino | 250ml | 50ml | 24g | $3.00 |

## 🎓 Learning Objectives

This project demonstrates key OOP concepts:

- ✅ **Classes and Objects**: Creating reusable code structures
- ✅ **Encapsulation**: Keeping data and methods together
- ✅ **Modularity**: Separating concerns into different files
- ✅ **Constructor Methods**: Initializing object state
- ✅ **Instance Variables**: Storing object-specific data
- ✅ **Method Interaction**: Objects working together

## 🛠️ Technologies Used

- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
- ![OOP](https://img.shields.io/badge/OOP-Principles-green)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Qusai Kagalwala**
- 🌐 GitHub: [@qusai-Kagal](https://github.com/qusai-Kagalwala)
- 💼 LinkedIn: [qusai-kagalwala](https://www.linkedin.com/in/qusai-kagalwala/)
- 📧 Email: qusai.kagalwala53@gmail.com

## 🙏 Acknowledgments

- 👩‍🏫 **Angela Yu** - 100 Days of Code Python Bootcamp
- ☕ **Coffee** - For the inspiration
- 🐍 **Python Community** - For amazing documentation

---

⭐ **If you found this project helpful, please give it a star!** ⭐

---

*Made with ❤️ and lots of ☕*
