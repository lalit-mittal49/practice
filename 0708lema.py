import re
import matplotlib.pyplot as plt
import nltk
import pandas as pd
import seaborn as sns
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

#1
df = pd.read_csv('news.csv')

print("Shape of the dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head(5))

print("\nLast 5 rows:")
print(df.tail(5))

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nNumber of news articles in each category:")
print(df['category'].value_counts())

#2
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize_text(text):
    return str(text).split()

stop_words = set(stopwords.words('english'))
def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

lemmatizer = WordNetLemmatizer()
def lemmatize_tokens(tokens):
    return [lemmatizer.lemmatize(word) for word in tokens]

# Apply preprocessing
df['cleaned_text'] = df['content'].apply(clean_text)
df['tokens'] = df['cleaned_text'].apply(tokenize_text)
df['tokens_after_stopwords'] = df['tokens'].apply(remove_stopwords)
df['lemmatized_tokens'] = df['tokens_after_stopwords'].apply(lemmatize_tokens)
df['final_text'] = df['lemmatized_tokens'].apply(lambda x: ' '.join(x))

print("\n--- First News Article Preprocessing Output ---")
print("Original News:", df['content'].iloc[0])
print("Cleaned News:", df['cleaned_text'].iloc[0])
print("Tokens:", df['tokens'].iloc[0])
print("Tokens after Stopword Removal:", df['tokens_after_stopwords'].iloc[0])
print("Lemmatized Tokens:", df['lemmatized_tokens'].iloc[0])
print("Final Processed News:", df['final_text'].iloc[0])

#3
tfidf = TfidfVectorizer(max_features=3000, min_df=1, max_df=0.9, ngram_range=(1, 2))
X_tfidf = tfidf.fit_transform(df['final_text'])

print("\nShape of the TF-IDF matrix:", X_tfidf.shape)
print("\nFirst 20 feature names:")
print(tfidf.get_feature_names_out()[:20])

#4
X = X_tfidf
y = df['category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nFirst 10 Actual Categories:")
print(y_test.iloc[:10].values)

print("\nFirst 10 Predicted Categories:")
print(y_pred[:10])

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

#5
def predict_news_category(news_article):
    cleaned = clean_text(news_article)
    tokens = tokenize_text(cleaned)
    no_stopwords = remove_stopwords(tokens)
    lemmatized = lemmatize_tokens(no_stopwords)
    final_processed = ' '.join(lemmatized)
    vectorized = tfidf.transform([final_processed])
    prediction = model.predict(vectorized)
    return prediction[0]

cm = confusion_matrix(y_test, y_pred)
labels = sorted(y.unique())

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Category')
plt.ylabel('Actual Category')
plt.tight_layout()
plt.savefig('confusion_matrix.png')
plt.show()