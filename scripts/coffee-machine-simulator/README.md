# ☕ Coffee Machine Simulator

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![CLI](https://img.shields.io/badge/interface-CLI-green.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)
![100DaysOfCode](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2015-orange.svg)

A command-line coffee machine simulator that recreates the experience of ordering coffee from a real machine. Built as part of Angela Yu's 100 Days of Code challenge to demonstrate Python fundamentals and object-oriented programming concepts.

## 🎯 Purpose

This script simulates a coffee machine interface where users can:
- Order different types of coffee (Espresso, Latte, Cappuccino)
- Pay using virtual coins (quarters, dimes, nickels, pennies)
- Receive change and manage machine resources
- Access admin features for maintenance

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/qusai-Kagal/DevVault.git

# Navigate to the script
cd DevVault/scripts/coffee-machine-simulator

# Run the coffee machine
python main.py
```

## 🎮 How to Use

### Making Coffee Orders
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0  
how many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

### Admin Commands
- **`report`** - Check current resources and profit
- **`off`** - Turn off the machine

### Sample Output
```
What would you like? (espresso/latte/cappuccino): report
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
```

## 📋 Menu & Specifications

| Drink | Water (ml) | Milk (ml) | Coffee (g) | Price |
|-------|------------|-----------|------------|-------|
| ☕ Espresso | 50 | - | 18 | $1.50 |
| 🥛 Latte | 200 | 150 | 24 | $2.50 |
| ☕ Cappuccino | 250 | 100 | 24 | $3.00 |

**Initial Resources:**
- 💧 Water: 300ml
- 🥛 Milk: 200ml  
- ☕ Coffee: 100g

## 🔧 Technical Implementation

### Key Features
- **Resource Management**: Tracks ingredient inventory
- **Payment Processing**: Handles coin input and change calculation
- **Error Handling**: Manages insufficient resources and payments
- **Modular Design**: Separated functions for different operations

### Code Structure
```python
# Main components:
- MENU: Dictionary containing drink recipes and pricing
- resources: Global state for ingredient tracking
- is_resource_sufficient(): Validates ingredient availability
- process_coins(): Handles payment input
- is_transaction_successful(): Processes payment logic
- make_coffee(): Updates resources and serves drink
```

## 🎓 Learning Objectives Demonstrated

This project showcases:
- ✅ **Functions & Parameters**: Modular code organization
- ✅ **Dictionaries & Data Structures**: Menu and resource management
- ✅ **Global Variables**: State management across functions
- ✅ **While Loops**: Main program flow control
- ✅ **Conditional Logic**: Decision-making processes
- ✅ **Input Validation**: User interaction handling
- ✅ **Mathematical Operations**: Payment calculations
- ✅ **Code Documentation**: Comprehensive commenting

## 🛠️ Prerequisites

- Python 3.6 or higher
- Basic understanding of command-line interfaces

## 📁 File Structure

```
coffee-machine-simulator/
│
├── main.py          # Main script file
└── README.md        # This documentation
```

## 🎨 Potential Enhancements

Future improvements could include:
- [ ] 🎨 GUI interface with tkinter
- [ ] 💾 Save/load machine state to file
- [ ] 📊 Sales analytics and reporting
- [ ] 🔄 Automatic resource restocking
- [ ] ☕ Custom drink creation
- [ ] 🧾 Receipt generation
- [ ] 🔊 Sound effects for actions

## 🐛 Troubleshooting

**Issue**: KeyError when entering invalid drink name
```
Solution: Enter exactly 'espresso', 'latte', or 'cappuccino'
```

**Issue**: Machine runs out of resources
```
Solution: Use 'report' command to check levels, restart script to reset
```

**Issue**: Payment calculation errors
```
Solution: Enter only whole numbers when prompted for coin quantities
```

## 🔗 Part of DevVault

This script is part of my **DevVault** collection - a comprehensive coding portfolio showcasing projects across multiple technologies. Check out the [main repository](https://github.com/qusai-Kagal/DevVault) for more projects!

## 📚 Course Context

**Angela Yu's 100 Days of Code - Day 15**
- Focus: Intermediate Python concepts
- Skills: Functions, dictionaries, program flow
- Challenge: Build a working simulation system

## 👨‍💻 Author

**Qusai Kagal**
- GitHub: [@qusai-Kagal](https://github.com/qusai-Kagal)
- Portfolio: [DevVault](https://github.com/qusai-Kagal/DevVault)

## 📄 License

This project is licensed under the MIT License - feel free to use and modify!

---

*Created with ☕ and Python. Part of the journey to becoming a better developer!*
