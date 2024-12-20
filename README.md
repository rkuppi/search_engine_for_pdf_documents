# Semantic Search for Research Abstracts  

This project implements a semantic search system that identifies the most relevant research abstracts for a given user query. It leverages word embeddings, centroid-based ranking, and a Flask API for dynamic query handling.

---

## 🚀 Features  
- **Preprocessing and Tokenization**: Cleans and tokenizes abstracts using spaCy.  
- **Word Embeddings**: Generates vector representations of words using Word2Vec.  
- **Centroid Calculation**: Computes document-level vectors by aggregating word embeddings.  
- **Cosine Similarity Ranking**: Matches user queries to abstracts based on semantic similarity.  
- **Flask API**: Exposes an endpoint for submitting queries and retrieving ranked abstracts.  

---

## 🛠️ Technologies Used  
- **Python**: Core programming language.  
- **spaCy**: Tokenization and sentence segmentation.  
- **Word2Vec**: Word embeddings (via `gensim`).  
- **Flask**: API development.  
- **NumPy**: Numerical computations.  
- **Pandas**: Data manipulation.  

---

## 📂 Project Structure  
