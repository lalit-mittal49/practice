import pandas as pd
import numpy as np
import re
import regex
#from nltk.corpus import stopwords
df=pd.read_csv("spam_dataset.csv")

#1
""" print(df.shape)
print(df.columns)
print(df.head(5))
print(df['label'].value_counts()) """

#2
def clean_text(text):
    text=str(text).lower()
    text=re.sub(r"\S+@\S+","",text)
    text=re.sub(r"\d+",'',text)
    text=re.sub(r"[^a-z\s]",'',text)
    text=re.sub(r"\s+"," ",text)
    return text
df['Cleaned message']=df['message'].apply(clean_text)
df.to_csv('spam_dataset.csv',index=False)
print("BEFORE cleaning (first resume, first 300 chars):\n", str(df["message"].iloc[0])[:300])
print("\nAFTER cleaning (first resume, first 300 chars):\n", df["Cleaned message"].iloc[0][:300])

#3
def tokenize_text(text):
    return str(text).split()
df['Tokens']=df['Cleaned message'].apply(tokenize_text)
df.to_csv('spam_dataset.csv',index=False)
print("Total tokens in first resume:", len(df["Tokens"].iloc[0]))
print("First 20 tokens of first resume:\n", df["Tokens"].iloc[0][:20])

#4
""" stop_words=set(stopwords.words("english"))
def remStop(Tokens):
    return [word for word in Tokens if word not in stop_words]
df["new tokens"]=df['Tokens'].apply(remStop)
df.to_csv('spam_dataset.csv',index=False)
print("Tokens BEFORE stopword removal (count):", len(df["Tokens"].iloc[0]))
print("Tokens AFTER stopword removal (count):", len(df["new tokens"].iloc[0]))
print("Tokens AFTER stopword removal (count):", df["new tokens"].iloc[0][:20]) """


#5
data=pd.read_csv("spam_dataset.csv")
data['cleaned']=data['message'].apply(clean_text)
data['tokenised']=data['cleaned'].apply(tokenize_text)
#data['afterstop']=data["tokenised"].apply(remStop)
data.to_csv("spam_dataset.csv",index=False)