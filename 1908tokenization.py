import numpy as np
import pandas as pd
import string
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

#1
para = str(input("Enter the paragraph: "))
sentences = sent_tokenize(para)
words = word_tokenize(para)

print(f"Total Sentences: {len(sentences)}")
print(f"Total Words/Tokens: {len(words)}")
print(f"Sentences: {sentences}")
print(f"Words: {words}")

#2
para = str(input("Enter the paragraph: "))
lowered = str(para).lower()
words = word_tokenize(lowered)
unique = set(words)

for i in sorted(unique, key=words.count, reverse=True):
    frequency = words.count(i)
    print(f"{i} : {frequency}")

#3
para = str(input('Enter: '))
words = word_tokenize(para)

alpha = []
nums = []
alphanumeric = []
punctuations = []

for i in words:
    if i.isalpha():
        alpha.append(i)
    elif i.isdigit():
        nums.append(i)
    elif i.isalnum():
        alphanumeric.append(i)
    else:
        punctuations.append(i)

print(f"Alphabetic tokens: {alpha}")
print(f"Numeric tokens: {nums}")
print(f"Alphanumeric/Mixed tokens: {alphanumeric}")
print(f"Punctuation & Special Symbols: {list(set(punctuations))}")

#4
para = str(input('Enter: '))
words = word_tokenize(para)

alpha_tokens = [w for w in words if w.isalpha()]
numeric_tokens = [w for w in words if w.isdigit() or re.match(r'^\d+(\.\d+)?$', w)]
special_tokens = [w for w in words if not w.isalnum() and not re.match(r'^\d+(\.\d+)?$', w)]

print(f"Total Tokens: {len(words)}")
print(f"Unique Tokens (Vocabulary Size): {len(set(words))}")
print(f"Alphabetic Token Count: {len(alpha_tokens)}")
print(f"Numeric Token Count: {len(numeric_tokens)}")
print(f"Special Characters/Punctuation Count: {len(special_tokens)}")

word_only_tokens = [w for w in words if w.isalnum()]
if word_only_tokens:
    print(f"Longest Word: {max(word_only_tokens, key=len)}")
    print(f"Shortest Word: {min(word_only_tokens, key=len)}")

#5
para = str(input('Enter: '))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    words = word_tokenize(text)
    tokens = [i for i in words if len(i) >= 3]
    return tokens

print(clean_text(para))

#6
para = str(input('Enter: '))

def pipeline(text):
    sentences = sent_tokenize(text)
    print(f'Sentences : {sentences}')
    
    words = word_tokenize(text)
    print(f'Words : {words}')
    
    lowered = [w.lower() for w in words]
    print(f'Lower cased : {lowered}')
    
    punctuation_set = set(string.punctuation)
    afterPunc = [w for w in lowered if w not in punctuation_set and any(c.isalnum() for c in w)]
    print(f'After removing punctuation : {afterPunc}')
    
    stop_words = set(stopwords.words('english'))
    afterStopwords = [w for w in afterPunc if w not in stop_words]
    print(f'After removing stopwords : {afterStopwords}')
    
    final_tokens = [w for w in afterStopwords if len(w) >= 2]
    print(f'Final Clean Tokens : {final_tokens}')

pipeline(para)

#7
para = "I love #Python6 and #AI ! 12345 Check https://example.com @student123 :blush:"

tokens1 = para.split()
tokens2 = word_tokenize(para)
tokens3 = re.findall(r'\w+', para)

print(f'Tokens1 (split())           : {tokens1} | Length: {len(tokens1)}')   
print(f'Tokens2 (word_tokenize())   : {tokens2} | Length: {len(tokens2)}')
print(f'Tokens3 (re.findall(\\w+))  : {tokens3} | Length: {len(tokens3)}')

print("\n--- Comparison & Explanation ---")
print("1. str.split(): Splits solely on whitespace. Punctuations and special characters stay attached to words (e.g., '!').")
print("2. word_tokenize(): Separates punctuation marks, emojis, and symbols into individual tokens while preserving sentence grammar.")
print("3. re.findall(r'\\w+'): Extracts only alphanumeric words/numbers; completely strips all punctuation, URLs, '@', and '#' symbols.")

#8
para = "I love #Python6 and #AI ! 12345 Check https://example.com @student123 :blush:"

def social_mediaTokenizer(text):
    hashtags = re.findall(r'#\w+', text)
    mentions = re.findall(r'@\w+', text)
    urls = re.findall(r'https?://\S+', text)
    emojis = re.findall(r':[a-zA-Z0-9_]+:', text)
    
    cleaned = text
    for item in hashtags + mentions + urls + emojis:
        cleaned = cleaned.replace(item, ' ')
        
    tokens = word_tokenize(cleaned)
    words = [t for t in tokens if t.isalpha()]
    numbers = [t for t in tokens if t.isdigit()]
    special_chars = [t for t in tokens if not t.isalnum()]

    print(f'Original Text   : {text}')
    print(f'Hashtags        : {hashtags}')
    print(f'Mentions        : {mentions}')
    print(f'URLs            : {urls}')
    print(f'Emojis          : {emojis}')
    print(f'Words           : {words}')
    print(f'Numbers         : {numbers}')
    print(f'Special Chars   : {special_chars}')

social_mediaTokenizer(para)

#9
word = 'playing'

def multi_level_tokenizer(text):
    words = word_tokenize(text)
    print(f'Word Tokens       : {words}')
    
    characters = [char for char in text if char != ' ']
    print(f'Character Tokens  : {characters}')
    
    subwords_2gram = [''.join(bg) for bg in ngrams(text, 2)]
    subwords_3gram = [''.join(tg) for tg in ngrams(text, 3)]
    print(f'Subwords (2-grams): {subwords_2gram}')
    print(f'Subwords (3-grams): {subwords_3gram}')

multi_level_tokenizer(word)

#10
para = "I love #Python6 and AI ! 12345 Check1 Check https://example.com @student123 :blush:"

def nlpAnalyzer(txt):
    sentences = sent_tokenize(txt)
    words = word_tokenize(txt)
    unique = set(words)
    stop_words = set(stopwords.words('english'))
    
    alphatok = []
    numtok = []
    punctok = []
    stopwordtok = []
    
    for i in words:
        if i.isalpha():
            alphatok.append(i)
            if i.lower() in stop_words:
                stopwordtok.append(i.lower())
        elif i.isdigit():
            numtok.append(i)
        elif not i.isalnum():
            punctok.append(i)

    cleaned_tokens = [w.lower() for w in words if w.isalnum() and w.lower() not in stop_words and len(w) >= 2]

    print(f'Number of Sentences           : {len(sentences)}')
    print(f'Total Tokens                  : {len(words)}')
    print(f'Unique Tokens                 : {len(unique)}')
    print(f'Number of Alphabetic Tokens   : {len(alphatok)}')
    print(f'Number of Numeric Tokens      : {len(numtok)}')
    print(f'Number of Punctuation Tokens  : {len(punctok)}')
    print(f'Number of Stopwords           : {len(stopwordtok)}')
    print(f'Final Cleaned Tokens          : {cleaned_tokens}')
    
    wordseries = pd.Series(words)
    print(f'\nTop 5 Most Common Tokens      :\n{wordseries.value_counts().head(5)}')
    print(f'\nAverage Token Length          : {wordseries.str.len().mean():.2f}')
    print(f'Max Token Length              : {wordseries.str.len().max()}')
    print(f'Min Token Length              : {wordseries.str.len().min()}')

nlpAnalyzer(para)