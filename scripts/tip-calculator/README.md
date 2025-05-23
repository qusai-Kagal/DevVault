# 💰 Tip Calculator

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Utility](https://img.shields.io/badge/Type-Utility%20Script-orange.svg)]()

> 🧾 **Quick and easy bill splitting with tip calculation!**

Never struggle with restaurant math again! This simple Python script calculates how much each person should pay when splitting a bill with tip. Perfect for dining out with friends, family meals, or any group expense.

## ✨ Features

### 🎯 Core Functionality
- 💵 **Bill Input**: Enter the total bill amount
- 📊 **Tip Calculation**: Choose from 10%, 12%, or 15% tip
- 👥 **Bill Splitting**: Divide equally among any number of people
- 🎯 **Precise Results**: Rounded to 2 decimal places
- ⚡ **Instant Calculation**: Get results immediately

### 🛠️ Technical Features
- 🐍 **Pure Python**: No external dependencies
- 🎨 **Clean Interface**: Simple command-line interaction
- 📱 **Lightweight**: Minimal resource usage
- ✅ **Accurate Math**: Proper rounding for currency

## 🚀 Quick Start

### Prerequisites
- 🐍 Python 3.6 or higher (uses only built-in libraries!)

### Installation & Running

1. **Clone the repository**
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/scripts/tip-calculator
   ```

2. **Run the calculator**
   ```bash
   python main.py
   ```

3. **Follow the prompts** and get your result! 🎉

## 🎮 How to Use

### 📋 Step-by-Step Guide

1. **Enter the total bill** (in dollars)
2. **Choose tip percentage** (10, 12, or 15)
3. **Enter number of people** splitting the bill
4. **Get your result** - amount each person pays!

### 💡 Example Usage

```
Welcome to the tip calculator!
What was the total bill? $85.50
What percentage tip would you like to give? 10, 12, or 15? 15
How many people to split the bill? 4
Each person should pay: $24.64
```

### 🧮 Calculation Breakdown

For the example above:
- **Original Bill**: $85.50
- **Tip (15%)**: $85.50 × 0.15 = $12.83
- **Total with Tip**: $85.50 + $12.83 = $98.33
- **Per Person**: $98.33 ÷ 4 = $24.64

## 📊 Usage Scenarios

### 🍽️ Restaurant Dining
```
Bill: $120.00, Tip: 15%, People: 6
Result: Each person pays $23.00
```

### ☕ Coffee Shop
```
Bill: $28.75, Tip: 12%, People: 3
Result: Each person pays $10.75
```

### 🍕 Pizza Night
```
Bill: $45.60, Tip: 10%, People: 5
Result: Each person pays $10.03
```

### 🎉 Group Celebration
```
Bill: $200.00, Tip: 15%, People: 8
Result: Each person pays $28.75
```

## 🔧 Code Explanation

### 📝 Main Components

```python
# User Input Collection
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculation Logic
tip_percent = tip / 100
total_with_tip = bill * (1 + tip_percent)
amount_per_person = total_with_tip / people

# Result Formatting
final_amount = round(amount_per_person, 2)
```

### 🧮 Mathematical Formula

```
Final Amount = (Bill × (1 + Tip%)) ÷ Number of People
```

Where:
- **Bill**: Original bill amount
- **Tip%**: Tip percentage (as decimal)
- **Number of People**: People splitting the bill

## 🚀 Enhancement Ideas

### 🎨 Potential Features
- 🔢 **Custom Tip Percentages**: Allow any tip percentage
- ✅ **Input Validation**: Handle invalid inputs gracefully
- 💱 **Currency Support**: Multiple currency formats
- 📊 **Detailed Breakdown**: Show tip amount separately
- 🎯 **Rounding Options**: Different rounding methods
- 💾 **Receipt Generation**: Save calculations to file
- 🖥️ **GUI Version**: Tkinter interface
- 📱 **Mobile App**: Cross-platform mobile version

### 🛠️ Code Improvements
```python
# Enhanced version features:
- Input validation and error handling
- Support for custom tip percentages
- Multiple currency formats
- Detailed calculation breakdown
- Command-line arguments support
```

## 🔧 Customization

### 💡 Easy Modifications

**Add more tip options:**
```python
tip = int(input("What percentage tip would you like to give? 10, 12, 15, 18, or 20? "))
```

**Custom tip percentage:**
```python
tip = float(input("What percentage tip would you like to give? "))
```

**Show detailed breakdown:**
```python
tip_amount = bill * tip_percent
print(f"Bill: ${bill:.2f}")
print(f"Tip ({tip}%): ${tip_amount:.2f}")
print(f"Total: ${total_with_tip:.2f}")
print(f"Each person pays: ${final_amount:.2f}")
```

## 🎯 Real-World Applications

### 🍽️ Dining & Entertainment
- Restaurant meals with friends
- Bar tabs and drinks
- Food delivery orders
- Coffee shop visits

### 🎉 Events & Gatherings
- Birthday dinner celebrations
- Office lunch meetings
- Group outings and activities
- Holiday party expenses

### 💼 Business Use
- Client dinner expenses
- Team building meals
- Conference dining
- Travel expense sharing

## 🤝 Contributing

Want to improve the Tip Calculator? Here's how:

1. 🍴 Fork the repository
2. 🌟 Create a feature branch (`git checkout -b feature/EnhancedFeature`)
3. 💾 Commit your changes (`git commit -m 'Add EnhancedFeature'`)
4. 📤 Push to branch (`git push origin feature/EnhancedFeature`)
5. 🔃 Open a Pull Request

### 💡 Contribution Ideas
- ✅ Input validation and error handling
- 🎨 GUI interface with tkinter
- 📱 Web version with Flask
- 💱 Multi-currency support
- 📊 Advanced calculation options
- 🧪 Unit tests
- 📖 Documentation improvements

## 🐛 Troubleshooting

### Common Issues

**❌ Invalid input errors?**
- Ensure you enter numbers only
- Use decimal point for cents (e.g., 25.50)
- Don't include currency symbols

**🔢 Unexpected results?**
- Check that tip percentage is 10, 12, or 15
- Verify number of people is greater than 0
- Ensure bill amount is positive

**💻 Python not found?**
- Install Python 3.6 or higher
- Check Python is in your system PATH
- Try `python3` instead of `python`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 About This Script

This tip calculator was created as a practical utility script to solve a common everyday problem. It demonstrates:
- 📊 **Basic mathematical operations**
- 💻 **User input handling**
- 🎯 **Number formatting and rounding**
- 🧮 **Real-world problem solving**

Perfect for Python beginners learning about user input, calculations, and formatting!

## 🙏 Acknowledgments

- 🍽️ Restaurant workers who inspired better tipping practices
- 🧮 Mathematics community for calculation accuracy
- 🐍 Python community for excellent built-in functions
- 💰 Everyone who's ever struggled with restaurant math

## 📬 Contact

**Qusai Kagal** - Practical Script Developer

- 💼 GitHub: [@qusai-Kagal](https://github.com/qusai-Kagal)

---

⭐ **Star this repo if it helped you split bills easier!** ⭐

*Made with 💰 and practical problem-solving!*
