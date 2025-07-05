---

# 🎬 Movie Recommender System

A content-personalized movie recommender system built using **item-item collaborative filtering**. It predicts user ratings based on **cosine similarity** between movies and recommends the top-N movies the user is likely to enjoy.

---

## 📌 Features

* Predicts user ratings for unrated movies using similarity-weighted scores
* Recommends top-N movies personalized to each user
* Uses **cosine similarity** between movie vectors (based on user ratings)
* Based on the **MovieLens (ml-latest-small)** dataset
* Built with **Pandas** and **scikit-learn**

---

## 📂 Dataset

This system uses the [MovieLens Latest Small Dataset](https://grouplens.org/datasets/movielens/latest/) which includes:

* `movies.csv`: Movie metadata (ID, title, genres)
* `ratings.csv`: User ratings (userId, movieId, rating, timestamp)

---

## 🚀 How It Works

1. Creates a **user-item matrix** from the ratings data.
2. Transposes and fills missing values to compute **item-item similarities**.
3. For each user, the system:

   * Identifies movies they haven’t rated
   * Predicts their ratings using weighted average of similar movies
   * Recommends the top-N movies with the highest predicted scores

---

## 📈 Example Output

```plaintext
Interstellar (2014): Predicted Rating = 5
Inception (2010): Predicted Rating = 4.8
The Matrix (1999): Predicted Rating = 4.75
```

---