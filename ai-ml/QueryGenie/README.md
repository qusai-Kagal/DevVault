# QueryGenie 🧞‍♂️

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-orange) ![License](https://img.shields.io/github/license/qusai-Kagal/DevVault) ![AI](https://img.shields.io/badge/AI-Powered-green)

A simple AI-powered tool that converts natural language descriptions into SQL queries using local AI models. Built with Streamlit for an interactive web interface.

## 📚 Table of Contents

- [Features](#-features)
- [Built With](#️-built-with)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Demo](#-demo)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

## ✨ Features

- 🗣️ Convert natural language to SQL queries
- 🔍 Automatic database schema detection
- ✨ Clean SQL output without explanations
- 💻 Local AI processing using Ollama
- 🌐 Interactive web interface

## 🛠️ Built With

- **Python** - Core programming language
- **Streamlit** - Web interface
- **Ollama** - Local AI model serving
- **DeepSeek-R1** - Language model for SQL generation
- **SQLAlchemy** - Database toolkit
- **LangChain** - AI application framework

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) installed

### ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/qusai-Kagal/DevVault.git
cd DevVault/ai-ml/QueryGenie
```

2. Install dependencies
```bash
pip install streamlit langchain-ollama sqlalchemy
```

3. Install and setup Ollama model
```bash
ollama pull deepseek-r1:8b
```

## 🎯 Usage

1. Start the application
```bash
streamlit run text-to-sql.py
```

2. Open your browser to `http://localhost:8501`

3. Enter your data request in natural language (e.g., "Show all users older than 25")

4. Copy the generated SQL query

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is part of the DevVault collection. For licensing information, please see the [DevVault License](https://github.com/qusai-Kagal/DevVault/blob/main/LICENSE).

## 🙏 Acknowledgements

- [Ollama](https://ollama.ai) - Local AI model infrastructure
- [DeepSeek](https://deepseek.com) - R1 language model
- [Streamlit](https://streamlit.io) - Web application framework
- [LangChain](https://langchain.com) - AI application development
