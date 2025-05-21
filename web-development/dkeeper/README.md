# 📝 DKeeper

DKeeper is a decentralized note-taking application built on the Internet Computer platform. It functions similar to Google Keep but operates on a decentralized blockchain infrastructure, providing enhanced privacy, data ownership, and security. This app allows you to create, organize, and manage your notes with data stored on the Internet Computer blockchain rather than traditional centralized servers.

## ✨ Features

- 📌 Create, read, update, and delete notes
- 💾 Store notes securely on the Internet Computer blockchain 
- 🔄 Persistent storage with blockchain technology
- 🔒 Decentralized architecture for enhanced privacy and security
- 📱 Responsive web interface built with React.js
- 🧩 Backend canister written in Motoko
- 🌐 No central servers or databases - truly decentralized

## 📸 Screenshot

![DKeeper App Screenshot](src/dkeeper_frontend/assets/screenshot.png)
*Note: Add an actual screenshot of your application by saving it to this path or update the path accordingly*

## 🛠️ Technology Stack

- 🖥️ **Frontend**: React.js
- 🔧 **Backend**: Internet Computer/Motoko
- 🧪 **Development Environment**: DFINITY SDK (dfx)
- 🔗 **Blockchain**: Internet Computer Protocol (ICP)

## 🔍 How It Works

DKeeper leverages the Internet Computer blockchain to create a truly decentralized note-taking experience:

1. 📋 **Notes Creation**: Create notes with titles and content through the React frontend
2. 📡 **Blockchain Storage**: Notes are stored on the Internet Computer blockchain via Motoko canisters
3. 🔐 **Decentralized Data**: Your notes exist on the blockchain, not on centralized servers
4. 🔄 **CRUD Operations**: Full support for creating, reading, updating, and deleting notes
5. 🌐 **Global Accessibility**: Access your notes from anywhere with an internet connection

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- 📦 [Node.js](https://nodejs.org/) (v12 or later)
- 🚀 [DFINITY Canister SDK](https://sdk.dfinity.org/docs/quickstart/local-quickstart.html)
- 🔄 [Git](https://git-scm.com/downloads)

## 🚀 Getting Started

### 📥 Clone the Repository

```bash
git clone https://github.com/qusai-Kagal/DevVault.git
cd DevVault/web-development/dkeeper
```

### 📦 Install Dependencies

```bash
npm install
```

### 🏃‍♂️ Run the Development Environment

1. Start the local Internet Computer replica:
```bash
dfx start --clean
```

2. In a new terminal window, deploy the canisters:
```bash
dfx deploy
```

3. Start the frontend development server:
```bash
npm start
```

4. Open your browser and navigate to:
```
http://localhost:8080/
```

### 🧪 Testing the Application

After the application is running, you can:
- Create new notes by filling out the title and content fields
- View all your created notes
- Delete notes by clicking the delete button

## 🌐 Deployment

To deploy to the Internet Computer mainnet:

1. Make sure you have cycles available in your wallet 💰

2. Deploy using:
```bash
dfx deploy --network ic
```

3. After deployment, you'll receive a canister URL that can be accessed from anywhere in the world 🌎

## 📁 Project Structure

```
DevVault/
└── web-development/
    └── dkeeper/
        ├── dist/
        │   └── dkeeper_assets/  # 📦 Built assets
        ├── src/                 # 💻 Source code
        │   ├── declarations/    # 📝 Type declarations for the canisters
        │   ├── dkeeper/         # 🧠 Main application code
        │   └── dkeeper_assets/  # 🖼️ Static assets for the application
        ├── dfx.json             # ⚙️ DFINITY project configuration
        ├── package.json         # 📦 Node.js dependencies
        ├── package-lock.json    # 🔒 Locked dependencies
        ├── tsconfig.json        # ⚙️ TypeScript configuration
        ├── webpack.config.js    # 🔧 Webpack bundler configuration
        └── README.md            # 📝 This file
```

## 🧠 Understanding the Code

### Backend (Motoko)

The backend is written in Motoko, a programming language designed for the Internet Computer. The main files contain:

- Note data structure definition
- Functions to create, read, and delete notes
- Persistent storage using stable variables

### Frontend (React)

The frontend is built with React and includes:

- Components for displaying and creating notes
- Integration with the Internet Computer backend
- Responsive design for various screen sizes

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project 🍴
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 🎉

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgments

- 💡 Inspired by Google Keep
- 🚀 Built with the Internet Computer platform
- 🙏 Thanks to the DFINITY Foundation for their developer tools and documentation
- 📚 Based on learning resources from Web3 development courses

## 📫 Contact

Qusai Kagal - [GitHub Profile](https://github.com/qusai-Kagal)

Project Link: [https://github.com/qusai-Kagal/DevVault/tree/main/web-development/dkeeper](https://github.com/qusai-Kagal/DevVault/tree/main/web-development/dkeeper)
