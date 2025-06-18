# 🗺️ Interactive Geography Games

An educational collection of interactive geography learning games built with Python's Turtle Graphics and Pandas. Learn US states, Indian states & union territories, and analyse real-world data through engaging, map-based quizzes.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.0+-green.svg)
![Turtle](https://img.shields.io/badge/Turtle-Graphics-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Features

### 🇺🇸 US States Game
- Interactive map-based learning of all 50 US states
- Real-time progress tracking (X/50 states correct)
- Visual feedback with state names appearing on correct guesses
- Personalised study materials generation for missed states
- Clean exit mechanism with progress saving

### 🇮🇳 India States & Union Territories Game  
- Learn all 28 states and 8 union territories of India
- Coordinate-based positioning system
- Progress tracking and study aid generation
- Interactive GUI with turtle graphics

### 📊 Data Analysis Tools
- **Central Park Squirrel Census Analysis**: Real-world data analysis of 2018 squirrel population by fur colour
- **Coordinate Mapper**: Interactive tool for creating custom geography games
- **CSV Processing**: Robust data handling with Pandas

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas turtle
```

### Running the Games

#### US States Game
```bash
cd 01-course-version
python main.py
```

#### India States Game  
```bash
cd 02-personal-version
python main.py
```

#### Data Analysis
```bash
cd csv_data_analysis
python main.py
```

## 📁 Project Structure

```
interactive-geography-games/
├── 01-course-version/          # US States Game
│   ├── main.py                 # Main game logic
│   ├── 50_states.csv          # US states coordinates
│   ├── blank_states_img.gif   # US map background
│   └── states_to_learn.csv    # Generated study materials
├── 02-personal-version/        # India States Game
│   ├── main.py                 # India game logic
│   ├── 28_states_8_u.t.csv    # Indian states/UTs coordinates  
│   ├── blank_states_img.gif   # India map background
│   ├── co-ordinate.py         # Coordinate mapping tool
│   ├── clicked_coordinates.csv # Coordinate data
│   └── states_to_learn.csv    # Study materials
└── csv_data_analysis/          # Data analysis projects
    ├── main.py                 # Squirrel census analysis
    ├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
    ├── weather_data.csv        # Sample weather data
    ├── squirrel_count.csv      # Analysis results
    └── new_data.csv           # Sample export data
```

## 🎮 How to Play

### US States Game
1. **Start**: Run `main.py` to launch the game
2. **Guess**: Type state names in the input dialog
3. **Visual Feedback**: Correct guesses appear on the map
4. **Progress**: Track your score (X/50 states)
5. **Exit**: Type "Exit" to save study materials
6. **Study**: Review `states_to_learn.csv` for missed states

### India States Game
1. **Launch**: Run the India version main.py
2. **Input**: Enter state or union territory names
3. **Learning**: Names appear at correct map locations
4. **Progress**: Monitor your learning progress
5. **Study Aid**: Generate personalised study materials

### Coordinate Mapper Tool
```bash
python co-ordinate.py
```
- **Click**: Mouse clicks to capture coordinates
- **Save**: Press 's' to export coordinates to CSV
- **Clear**: Press 'c' to reset and start over
- **Create**: Build custom geography games

## 📊 Data Analysis Features

### Central Park Squirrel Census
Analyses real 2018 data from NYC's Central Park:
- **Grey Squirrels**: 2,473 observed
- **Cinnamon Squirrels**: 392 observed  
- **Black Squirrels**: 103 observed

### Weather Data Processing
Demonstrates various CSV handling techniques:
- Built-in `open()` function
- CSV module usage
- Pandas DataFrame operations
- Data filtering and statistics

## 🛠️ Technical Implementation

### Key Technologies
- **Python Turtle**: Interactive graphics and user input
- **Pandas**: CSV data manipulation and analysis
- **Event Handling**: Mouse clicks and keyboard shortcuts
- **Data Export**: CSV generation for study materials

### Core Concepts Demonstrated
- **DataFrame Operations**: Filtering, indexing, aggregation
- **Interactive GUI**: `textinput()` dialogs and event binding
- **Coordinate Systems**: Map-based positioning
- **File I/O**: CSV reading/writing with error handling
- **Game Logic**: State management and progress tracking

## 📈 Learning Outcomes

### Data Science Skills
- CSV data loading and manipulation with Pandas
- Boolean indexing and data filtering
- Statistical analysis and aggregation
- Data export and visualization

### Programming Concepts  
- Event-driven programming
- Interactive application development
- File handling and data persistence
- User interface design with Turtle Graphics

### Geography Knowledge
- US state locations and names
- Indian states and union territories
- Coordinate-based geographical positioning
- Interactive learning methodology

## 🎯 Game Statistics

### US States Game Performance
Example study materials generated:
- Alabama, Arizona, Arkansas, Colorado, Connecticut
- Delaware, Florida, Georgia, Idaho, Illinois
- And 30+ more states for focused learning

### India Game Progress
Sample missed states for review:
- Uttarakhand, Haryana, Uttar Pradesh
- Chhattisgarh, Odisha, Telangana
- Personalised based on your performance

## 🔧 Customisation

### Adding New Maps
1. **Image**: Add your map as a GIF file
2. **Coordinates**: Use `co-ordinate.py` to map locations
3. **Data**: Create CSV with state names and coordinates
4. **Code**: Modify main.py to load your data

### Custom Study Materials
The games automatically generate `states_to_learn.csv` files containing:
- States you haven't guessed yet
- Personalised study lists
- Progress tracking data

## 🤝 Contributing

Contributions welcome! Areas for enhancement:
- Additional countries/regions
- Difficulty levels and timing challenges
- Enhanced graphics and animations
- Mobile-friendly versions
- Multiplayer functionality

## 📚 Educational Use

Perfect for:
- **Geography Teachers**: Interactive classroom tools
- **Students**: Self-paced learning and assessment  
- **Homeschooling**: Engaging educational activities
- **Data Science Learning**: Real-world Pandas applications

## 🏆 Achievements Unlocked

- ✅ Interactive map-based learning
- ✅ Real-time progress tracking  
- ✅ Personalised study material generation
- ✅ Multiple country support
- ✅ Data analysis integration
- ✅ Custom game creation tools

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Angela Yu's 100 Days of Code**: Original course inspiration
- **Central Park Conservancy**: Squirrel census data
- **Python Community**: Turtle Graphics and Pandas libraries
- **Educational Technology**: Interactive learning principles

---

**Happy Learning! 🎓🗺️**

*Built with ❤️ for geography education and Python learning*
