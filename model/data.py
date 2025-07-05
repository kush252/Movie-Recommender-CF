import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("ml-latest-small/movies.csv")
ratings = pd.read_csv("ml-latest-small/ratings.csv")

user_item_matrix_copy = ratings.pivot_table(index='userId', columns='movieId', values='rating')
user_item_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
# print(user_item_matrix.head(5))

# Fill NaNs with 0 for similarity calculation
item_user_matrix = user_item_matrix.T.fillna(0)

# Compute similarity between items
item_similarity = cosine_similarity(item_user_matrix)


item_similarity_df = pd.DataFrame(item_similarity, index=item_user_matrix.index, columns=item_user_matrix.index)
# print(item_similarity_df.head(10))
  
def predict_rating(target_movie_id,user_Id,k=10):
    if target_movie_id not in item_similarity_df:
        return None
    
    user_ratings=user_item_matrix_copy.loc[user_Id].dropna()

    similar_movies=item_similarity_df.loc[target_movie_id,user_ratings.index]

    top_k=similar_movies.sort_values(ascending=False).head(k)

    top_k_ratings=user_ratings.loc[top_k.index]

    num=(top_k_ratings*top_k).sum()
    den=top_k.sum()

    if den==0:
        return None
    return num/den

def recommender(user_Id,n=5):
    not_rated=user_item_matrix_copy.loc[user_Id][user_item_matrix_copy.loc[user_Id].isna()].index
    predictions=[]
    for movies in not_rated:
        pred = predict_rating(movies,user_Id)
        if pred is not None:
            predictions.append((movies,pred))
    
    sorted_predictions = sorted(predictions, key=lambda x: x[1], reverse=True)
    return sorted_predictions[:10]

user_Id = int(input("Enter User Id: "))
predictions_list=recommender(user_Id)


titles=movies['title']
for val in predictions_list:
    movie_id = val[0]
    title = movies[movies['movieId'] == movie_id]['title'].values[0]
    print(title)

