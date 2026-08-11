import re
import matplotlib.pyplot as plt
import nltk
import csv
import numpy as np
import pandas as pd
import seaborn as sns
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
customer=pd.read_csv("proCustom.csv")
stock=pd.read_csv('proStock.csv')

def checkStock(ingredient):
    credited = stock[(stock['Item_Name'] == ingredient) & (stock['Transaction_Type'] == 'credit')]['Quantity'].sum()
    debited = stock[(stock['Item_Name'] == ingredient) & (stock['Transaction_Type'] == 'debit')]['Quantity'].sum()
    left=credited-debited   
    return left

def orderstock(ingredient):
    updated=checkStock(ingredient)+10
    with open("proStock.csv",'a') as file:
        writer=csv.writer(file)
        writer.writerow([
            ingredient,10,'credit'
        ])
    print('Stock Ordered Successfully')
    print('updated stock : ',updated)

def dangerZone():
    for items in stock['Item_Name'].unique():
        if(checkStock(items)<10):
            print(items)
            return True
        else:
            print(items)
            return False

def orderFood(orderedItem):
    if orderedItem==1:
        if checkStock('Cooking Oil')>5 and checkStock('Chicken Breast')>2:
            print('ordered Successfully')
            with open("proStock.csv",'a') as file:
                writer=csv.writer(file)
                writer.writerows([
                    ['Cooking Oil',5,'debit'],
                    ['Chicken Breast',2,'debit']
                ])
        else:
              print('out of stock')
    if orderedItem==2:
        if checkStock('Sauce')>1 and checkStock('Cheese')>2 and checkStock('Maida')>3:
            print('ordered Successfully')
            with open("proStock.csv",'a') as file:
                writer=csv.writer(file)
                writer.writerows([
                    ['Sauce',1,'debit'],
                    ['Maida',3,'debit'],
                    ['Cheese',2,'debit']
                ])
        else:
              print('out of stock')
    if orderedItem==3:
        if checkStock('Tomatoes')>1 and checkStock('Noodles')>5 and checkStock('Onions')>3:
            print('ordered Successfully')
            with open("proStock.csv",'a') as file:
                writer=csv.writer(file)
                writer.writerows([
                    ['Tomatoes',1,'debit'],
                    ['Noodles',5,'debit'],
                    ['Onions',2,'debit']
                ])
        else:
              print('out of stock')

def spendPrediction():
    features=['Preferred_Cuisine','Favorite_Food_Item','Visit_Frequency','Preferred_Order_Type','Loyalty_Member','Satisfaction_Rating']
    target='Avg_Spend_Per_Visit_USD'
    X_raw = customer[features]
    X = pd.get_dummies(
        X_raw,
        columns=[
            "Preferred_Cuisine",
            "Favorite_Food_Item",
            "Visit_Frequency",
            "Preferred_Order_Type",
            "Loyalty_Member",
        ],
        drop_first=True,
    )
    y = customer[target]
    X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    model=LinearRegression()
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test) 
    print(y_pred)

choice=1
while(choice!=3):
    choice=int(input('Enter ypur option:\n1 for customer\n2 for staff :\n3 to exit\n'))
    match choice:
        case 1:
            orderedItem=int(input('What do you want to order: \nMenu:\n1 for Butter Chicken & Naan\n2 for Margherita Pizza\n3 for Veg Hakka Noodles\n'))
            orderFood(orderedItem)
        case 2:
            ent=int(input('Enter PIN\n'))
            pin=1234
            if ent==pin:
                  opt=int(input('Enter ur choice:\n1 to check stock\n2 to order ingredients\n3 for predicting bill'))
                  if opt==1:
                        ingName=input('Enter name of ingredient to check stock:\n')
                        checkStock(ingName)
                  elif opt==2:
                        ingName=input('Enter name of ingredient to check stock:\n')
                        orderstock(ingName)
                  elif opt==3:
                        spendPrediction()
                  else:
                        print('wrong input')
            else:
                  print('Wrong PIN try again')
        case 3:
              break;
        case _:
                print('wrong input')