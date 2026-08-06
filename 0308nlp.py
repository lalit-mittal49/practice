import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#1
docs=['I love NLP', 'NLP is amazing', 'I love coding']
words=set()
for doc in docs:
    tokens=doc.split()
    words.update(tokens)
print(words)

#2
""" vectorizer=CountVectorizer()
bow_matrix=vectorizer.fit_transform(documents)
print("Vocabulary:",vectorizer.get_feature_names_out())
print("Bow Representation:\n",bow_matrix)
print("Bow Representation:\n",bow_matrix.toarray()) """

#3
"""documents = [
    "I love NLP and Machine Learning",
    "Machine Learning is amazing",
    "I love learning new things"
]
tfidf_vectorizer=TfidfVectorizer()
tfidf_matrix=tfidf_vectorizer.fit_transform(documents)
print("TF-IDF Vocabulary:",tfidf_vectorizer.get_feature_names_out())
print("TF-IDF Representation:\n",tfidf_matrix)
print("TF-IDF Representation:\n",tfidf_matrix.toarray()) """

#4
""" text1 = "I love NLP"
text2 = "I enjoy NLP and text processing"
documents=[text1,text2]
tfidf_vectorizer=TfidfVectorizer()
tfidf_matrix=tfidf_vectorizer.fit_transform(documents)
print("TF-IDF Vocabulary:",tfidf_vectorizer.get_feature_names_out())
print("TF-IDF Representation:\n",tfidf_matrix)
print("TF-IDF Representation:\n",tfidf_matrix.toarray())
similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
print(similarity_score) """


#5
""" text1="Python, Machine Learning, SQL, Deep Learning, NLP"
text2="Looking for a Python developer with Machine Learning, NLP, SQL and Deep Learning skills."
document=[text1,text2]
tfidf_vector=TfidfVectorizer()
tfidf=tfidf_vector.fit_transform(document)
similarityScore=cosine_similarity(tfidf[0],tfidf[1])
match_percentage = round(similarityScore * 100, 2)
print(match_percentage) """ 