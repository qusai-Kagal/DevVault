# 🥁 Drum Kit

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

An interactive web-based drum kit that brings the joy of drumming to your browser. Play realistic drum sounds using keyboard keys or mouse clicks with smooth animations and instant audio feedback.

## 🌟 Features

- **🎵 7 Drum Sounds**: Tom drums, snare, crash cymbal, and kick bass
- **⌨️ Dual Input Methods**: Play with keyboard keys or mouse clicks
- **✨ Visual Feedback**: Smooth animations when drums are triggered
- **🎨 Modern UI**: Clean design with custom drum images and typography
- **📱 Responsive Design**: Works seamlessly across devices
- **🔊 Real-time Audio**: Instant sound playback with HTML5 Audio API

## 🎮 How to Play

### Keyboard Controls
| Key | Drum Sound | Visual |
|-----|------------|--------|
| **W** | Tom 1 | 🥁 |
| **A** | Tom 2 | 🥁 |
| **S** | Tom 3 | 🥁 |
| **D** | Tom 4 | 🥁 |
| **J** | Snare | 🥁 |
| **K** | Crash Cymbal | 🥁 |
| **L** | Kick Bass | 🥁 |

### Mouse Controls
Simply click any drum button to play the corresponding sound!

## 🚀 Quick Start

### Option 1: Direct Download
1. **Download** or **clone** this repository
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/web-development/drum-kit
   ```

2. **Open in browser**
   ```bash
   # Simply double-click index.html
   # OR open with your preferred browser
   open index.html
   ```

### Option 2: Local Server (Recommended)
```bash
# Using Python 3
python -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

Then visit `http://localhost:8000`

## 📁 Project Structure

```
drum-kit/
├── 📄 index.html          # Main HTML structure
├── 🎨 styles.css          # Styling & animations
├── ⚡ index.js            # JavaScript functionality
├── 📂 images/             # Drum visual assets
│   ├── tom1.png          # Tom drum 1 image
│   ├── tom2.png          # Tom drum 2 image
│   ├── tom3.png          # Tom drum 3 image
│   ├── tom4.png          # Tom drum 4 image
│   ├── snare.png         # Snare drum image
│   ├── crash.png         # Crash cymbal image
│   └── kick.png          # Kick drum image
├── 📂 sounds/             # Audio files
│   ├── tom-1.mp3         # Tom drum 1 sound
│   ├── tom-2.mp3         # Tom drum 2 sound
│   ├── tom-3.mp3         # Tom drum 3 sound
│   ├── tom-4.mp3         # Tom drum 4 sound
│   ├── snare.mp3         # Snare drum sound
│   ├── crash.mp3         # Crash cymbal sound
│   └── kick-bass.mp3     # Kick bass sound
└── 📖 README.md           # Project documentation
```

## 🛠️ Technologies Used

### Frontend
- **HTML5**: Semantic structure and audio elements
- **CSS3**: Modern styling, animations, and responsive design
- **JavaScript (ES6)**: Interactive functionality and event handling

### External Resources
- **Google Fonts**: Arvo font family for typography
- **Audio API**: HTML5 Audio for sound playback

## 🧠 Learning Concepts

This project demonstrates essential web development skills:

### JavaScript Concepts
- **Event Listeners**: `addEventListener()` for keyboard and click events
- **DOM Manipulation**: `querySelector()` and `classList` methods
- **Audio API**: Creating and playing audio dynamically
- **Switch Statements**: Clean conditional logic for key mapping
- **Functions**: Modular code with `makeSound()` and `buttonAnimation()`

### CSS Concepts  
- **Background Images**: Custom drum visuals for each button
- **CSS Animations**: `.pressed` class for visual feedback
- **Flexbox/Grid**: Responsive layout techniques
- **Custom Properties**: Consistent color scheme
- **Typography**: Google Fonts integration

### HTML Concepts
- **Semantic Elements**: Proper document structure
- **Event Attributes**: Button interactions
- **External Resources**: Linking stylesheets and scripts

## 🎨 Design Features

- **Color Palette**: Dark theme with blue (#283149) and pink (#DA0463) accents
- **Typography**: Arvo font family for retro drum machine aesthetic
- **Animations**: Smooth opacity and shadow transitions
- **Visual Feedback**: Immediate response to user interactions
- **Accessibility**: High contrast and clear visual hierarchy

## 🔧 Customization

### Adding New Sounds
1. Add your audio file to the `sounds/` directory
2. Add corresponding image to `images/` directory
3. Update the JavaScript switch statement:
   ```javascript
   case "newkey":
     var newSound = new Audio('sounds/newsound.mp3');
     newSound.play();
     break;
   ```
4. Add CSS styling for the new button

### Modifying Styles
- **Colors**: Update the CSS custom properties
- **Animations**: Modify the `.pressed` class timing and effects
- **Layout**: Adjust button sizes and spacing in `.drum` class

## 🌐 Browser Support

- ✅ Chrome 60+
- ✅ Firefox 55+  
- ✅ Safari 11+
- ✅ Edge 79+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

Contributions make the open source community amazing! Any contributions you make are **greatly appreciated**.

### How to Contribute
1. **Fork** the Project
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contributions
- 🎵 Add more drum sounds (hi-hat, ride cymbal, etc.)
- 🎹 Implement recording and playback functionality
- 🎛️ Add volume controls for individual drums
- 📱 Improve mobile touch experience
- 🎨 Create different drum kit themes
- 📊 Add visual sound wave animations
- ⚡ Implement keyboard shortcuts for drum patterns

## 📜 License

Distributed under the MIT License. See `LICENSE` file for more information.

## 👨‍💻 Author

**Qusai Kagalwala**
- GitHub: [@qusai-Kagal](https://github.com/qusai-Kagal)

## 🙏 Acknowledgments

- **Audio Samples**: [Credit your audio sources if applicable]
- **Design Inspiration**: Classic drum machine interfaces
- **Learning Resources**: Web development community tutorials
- **Font**: Google Fonts - Arvo family

## 🔗 Related Projects

Explore more projects in the [DevVault Repository](https://github.com/qusai-Kagal/DevVault):
- 🌐 Web Development Projects
- ⚡ JavaScript Applications
- 🎮 Interactive Games
- 🎨 UI/UX Experiments

---

<div align="center">

**Made with ❤️ and lots of ☕**

⭐ **Star this repo if you found it helpful!** ⭐

[Report Bug](https://github.com/qusai-Kagal/DevVault/issues) · [Request Feature](https://github.com/qusai-Kagal/DevVault/issues) · [View Demo](https://qusai-kagal.github.io/DevVault/web-development/drum-kit/)

</div>
