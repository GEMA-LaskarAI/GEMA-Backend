import os
import pandas as pd
import json
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

load_dotenv()

def load_env():
    db_user = os.getenv('DB_USER')
    db_pass = quote_plus(os.getenv('DB_PASS'))
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    db_uri = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(db_uri)

    return engine

def train_data():
    engine = load_env()
    query = """
    SELECT
        id,
        question_id,
        major_id,
        weight
    FROM gema_question_major_weights
    """
    qmw_df = pd.read_sql(query, engine)

    df = qmw_df.pivot(
        index='major_id',
        columns='question_id',
        values='weight'
    ).reset_index()

    numerical_columns = df.select_dtypes(include=['number']).columns
    scaler = StandardScaler()
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    X = df.drop(columns=['major_id']).values
    y = df['major_id'].values

    k = df.shape[0] // 3
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(X)

    df['cluster'] = clusters
    df['major_id'] = y

    return df, X, scaler, kmeans

def recommend_majors(answer: list[int]):
    engine = load_env()
    df, X, scaler, kmeans = train_data()
    if len(answer) != X.shape[1]:
        raise ValueError(f"Panjang jawaban siswa ({len(answer)}) tidak sesuai jumlah soal ({X.shape[1]})")
    
    answer_scaled = scaler.transform([answer])
    predicted_cluster = kmeans.predict(answer_scaled)[0]

    cluster_df = df[df['cluster'] == predicted_cluster]
    query = """
    SELECT
        id as major_id,
        name
    FROM gema_majors
    """
    major_df = pd.read_sql(query, engine)
    merged_df = cluster_df.merge(
        major_df,
        left_on='major_id',
        right_on='major_id',
        how='left'
    )
    top_majors = merged_df[['major_id', 'name']].head(3)

    return json.loads(top_majors.to_json(orient='records'))
