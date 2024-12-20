from flask import Flask, request, jsonify
from gensim.models import Word2Vec
import numpy as np
import pandas as pd

app = Flask(__name__)


df_data = pd.read_csv(r'./artifacts/processed_data.csv')  


model = Word2Vec.load(r"./artifacts/word2vec_model.model")

df_data["centroid"] = df_data["centroid"].apply(lambda x: np.array(eval(x)))

def rank_docs(model, query, df_covid, num):
    """Ranks documents based on cosine similarity between query and document centroids."""
    cosine_list = []
    query_vectors = []
    query_tokens = query.split(" ")
    for token in query_tokens:
        try:
            query_vectors.append(model.wv[token])
        except KeyError:
            continue


    for _, row in df_covid.iterrows():
        centroid = row['centroid']
        total_sim = 0
        for vector in query_vectors:
            cos_sim = np.dot(vector, centroid) / (np.linalg.norm(vector) * np.linalg.norm(centroid))
            total_sim += cos_sim
        # cosine_list.append((row['title'], row['processed_abstract'], total_sim))
        cosine_list.append((row['title'], total_sim))
    cosine_list.sort(key=lambda x: x[1], reverse=True)
    papers_list = []
    for item in cosine_list[:num]:
        # papers_list.append({"title": item[0], "abstract": item[1], "score": item[2]})
        papers_list.append({"title": item[0], "score": item[1]})
    return papers_list

@app.route('/query', methods=['POST'])
def query():
    """API endpoint for querying ranked documents."""
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Invalid request. 'query' is required."}), 400

    query_text = data['query']
    top_matches = data.get('top_matches', 10)

    try:
        results = rank_docs(model, query_text, df_data, top_matches)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
