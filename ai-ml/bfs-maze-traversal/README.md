# 🧩 BFS Maze Traversal 🔍

## 📋 Overview

This project implements a **Breadth-First Search (BFS)** algorithm to find the shortest path through a maze. BFS is particularly useful for maze traversal as it guarantees finding the shortest path in unweighted graphs.

## 🌟 Features

- 🤖 Implements BFS algorithm for maze traversal
- 🗺️ Works with 2D grid-based mazes
- 🚀 Finds the shortest path from start to goal
- 📊 Visualizes the explored path
- ⏱️ Efficient implementation for quick solutions

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/qusai-Kagal/DevVault.git

# Navigate to the project directory
cd DevVault/ai-ml/bfs-maze-traversal

# Install dependencies (if any)
pip install -r requirements.txt
```

## 🚀 Usage

```python
# Import the BFS module
from bfs_maze import find_path

# Define your maze (0 = path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

# Set start and goal positions
start = (0, 0)
goal = (4, 4)

# Find the path
path = find_path(maze, start, goal)
print(path)
```

## 🧠 How It Works

1. 📍 Start at the initial position
2. 🔄 Explore all neighboring cells
3. 📝 Keep track of visited cells to avoid loops
4. 🔄 Use a queue to maintain the BFS traversal order
5. 🏁 Reconstruct the shortest path once the goal is reached

## 📊 Algorithm Complexity

- ⏱️ **Time Complexity**: O(V + E) where V is the number of vertices (cells) and E is the number of edges (connections between cells)
- 🗃️ **Space Complexity**: O(V) for storing the queue and visited set

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. 🍴 Fork the repository
2. 🔄 Create a new branch
3. 🛠️ Make your changes
4. 📤 Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

- 👨‍💻 Qusai Kagal
- 🔗 GitHub: [qusai-Kagal](https://github.com/qusai-Kagal)

## 🙏 Acknowledgments

- 📚 Inspired by classic pathfinding algorithms
- 🧩 Built as part of learning AI/ML fundamentals
