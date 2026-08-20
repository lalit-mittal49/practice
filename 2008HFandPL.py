from transformers import pipeline
from nltk import word_tokenize
import pandas as pd

#1
""" sentence=str(input('Enter the sentence: '))
while sentence!="exit":
    classifier=pipeline('sentiment-analysis')
    result=classifier(sentence)
    print(result)
    sentence=str(input('Enter the sentence: ')) """

#2
""" review=[
    'I love this product!',
    'This product is terrible.',
    'I was pleasantly surprised by how well this product worked.',
    'I had high hopes for this product',
    'This product is a game-changer!'
]
classifier=pipeline('sentiment-analysis')
result=classifier(review)
posRev=0
for i in range(len(review)):
    print(f'{review[i]} -> {result[i]['label']} -> {(result[i]['score'])*100:.2f}%')
    if result[i]['label']=='POSITIVE':
        posRev+=1
print(f'Total Positive Reviews: {posRev}')
print(f'Total Negative Reviews: {len(review)-posRev}') """

#3
""" prompt=str(input('Enter the prompt: '))
while prompt!="exit":
    generator=pipeline('text-generation', model='gpt2')
    result=generator(prompt, max_length=20, num_return_sequences=1)
    print(result)
    prompt=str(input('Enter the prompt: ')) """

#4
""" option=int(input('Enter the option: \n1 for Sentiment Analysis \n2 for Text Generation \n3 to Exit \n'))
while option!=3:
    if option==1:
        classifier=pipeline('sentiment-analysis')
        sent=str(input('Enter the sentence: '))
        result=classifier(sent)
        print(result)
    elif option==2:
        generator=pipeline('text-generation',model='gpt2')
        prompt=str(input('Enter the prompt: '))
        result=generator(prompt, max_length=20, num_return_sequences=1)
        print(result)
    else:
        print('Invalid option. Please try again.')
    option=int(input('Enter the option: \n1 for Sentiment Analysis \n2 for Text Generation \n3 to Exit \n')) """

#5
""" classifier=pipeline('sentiment-analysis')
ent=str(input('Enter the review: '))
reviews=[]
posRev=0
add=0
while ent!='exit':
    reviews.append(ent)    
    i=0
    tempresult=(classifier(ent))
    add+=(tempresult[0]['score']*100)
    print(f'label- {tempresult[i]['label']}')
    print(f'Score- {(tempresult[i]['score'])*100:.2f}%')
    if tempresult[i]['label']=='POSITIVE':
        posRev+=1
    i+=1
    ent=str(input('Enter the review: '))
result=classifier(reviews)
print(f'Total no. of postive reviews: {posRev}')
print(f'Total no. of negative reviews: {(len(reviews))-posRev}')
for j in range(0,len(result)-1):
    if result[j]['score']>result[j+1]['score']:
        mostconfi=result[j]['score']
        mostconfiRev=reviews[j]
print(f'Average: {add/len(result)}')
print(f'Most confident {mostconfiRev} {(mostconfi*100):.2f}') """

#6 doubt
""" generator=pipeline('text-generation',model='gpt2')
def generate(text):
    result=generator(text,max_length=20)
    print(f'Generated text:\n{result}')
def display():
    print('Enter your option:\n1 for Blog Introduction\n2 for Product Description\n3 for Social Media Post\n4 to Exit')
    option=int(input())
    return option
def options():
    sentence=str(input('Enter topic:'))
    print(generate(sentence))

ent=display()
while ent!=4:
    options()
    ent=display() """

#7 
""" generator=pipeline('text-generation',model='gpt2')
classifier=pipeline('text-classification')

review=str(input('Enter your review: '))

def senti(text):
    result=classifier(text)
    print(f'Sentiment:\n{result[0]['label']}')
    return result
def generate(text):
    prompt = (f"
You are a professional customer service representative.

Your task is to reply to the customer's review below.

Instructions:
- Respond as the company/customer support representative.
- Be polite, professional, and helpful.
- Keep the response short, around 2-4 sentences.
- If the customer is unhappy, apologize and offer help or a solution.
- If the customer is happy, thank them and show appreciation.
- Do not repeat or summarize the customer's review.
- Do not mention that you are an AI.
- Do not explain what you are doing.
- Start directly with the customer service response.
- Return only the response.

Customer review:
{text}

Customer service response:
")
    result=generator(prompt,max_new_tokens=50,return_full_text=False)
    print(f'Generated Response:\n{result[0]['generated_text']}')
senti(review)
generate(review) """

#8
classifier=pipeline('text-classification')
generator=pipeline('text-generation',model='gpt2')

def sentiment():
    text=str(input('Enter sentence to analyse:\n'))
    result=classifier(text)
    print(f'Review is {result[0]['label']}')

def generate():
    text=str(input('Enter prompt to generate:\n'))
    result=generator(text,max_new_tokens=100)
    print(f'Generated text:\n{result[0]['generated_text']}')

def multipleReviews():
    review=str(input('Enter Review: '))
    reviews=[]
    while review!='exit':
        reviews.append(review)
        review=str(input('Enter Review: '))
    result=classifier(reviews)
    posCount=0
    sumScore=0
    mostconfiscore=0
    for i in range(len(reviews)):
        if result[i]['label']=='POSITIVE':
            posCount+=1
        sumScore+=result[i]['score']
        if result[i]['score']>mostconfiscore:
            mostconfiscore=result[i]['score']
            mostconfilabel=result[i]['label']
    print(f'Total Reviews : {len(reviews)}')
    print(f'Positive : {posCount}')
    print(f'Negative : {(len(reviews)-posCount)}')
    print(f'Average : {(sumScore/len(reviews))*100}')
    print(f'Most Confident : {mostconfilabel} - {mostconfiscore*100}%')

def display():
    print('\nChoose ypur option:\n1. Analyze Sentiment\n2. Generate Text\n3. Analyze Multiple Reviews\n4. Exit\n')

display()
option=int(input())
while option!=4:
    match(option):
        case 1:
            sentiment()
            display()
            option=int(input())
        case 2:
            generate()
            display()
            option=int(input())
        case 3:
            multipleReviews()
            display()
            option=int(input())
        case _:
            print('Invalid input')
            display()
            option=int(input())
    