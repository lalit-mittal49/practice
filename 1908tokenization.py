import numpy as np
import pandas as pd
import nltk
from sympy import re
import re
from nltk import word_tokenize
from nltk import sent_tokenize

#1
""" from nltk.tokenize import sent_tokenize
para=str(input("Enter the paragraph: "))
sentenses=sent_tokenize(para)

from nltk import word_tokenize
words=word_tokenize(para)

print(len(sentenses))
print(len(words))
print(sentenses)
print(words) """

#2
""" para=str(input("Enter the paragraph: "))
lowered=str(para).lower()
from nltk import word_tokenize
words=word_tokenize(lowered)
unique=set(words)
max_count=0
for i in sorted(unique, key=words.count,reverse=True):
    frequency=words.count(i)
    print(f"{i} : {frequency}") """

#3
""" para=str(input('enter: '))
words=re.sub(r'[^a-zA-Z]',' ', para)
print(word_tokenize(words))
punctuation=re.sub(r'[a-zA-Z0-9]',' ', para)
print(set(word_tokenize(punctuation)))
numbers=re.sub(r'[^\d.]',' ', para)
numTokens=word_tokenize(numbers)
for i in numTokens:
    if i=='.':
        numTokens.remove(i)
print(numTokens) """

#4
""" para=str(input('enter: '))
words=word_tokenize(para)
print(len(words))
print(len(set(words)))
print(len(word_tokenize(re.sub(r'[^a-zA-Z]',' ', para))))
numTokens=word_tokenize(re.sub(r'[^0-9.]',' ', para))
for i in numTokens:
    if i=='.':
        numTokens.remove(i)
print(len(numTokens))
print(len(word_tokenize(re.sub(r'[^a-zA-Z0-9]',' ', para))))
print(max(words, key=len))
print(min(words, key=len)) """

#5
""" para=str(input('enter: '))
def clean_text(text):
    text=str(text).lower()
    text=re.sub(r'[^a-zA-Z]',' ', text)
    words=word_tokenize(text)
    tokens=[]
    for i in words:
        if len(i)>=3:
            tokens.append(i)
    return tokens
print(clean_text(para)) """

#6
""" para=str(input('enter: '))
def pipeline(text):
    sentences=sent_tokenize(text)
    print(f'Sentences : {sentences}')
    words=word_tokenize(text)
    print(f'Words : {words}')
    lowered=[]
    for w in words:
        lowered.append(w.lower())
    print(f'Lower cased : {lowered}')
    punctuation=re.sub(r'[a-zA-Z0-9]',' ', text)
    puncTokens=word_tokenize(punctuation)
    print(f'Punctuation : {puncTokens}')
    afterPunc=[]
    for i in lowered:
        if i not in puncTokens:
            afterPunc.append(i)
    print(f'After removing punctuation : {afterPunc}')
pipeline(para) """

#7
""" para="I love #Python6 and #AI ! 12345 Check https://example.com @student123 :blush:"
tokens1=str(para).split()
tokens2=word_tokenize(para)
tokens3=re.findall(r'\w+', para)
print(f'Tokens1 : {tokens1} and length : {len(tokens1)}')   
print(f'Tokens2 : {tokens2} and length : {len(tokens2)}')
print(f'Tokens3 : {tokens3} and length : {len(tokens3)}') """

#8
""" para="I love #Python6 and #AI ! 12345 Check https://example.com @student123 :blush:"
def social_mediaTokenizer(text):
    tokens=str(text).split()
    print(f'Tokens : {tokens}')
    hashtags=[]
    mentions=[]
    url=[]
    emojis=[]
    words=[]
    numbers=[]
    for i in tokens:
        if i.startswith('#'):
            hashtags.append(i)
        elif i[:5]=='https':
            url.append(i)
        elif i[0]==':' and i[-1]==':':
            emojis.append(i)
        elif i.isalpha():
            words.append(i)
        elif i.isdigit():
            numbers.append(i)
    mentions=re.findall(r'@\w+', text)
    print(f'Hashtag : {hashtags}')
    print(f'Mention : {mentions}')
    print(f'URL : {url}')
    print(f'Emoji : {emojis}')
    print(f'Words : {words}')
    print(f'Numbers : {numbers}')

social_mediaTokenizer(para) """

#9 doubt
word='playing'

def clean(text):
    words=word_tokenize(text)
    print(f'Words : {words}')
    print(f'characters: {str(words)}')

clean(word)


#10
""" para="I love #Python6 and AI ! 12345 Check1 Check https/example.com @student123 blush:"
def nlpAnalyzer(txt):
    sentences=sent_tokenize(txt)
    print(f'Number of Sentences : {len(sentences)}')
    words=word_tokenize(txt)
    print(f'Words : {words}')
    print(f'Number of Words : {len(words)}')
    unique=set(words)
    print(f'Number of Unique Tokens : {len(unique)}')
    alphatok=0
    numtok=0
    punctok=0
    for i in words:
        if i.isalpha():
            alphatok+=1
        elif i.isdigit():
            numtok+=1
        else:
            punctok+=1
    print(f'Number of Alphabetic Tokens : {alphatok}')
    print(f'Number of Numeric Tokens : {numtok}')
    print(f'Number of Punctuation Tokens : {punctok}')
    wordseries=pd.Series(words)
    print(f'most common tokens : {wordseries.value_counts().head(1)}')
    print(f'least common tokens : {wordseries.value_counts().tail(1)}')
    print(f'most common tokens : {wordseries.value_counts().head(5)}')
    print(f'averagelength : {wordseries.str.len().mean()}')
    print(f'maxlength : {wordseries.str.len().max()}')
    print(f'minlength : {wordseries.str.len().min()}')

nlpAnalyzer(para) """