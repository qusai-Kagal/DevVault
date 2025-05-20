# Repo Vista

<p align="center">
  <br>
  <em>Create beautiful social preview images for your GitHub repositories</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB" alt="React"/>
  <img src="https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
  <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge" alt="License"/>
</p>

## 📖 Overview

Repo Vista is a modern React application that helps developers craft eye-catching social preview images for their GitHub repositories. These images showcase repository statistics, language breakdown, avatars, and more - making your projects stand out in GitHub feeds and social media shares.

## ✨ Features

- **GitHub API Integration**: Fetches real repository data including stars, forks, and language statistics
- **User Avatar Support**: Displays repository owner's avatar in the preview
- **Enhanced UI**: Beautiful, modern interface with customizable elements
- **Multiple Themes**: Choose from 7 different color themes:
  - 🌑 Dark: Dark blue gradient background
  - ☀️ Light: Clean white background
  - 🌈 Gradient: Purple to blue gradient
  - 🐙 GitHub: GitHub's dark theme
  - 🌅 Sunset: Warm orange to yellow gradient
  - 🌊 Ocean: Calming blue gradient
  - 🌲 Forest: Soothing green gradient
- **Background Patterns**: Add stylish patterns to your preview
- **Customizable Language Breakdown**: Edit your repository's language distribution
- **Download & Copy**: Export your preview as a PNG image or copy to clipboard
- **Responsive Design**: Works seamlessly on all devices

## 🚀 Getting Started

### Prerequisites

- Node.js (v14.0.0 or higher)
- npm (v6.0.0 or higher)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/qusai-Kagalwala/repo-vista.git
cd repo-vista
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The application will open in your browser at `http://localhost:3000`.

## 📋 Usage

### Using GitHub API

1. Enter a GitHub repository URL (e.g., https://github.com/username/repository)
2. Click "Fetch" to automatically load repository data from GitHub
3. The preview will update with real repository data and language breakdown

### Manual Customization

1. Edit repository details (name, description, stars, forks)
2. Customize language breakdown by adding, removing, or adjusting percentages
3. Choose your preferred theme and background pattern
4. Download the preview image or copy it to clipboard

### Setting Your GitHub Social Preview

1. Download your generated image
2. Go to your GitHub repository
3. Click on "Settings"
4. Scroll down to the "Social Preview" section
5. Click "Edit"
6. Upload your downloaded image
7. Click "Save changes"

## 🏗️ Project Structure

```
repo-vista/
│
├── public/
│   ├── index.html
│   ├── favicon.ico
│   └── manifest.json
│
├── src/
│   ├── components/
│   │   ├── GitHubPreviewGenerator.jsx   # Main component
│   │   ├── LanguageBar.jsx              # Language breakdown bar
│   │   ├── PreviewCard.jsx              # Preview display
│   │   └── ThemeSelector.jsx            # Theme selection
│   │
│   ├── styles/
│   │   ├── main.css                     # Main CSS styles
│   │   ├── themes.css                   # Theme-specific styles
│   │   └── languages.css                # Language color definitions
│   │
│   ├── utils/
│   │   ├── helpers.js                   # Helper functions
│   │   └── github-api.js                # GitHub API integration
│   │
│   ├── App.jsx
│   ├── index.jsx
│   └── index.css
│
├── package.json
└── README.md
```

## 🔌 GitHub API Integration

This project uses the GitHub REST API to fetch repository data:

- Repository information: `https://api.github.com/repos/{username}/{repository}`
- Language statistics: `https://api.github.com/repos/{username}/{repository}/languages`
- User avatar: `https://api.github.com/users/{username}`

Note: The GitHub API has rate limits for unauthenticated requests (60 requests per hour). For higher limits, consider implementing GitHub OAuth authentication.

## 🛠️ Technologies Used

- **React**: UI framework for building interactive interfaces
- **Bootstrap**: CSS framework for responsive layout and components
- **HTML2Canvas**: Library for generating downloadable images
- **Lucide React**: For SVG icons and visual elements
- **GitHub API**: For fetching real-time repository data

## 🎨 Customization Options

### Themes

Choose from 7 beautiful themes to make your preview stand out:

- **Dark**: Dark blue gradient background
- **Light**: Clean white background
- **Gradient**: Purple to blue gradient
- **GitHub**: GitHub's dark theme
- **Sunset**: Warm orange to yellow gradient
- **Ocean**: Calming blue gradient
- **Forest**: Soothing green gradient

### Background Patterns

Add extra style with various patterns:

- **None**: Solid background
- **Dots**: Dotted pattern
- **Lines**: Diagonal lines
- **Hexagons**: Hexagonal pattern
- **Circuit**: Circuit board pattern

## ⚡ Performance Optimization

Repo Vista is optimized for performance in several ways:

- **Lazy Loading**: Components are loaded only when needed
- **Memoization**: Prevents unnecessary re-renders
- **Image Optimization**: Preview images are compressed without quality loss
- **API Caching**: Repository data is cached to minimize API calls

## 🔍 Troubleshooting

### Common Issues

1. **API Rate Limiting**: If you encounter GitHub API rate limits, try implementing OAuth authentication.
2. **Image Generation Failed**: Make sure all custom elements (especially images) are properly loaded before generating.
3. **Custom Fonts Not Loading**: Ensure you have an internet connection as fonts are loaded from Google Fonts.

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Report bugs or request features by opening an issue
2. Improve documentation
3. Fix bugs or add features by submitting a pull request

### Development Guidelines

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🛣️ Roadmap

- **Authentication**: GitHub OAuth integration
- **Custom Fonts**: Support for custom typography
- **Template Gallery**: Pre-designed templates
- **Dark/Light Mode**: UI theme switching
- **Export Options**: Additional export formats (JPG, SVG)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [Socialify](https://socialify.git.ci/)
- GitHub for their API
- The open-source community

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/qusai-Kagalwala">Qusai Kagalwala</a>
</p>
