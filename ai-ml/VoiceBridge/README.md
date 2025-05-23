# 🎙️ VoiceBridge

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 🌍 **Break language barriers with real-time voice translation!**

VoiceBridge is a powerful live language translator that listens to your speech, detects the language automatically, and provides instant translations with natural-sounding speech output. Perfect for conversations, meetings, travel, and learning new languages.

## ✨ Features

### 🎯 Core Functionality
- 🎤 **Real-time Speech Recognition** - Capture voice input with adjustable sensitivity
- 🔍 **Automatic Language Detection** - Identifies 100+ languages automatically
- 🌐 **Instant Translation** - Powered by Google Translate API
- 🔊 **Natural Text-to-Speech** - High-quality voice output in target language
- 📱 **User-Friendly GUI** - Clean, intuitive Tkinter interface

### ⚙️ Advanced Settings
- ⏱️ **Customizable Timeouts** - Adjust listening duration (1-15 seconds)
- 🎛️ **Phrase Time Limits** - Control speech capture length
- 🔄 **Auto-Translation** - Automatic speech output toggle
- 🧹 **Session Management** - Clear conversations with one click

### 🌍 Language Support
Supports **100+ languages** including:
- 🇺🇸 English • 🇪🇸 Spanish • 🇫🇷 French • 🇩🇪 German • 🇮🇹 Italian
- 🇯🇵 Japanese • 🇰🇷 Korean • 🇨🇳 Chinese • 🇷🇺 Russian • 🇦🇷 Arabic
- 🇮🇳 Hindi • 🇵🇹 Portuguese • 🇳🇱 Dutch • 🇸🇪 Swedish • And many more!

## 🚀 Quick Start

### Prerequisites
- 🐍 Python 3.7 or higher
- 🎤 Working microphone
- 🔊 Audio output (speakers/headphones)
- 🌐 Internet connection

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/ai-ml/VoiceBridge
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python live_lang_translator.py
   ```

## 📦 Dependencies

```
speech_recognition>=3.10.0
pyttsx3>=2.90
langdetect>=1.0.9
deep-translator>=1.11.4
gtts>=2.3.1
pygame>=2.1.0
requests>=2.28.0
```

## 🎮 How to Use

### 🔧 Setup
1. **Select Target Language** - Choose your desired translation language from the dropdown
2. **Adjust Settings** - Set listening timeout and phrase limits as needed
3. **Test Audio** - Use "Test Speech" to verify your audio setup

### 🎙️ Translation Process
1. **Start Listening** - Click "Start Listening" button
2. **Speak Clearly** - Talk into your microphone in any supported language
3. **View Results** - See original text and translation in real-time
4. **Listen to Translation** - Auto-speech or manual playback available

### ⚡ Pro Tips
- 🎯 Speak clearly and at moderate pace for best recognition
- 🔇 Minimize background noise for accurate detection
- 📏 Keep phrases under 5 seconds for optimal performance
- 🔄 Use auto-speak for seamless conversations

## 🛠️ Technical Details

### Architecture
- **Speech Recognition**: Google Speech-to-Text API
- **Language Detection**: langdetect library with statistical analysis
- **Translation Engine**: Google Translate via deep-translator
- **Text-to-Speech**: Google TTS (gTTS) with pygame audio playback
- **GUI Framework**: Tkinter with modern styling

### Key Components
```python
🎤 SpeechRecognizer    # Audio capture and processing
🔍 LanguageDetector    # Automatic language identification  
🌐 Translator         # Real-time translation engine
🔊 TTSEngine          # Natural voice synthesis
📱 GUI               # User interface and controls
```

## 🤝 Contributing

Contributions welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌟 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

### 💡 Ideas for Contributions
- 🎨 UI/UX improvements
- 🌍 Additional language support
- 🔧 Performance optimizations
- 📱 Mobile app version
- 🔌 API integrations

## 🐛 Troubleshooting

### Common Issues

**🎤 Microphone not working?**
- Check system permissions for microphone access
- Verify default audio input device
- Test with other voice applications

**🌐 Translation errors?**
- Ensure stable internet connection
- Check Google Translate service status
- Try shorter phrases

**🔊 No audio output?**
- Verify speaker/headphone connections
- Check system audio settings
- Test with "Test Speech" button

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🎯 Google for Speech Recognition and Translation APIs
- 🔊 gTTS team for text-to-speech capabilities
- 🐍 Python community for amazing libraries
- 🌟 Open source contributors

## 📬 Contact

**Qusai Kagal** - Passionate Developer & Tech Enthusiast

- 💼 GitHub: [@qusai-Kagal](https://github.com/qusai-Kagal)

---

⭐ **Star this repo if VoiceBridge helped you break language barriers!** ⭐

*Made with ❤️ and lots of ☕*
