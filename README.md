# Semantic Search for Research Abstracts  

This project implements a **semantic search system** designed to identify the most relevant research abstracts for a given query. It leverages **word embeddings** for semantic representation, computes centroid-based similarity scores, and provides query results via a **Flask API**.  

---

## 🚀 Features  
- **Data Preprocessing**: Tokenizes and processes abstracts using spaCy.  
- **Word Embeddings**: Uses Word2Vec to generate vector representations of words.  
- **Centroid Calculation**: Computes document-level vectors as centroids of word embeddings.  
- **Semantic Ranking**: Ranks abstracts based on cosine similarity to the query.  
- **API Integration**: Exposes a REST API for query input and results retrieval.  

---

## 🛠️ Technologies Used  
- **Python**: Core programming language for implementation.  
- **spaCy**: For text preprocessing and tokenization.  
- **Word2Vec**: To generate word embeddings (`gensim` library).  
- **Flask**: For creating the API.  
- **NumPy**: For numerical computations (e.g., cosine similarity).  
- **Pandas**: For data manipulation and organization.  

---

