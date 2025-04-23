```markdown
# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python, Pandas, Scikit-learn, and Streamlit. This project suggests similar movies based on a selected title by computing cosine similarity on movie features.

## 🚀 Features

- Recommends top 5 similar movies based on your selection.
- Clean and responsive UI built with Streamlit.
- Fast recommendations powered by precomputed similarity matrix.
- Uses `.pkl` files to store processed data and models for performance.

## 📂 Project Structure

```
movie-recommender-system/
│
├── app.py                  # Streamlit application file
├── movies.pkl              # Pickled file containing the movie titles
├── similarity.pkl          # Pickled similarity matrix
├── movies_dict.pkl         # Dictionary of movie metadata
├── README.md               # Project documentation
```

## 🧠 How It Works

1. Movie metadata is loaded from `movies_dict.pkl` and `movies.pkl`.
2. Cosine similarity between movie vectors is precomputed and stored in `similarity.pkl`.
3. When a movie is selected via the UI, the system retrieves and displays the top 5 similar movies.

## 💻 Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Pickle**

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/ai-ml/movie-recommender-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Use the dropdown in the UI to select a movie and view recommendations.

## 🗂️ Dataset Information

The model uses a custom dataset of movies which is processed and saved in the following files:

- `movies_dict.pkl`: A dictionary containing movie metadata
- `movies.pkl`: List of movie titles
- `similarity.pkl`: Cosine similarity matrix used for generating recommendations

These files are available in the Google Drive folder linked below and should be placed in the same directory as `app.py`.

📁 [Download Data Files](https://drive.google.com/drive/folders/1B3KuWuKgSZV9LDX1tDqP69lzRo58hNuQ?usp=drive_link)

## 📜 License

This project is licensed under the MIT License.

## 🙌 Acknowledgements

Inspired by various open-source tutorials and datasets available online. Built as part of a machine learning project for learning and demonstration purposes.
