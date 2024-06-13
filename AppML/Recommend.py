import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def get_recommendations(user_id, top_n, df):

    df = df[df['behavior'] == 'play']

    df = df.drop(['behavior', 'unknown'], axis=1)

    utility_matrix = df.pivot_table(
        index='user_id', columns='game', values='time').fillna(0)

    cosine_sim = cosine_similarity(utility_matrix)

    cosine_sim_df = pd.DataFrame(
        cosine_sim, index=utility_matrix.index, columns=utility_matrix.index)

    top_500_user = cosine_sim_df[user_id].sort_values(ascending=False)[
        1:501].index

    played_games = utility_matrix.loc[user_id]
    played_games = played_games[played_games > 0].index.tolist()

    recommend_games = {}
    for other_user in top_500_user:
        if other_user == user_id:
            continue
        similarity_score = cosine_sim_df.loc[user_id, other_user]
        for game in utility_matrix.columns:
            if game in played_games:
                continue
            if game not in recommend_games:
                recommend_games[game] = 0
            else:
                recommend_games[game] += similarity_score * \
                    utility_matrix.loc[other_user, game]

    recommend_games = sorted(recommend_games.items(),
                             key=lambda x: x[1], reverse=True)
    return recommend_games[:top_n]
