# 🎭 Joke Generator

A simple yet delightful Express.js web application that fetches and displays random jokes using the JokeAPI. Features a clean, responsive UI with modern CSS styling and EJS templating.

## ✨ Features

- **Random Joke Fetching**: Pulls jokes from the comprehensive JokeAPI
- **Dual Joke Support**: Handles both single-line jokes and two-part setup/delivery jokes
- **Instant Refresh**: One-click button to load new jokes without page navigation
- **Content Filtering**: Automatically filters out NSFW, religious, political, racist, sexist, and explicit content
- **Responsive Design**: Mobile-friendly interface with gradient background
- **Error Handling**: Graceful error management for API failures

## 🛠️ Technologies Used

- **Backend**: Node.js with Express.js framework
- **Templating**: EJS (Embedded JavaScript)
- **HTTP Client**: Axios for API requests
- **Styling**: Custom CSS with modern gradients and animations
- **API**: JokeAPI v2 for joke content

## 📂 Project Structure

```
joke-generator/
├── public/
│   └── styles.css          # CSS styling for the web interface
├── views/
│   └── index.ejs           # EJS template for rendering jokes
├── index.js                # Main Express server file
├── package.json            # Project dependencies and scripts
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm (Node Package Manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/web-development/joke-generator
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the server**
   ```bash
   node index.js
   ```

4. **Open your browser**
   Navigate to `http://localhost:3000` to start enjoying jokes!

## 📦 Dependencies

```json
{
  "express": "^4.x.x",
  "axios": "^1.x.x",
  "ejs": "^3.x.x"
}
```

## 🎨 Features in Detail

### Joke Types Supported
- **Single Jokes**: One-liner jokes displayed directly
- **Two-Part Jokes**: Setup and delivery format with Q&A styling

### Content Safety
The application automatically excludes jokes with the following flags:
- NSFW content
- Religious content
- Political content
- Racist content
- Sexist content
- Explicit content

### UI/UX Features
- Modern gradient background (pink to peach)
- Clean white card design with subtle shadows
- Hover effects on buttons
- Responsive design for mobile devices
- Typography optimised for readability

## 🔧 Customisation

### Changing Joke Categories
Modify the API endpoint in `index.js`:
```javascript
const response = await axios.get("https://v2.jokeapi.dev/joke/Programming,Dark?blacklistFlags=nsfw");
```

### Styling Modifications
Update `public/styles.css` to change:
- Background gradients
- Card styling
- Button colours
- Typography

### Adding New Features
The modular structure makes it easy to extend:
- Add joke favouriting functionality
- Implement joke categories selection
- Add sharing capabilities

## 🌐 API Reference

This project uses the [JokeAPI v2](https://jokeapi.dev/):
- **Endpoint**: `https://v2.jokeapi.dev/joke/Any`
- **Parameters**: Blacklist flags for content filtering
- **Response**: JSON object with joke data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is part of the DevVault collection. Feel free to use and modify as needed.

## 🎯 Future Enhancements

- [ ] Add joke categories filter
- [ ] Implement favourite jokes storage
- [ ] Add social sharing buttons
- [ ] Create dark/light theme toggle
- [ ] Add joke rating system
- [ ] Implement user-submitted jokes

## 📞 Support

If you encounter any issues or have suggestions, please open an issue in the [DevVault repository](https://github.com/qusai-Kagal/DevVault/issues).

---

**Made with ❤️ using Express.js and JokeAPI**
