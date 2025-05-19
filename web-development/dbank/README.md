# DBank - Decentralized Banking Application

**Part of [DevVault](https://github.com/qusai-Kagal/DevVault) - Web Development Portfolio**

A modern decentralized banking application built on the Internet Computer blockchain, featuring secure deposits, withdrawals, and compound interest calculations.

## 🎯 Project Overview

DBank is a full-stack decentralized application (dApp) that demonstrates the power of blockchain technology in creating trustless financial services. Built with React.js frontend and Motoko smart contracts on the Internet Computer.

## ✨ Features

- 💰 **Secure Deposits**: Add funds to your decentralized account
- 💸 **Safe Withdrawals**: Withdraw funds with automatic balance validation
- 📈 **Compound Interest**: Automatic interest calculation and application
- 📊 **Real-time Balance**: Live account balance tracking
- 🔐 **Trustless Security**: No central authority required
- 🌍 **Global Access**: Available anywhere with internet connection

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | React.js, CSS3, HTML5 |
| **Backend** | Motoko (Internet Computer) |
| **Blockchain** | Internet Computer Protocol (ICP) |
| **Build Tool** | Webpack |
| **Development** | DFX (DFINITY SDK) |
| **Package Manager** | NPM |

## 🚀 Quick Start

### Prerequisites
```bash
# Install Node.js (v14+)
# Install DFX SDK
sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"
```

### Installation & Setup
```bash
# 1. Navigate to project directory
cd web-development/dbank

# 2. Install dependencies
npm install

# 3. Start local Internet Computer replica
dfx start --clean

# 4. Deploy canisters (in new terminal)
dfx deploy

# 5. Start development server
npm start
```

🌐 **Application will be available at:** `http://localhost:3000`

## 📂 Project Structure

```
dbank/
├── src/
│   ├── dbank/              # Backend (Motoko)
│   │   └── main.mo         # Smart contract logic
│   └── dbank_assets/       # Frontend (React)
│       ├── src/
│       │   ├── index.js    # Main React component
│       │   ├── index.html  # HTML template
│       │   └── index.css   # Styling
│       └── assets/         # Static files
├── .dfx/                   # DFX build files
├── dfx.json               # Project configuration
├── package.json           # NPM configuration
├── webpack.config.js      # Build configuration
└── README.md             # This file
```

## 🎮 How to Use

### 1. **Check Balance**
- View your current account balance on page load
- Balance updates in real-time

### 2. **Make a Deposit**
- Enter deposit amount in the input field
- Click "Submit" to add funds to your account
- Transaction is processed immediately

### 3. **Withdraw Funds**
- Enter withdrawal amount
- Click "Withdraw" (only works if sufficient balance)
- Automatic balance validation prevents overdrafts

### 4. **Apply Interest**
- Click "Finalise Interest" to calculate and apply compound interest
- Interest is calculated based on time elapsed since last compound

## 🔧 Smart Contract Functions

```motoko
// Check current balance
public query func checkBalance() : async Float

// Add funds to account
public func topUp(amount: Float) : async Float

// Remove funds from account  
public func withdraw(amount: Float) : async Result.Result<Float, Text>

// Calculate and apply compound interest
public func compound() : async ()
```

## 🔐 Security Features

- **Overflow Protection**: Prevents arithmetic overflow in calculations
- **Balance Validation**: Automatic checks prevent negative balances
- **Immutable Records**: All transactions stored on blockchain
- **No Central Control**: Fully decentralized operation

## 🧪 Development Commands

```bash
# Start local replica (clean state)
dfx start --clean

# Deploy to local network
dfx deploy

# Deploy to IC mainnet
dfx deploy --network ic

# Reset local state
dfx stop && dfx start --clean

# Check canister status
dfx canister status dbank
```

## 🔍 Testing

```bash
# Run local tests
dfx test

# Interact with deployed canister
dfx canister call dbank checkBalance
dfx canister call dbank topUp '(100.0)'
dfx canister call dbank withdraw '(50.0)'
```

## 📚 Learning Outcomes

This project demonstrates:
- Internet Computer blockchain development
- Motoko smart contract programming
- React.js frontend integration
- DFX development workflow
- Decentralized application architecture
- Web3 user experience design

## 🐛 Known Issues

- Interest calculation resets on canister upgrade
- Frontend may need refresh after deployment
- Local development requires stable internet connection

## 🔗 Related Projects

Explore more projects in [DevVault](https://github.com/qusai-Kagal/DevVault):
- [Web Development](../README.md)
- [Full Portfolio](../../README.md)

## 📜 License

This project is part of DevVault and is licensed under the MIT License.

## 👤 Developer

**Qusai Kagal**
- GitHub: [@qusai-Kagal](https://github.com/qusai-Kagal)
- DevVault: [Portfolio](https://github.com/qusai-Kagal/DevVault)

---

💡 **Tip**: This project is great for learning Web3 development! Check out the [Internet Computer documentation](https://internetcomputer.org/docs/) for more advanced features.

*Built with ❤️ as part of the DevVault learning journey*
