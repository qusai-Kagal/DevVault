# 🎬 Movie Recommender System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-purple.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 🚀 **A content-based movie recommendation system that suggests similar movies based on your preferences!**

## 📖 Overview

This project implements a **content-based movie recommendation system** using machine learning techniques. The system analyzes movie features like genres, keywords, cast, crew, and plot overview to recommend similar movies to users.

### ✨ Key Features

- 🎯 **Content-Based Filtering**: Recommends movies based on movie content similarity
- 🔍 **Multiple Feature Analysis**: Uses genres, keywords, cast, crew, and overview
- 🌐 **Interactive Web Interface**: Built with Streamlit for easy user interaction
- ⚡ **Fast Recommendations**: Pre-computed similarity matrix for instant results
- 📊 **5000+ Movies**: Comprehensive dataset from TMDB

## 🛠️ Technology Stack

- **Frontend**: ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
- **Backend**: ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
- **ML Libraries**: ![Scikit-learn](https://img.shields.io/badge/-Scikit%20Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
- **Data Processing**: ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white)
- **NLP**: ![NLTK](https://img.shields.io/badge/-NLTK-green?style=flat)

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/qusai-Kagalwala/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501` to use the application.

## 📁 Project Structure

```
movie-recommender-system/
│
├── 📄 app.py                    # Main Streamlit application
├── 📄 movie-recommender-system.ipynb  # Data preprocessing notebook
├── 📦 movies_dict.pkl           # Processed movie data
├── 📦 similarity.pkl            # Precomputed similarity matrix
├── 📄 requirements.txt          # Python dependencies
├── 📄 setup.sh                  # Heroku setup script
├── 📄 Procfile                  # Heroku deployment config
└── 📄 README.md                 # Project documentation
```

## 🔧 How It Works

### 1. **Data Processing Pipeline**
- 📥 **Data Loading**: Loads TMDB 5000 movies and credits datasets
- 🧹 **Data Cleaning**: Removes null values and duplicates
- 🔄 **Feature Extraction**: Extracts genres, keywords, cast, crew, and overview
- 📝 **Text Preprocessing**: Applies stemming and removes spaces for consistency

### 2. **Feature Engineering**
- 🎭 **Cast & Crew**: Extracts top 3 actors and director
- 🏷️ **Keywords & Genres**: Processes and cleans categorical data
- 📖 **Overview**: Splits plot summaries into individual words
- 🔗 **Tags Creation**: Combines all features into unified text tags

### 3. **Recommendation Algorithm**
- 🔢 **Vectorization**: Uses CountVectorizer (5000 features, English stop words removed)
- 📐 **Similarity Calculation**: Computes cosine similarity between movie vectors
- 🎯 **Recommendation**: Returns top 5 most similar movies based on content

### 4. **Mathematical Foundation**
```
Cosine Similarity = (A · B) / (||A|| × ||B||)
```
Where A and B are feature vectors of two movies.

## 🎮 Usage

1. **Select a Movie**: Choose from the dropdown menu containing 4800+ movies
2. **Get Recommendations**: Click the "Recommend" button
3. **View Results**: See 5 similar movies displayed instantly

### Example
```
Selected Movie: "Avatar"
Recommendations:
├── Guardians of the Galaxy
├── Star Trek Into Darkness
├── John Carter
├── Green Lantern
└── TRON: Legacy
```

## 🎨 Features

### Current Features
- ✅ Content-based movie recommendations
- ✅ Interactive web interface
- ✅ Fast similarity computation
- ✅ Comprehensive movie database

### Upcoming Features
- 🔄 **Collaborative Filtering**: User-based recommendations
- 🖼️ **Movie Posters**: Visual movie displays
- ⭐ **Ratings Integration**: IMDb/TMDB ratings
- 📱 **Mobile Responsive**: Better mobile experience
- 🔍 **Search Functionality**: Movie search capabilities

## 📊 Dataset Information

- **Source**: TMDB 5000 Movie Dataset
- **Movies**: 4,800+ unique movies
- **Features**: Genres, Keywords, Cast, Crew, Overview
- **Time Period**: Various release years
- **Data Size**: ~45MB processed

## 🚀 Deployment

### Local Deployment
```bash
streamlit run app.py
```

### Heroku Deployment
1. Create a Heroku app
2. Connect your GitHub repository
3. Deploy using the provided `Procfile` and `setup.sh`

### Docker Deployment (Coming Soon)
```dockerfile
# Dockerfile configuration coming soon
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Areas for Contribution
- 🎨 UI/UX improvements
- 🤖 Algorithm enhancements
- 📊 Additional datasets
- 🐛 Bug fixes
- 📚 Documentation

## 🔍 Performance Metrics

- **Response Time**: < 1 second for recommendations
- **Accuracy**: Content-based similarity matching
- **Scalability**: Handles 5000+ movies efficiently
- **Memory Usage**: ~200MB for similarity matrix

## 🎯 Future Enhancements

- [ ] **Hybrid Recommendation System** (Content + Collaborative)
- [ ] **Deep Learning Integration** (Neural Collaborative Filtering)
- [ ] **Real-time Updates** (Live TMDB API integration)
- [ ] **User Profiles** (Personalized recommendations)
- [ ] **Movie Reviews Analysis** (Sentiment-based filtering)
- [ ] **Multi-language Support** (International movies)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributors

- **Qusai Kagalwala** - *Initial work* - [qusai-Kagalwala](https://github.com/qusai-Kagalwala)

## 🙏 Acknowledgments

- 🎬 **TMDB** for providing the comprehensive movie dataset
- 🚀 **Streamlit** for the amazing web framework
- 🤖 **Scikit-learn** for machine learning tools
- 🐍 **Python Community** for incredible libraries

## 📧 Contact

- **Email**: qusai.kagalwala53@gmail.com
- **LinkedIn**: [Qusai Kagalwala](https://www.linkedin.com/in/qusai-kagalwala/)
- **GitHub**: [qusai-Kagalwala](https://github.com/qusai-Kagalwala)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ and 🐍 by [Qusai Kagalwala](https://github.com/qusai-Kagalwala)

</div>
