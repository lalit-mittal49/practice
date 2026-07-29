import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
""" with open("ipl_stats.csv",'w+') as file:
    writer=csv.writer(file)
    writer.writerows([
        ['Player name','Team','Matches','Runs','Strike Rate'],
        ['Jarvis','pbks',2,570,450],
        ['melon','rbc',3,370,120],
        ['notew','rbc',4,590,230],
        ['rews','csk',2,70,100],
        ['defos','pbks',5,580,300],
        ['lavis','mi',2,534,100]
    ])
df=pd.read_csv("ipl_stats.csv")
sorted_df=df.sort_values(by="Runs",ascending=False)
print(sorted_df.head(5))
filtered=df[df['Strike Rate']>140]
print(filtered)
print(df['Runs'].mean())
highest_score=df['Runs'].max()
print(df[df['Runs']==highest_score])

x=df['Player name']
y=df['Runs']
plt.bar(x,y)
plt.xlabel("Players")
plt.ylabel("Runs")
plt.show()

x=df['Matches']
y=df['Runs']
plt.scatter(x,y)
plt.xlabel("Matches")
plt.ylabel('Runs')
plt.show()

data=df['Strike Rate']
plt.hist(data)
plt.xlabel("Strike Run")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show() """

#2
""" data={
    'Flight Number':['101','102','103','104','105','106'],
    'Source':['India','US','China','Pak','Nepal','EU'],
    'Destination':['US','EU','AFrica','China','India','India'],
    'Ticket Price':[2500,8000,12000,8000,5000,9000],
    'Seats Available':[32,20,30,14,26,16]
}
df=pd.DataFrame(data)
filtered=df[df['Ticket Price']>7000]
print(filtered)
filteredSeats=df[df['Seats Available']<25]
print(filteredSeats)

highTP=df['Ticket Price'].max()
lowTP=df['Ticket Price'].min()
avgTP=df['Ticket Price'].mean()
print(highTP)
print(lowTP)
print(avgTP)
desti_cc=df['Destination'].value_counts()
#data=df['Destination']
plt.pie(desti_cc,labels=desti_cc.index,autopct="%1.1f%%")
plt.show()

y=df['Ticket Price']
x=df['Flight Number']
plt.bar(x,y)
plt.xlabel("Flight no.")
plt.ylabel("Ticket Price")
plt.show()
 """

#3
""" with open("smartphone.csv",'w+') as file:
    writer=csv.writer(file)
    writer.writerows([
        ['Brand','Model','RAM','Storage','Battery','Price'],
        ['a','t',16,128,5600,45000],
        ['s','r',8,128,2800,30000],
        ['d','e',4,256,6000,20000],
        ['f','w',32,1024,8000,40000],
        ['g','q',4,128,5600,20000],
    ])
df=pd.read_csv('smartphone.csv')
filtram=df[df['RAM']>=8]
print(filtram)
filtprice=df[df['Price']<30000]
print(filtprice)
highpr=df['Price'].max()
print(highpr)
avgpr=df['Price'].mean()
print(avgpr)
x=df['RAM']
y=df['Price']
plt.scatter(x,y)
plt.show()

data=df['Battery']
plt.hist(data)
plt.show()

y=df['Price']
x=df['Brand']
plt.bar(x,y)
plt.show() """

#4
""" with open("orders.csv",'w+') as file:
    writer=csv.writer(file)
    writer.writerows([
        ['Order Id','Customer','Product','Quantity','Price'],
        [101,'q','w',14,1000],
        [102,'a','w',23,900],
        [103,'z','s',45,500],
        [104,'e','c',12,100],
        [105,'v','k',20,200],
        [106,'r','a',10,500]
    ])
df=pd.read_csv('orders.csv')
totalValue=df['Quantity']*df['Price']
print(totalValue)
df['Total']=totalValue
df.to_csv('orders.csv')
print(df['Total'].max())
print(df['Total'].min())
print(df['Total'].mean())
print(df[df['Total']>5000])

x=df['Order Id']
y=df['Total']
plt.xlabel('Order Id')
plt.ylabel('order Value')
plt.plot(x,y)
plt.show()
pro_cc=df['Product'].value_counts()
plt.pie(
    pro_cc,
    labels=pro_cc.index,
    autopct="%1.1f%%"
)
plt.show() """

#5
""" data={
    'City':['Mohali','Samana','Patiala','Kharar','Ludhiana'],
    'Temp':[25,45,30,35,16],
    'Humi':[50,40,60,85,95],
    'Rain':[80,50,60,30,70]
}
df=pd.DataFrame(data)
print(df[df['Temp']>35])
print(df[df['Humi']>70])
print(df['Rain'].mean())

x=df['Humi']
y=df['Temp']
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.scatter(x,y)
plt.show()

x=df['City']
y=df['Rain']
plt.plot(x,y)
plt.show()

data=df['Temp']
plt.hist(data)
plt.show() """

#6
""" data={
    'Movie':['a','s','d','f','g'],
    'Genre':['q','e','w','q','w'],
    'Duration':[3,3.5,2,1.5,3],
    'Rating':[9,8.5,5,3.6,9.5],
    'Release Year':[2025,2024,2025,2026,2024]
}
df=pd.DataFrame(data)
print(df[df['Release Year']>2020])
print(df[df['Rating']>8])
longest=df['Duration'].max()
print(df[df['Duration']==longest])
shortest=df['Duration'].min()
print(df[df['Duration']==shortest])
print(df['Duration'].mean())

ge_cc=df['Genre'].value_counts()
plt.pie(
    ge_cc,
    labels=ge_cc.index,
    autopct="%1.1f%%"
)
plt.show()

data=df['Rating']
plt.hist(data)
plt.show()

x=df['Movie']
y=df['Rating']
plt.bar(x,y)
plt.show() """

#7
""" data={
    'Member Name':['a','s','d','f','g','h'],
    'Age':[23,25,36,30,40,26],
    'Weight':[50,40,60,90,50,55],
    'Membership Plan':['p','n','g','p','g','g'],
    'Monthly Fee':[5000,1000,2500,5000,2500,2500]
}
df=pd.DataFrame(data)
print(df[df['Age']>30])
print(df[df['Membership Plan']=='p'])
print(df['Monthly Fee'].mean())
print(df['Monthly Fee'].max())

mp_cc=df['Membership Plan'].value_counts()
plt.pie(
    mp_cc,
    labels=mp_cc.index,
    autopct="%1.1f%%"
)
plt.show()

x=df['Age']
y=df['Weight']
plt.scatter(x,y)
plt.xlabel('Age')
plt.ylabel('Weight')
plt.show()

x=df['Member Name']
y=df['Monthly Fee']
plt.bar(x,y)
plt.show() """

#8
""" with open('uni.csv','w+') as file:
    writer=csv.writer(file)
    writer.writerows([
        ['name','course','percent','city'],
        ['a','q',68,'z'],
        ['s','w',89,'x'],
        ['d','q',45,'c'],
        ['f','e',70,'x'],
        ['g','q',80,'m']
    ])
df=pd.read_csv('uni.csv')
print(df[df['percent']>80])
print(df[df['city']=='delhi'])
print(df['percent'].mean())
print(df.groupby('course')['name'].count())

x=df['name']
y=df['percent']
plt.bar(x,y)
plt.xlabel='name'
plt.ylabel='percentage'
plt.show() """

#9
""" with open("sales.csv",'w+') as file:
    writer=csv.writer(file)
    writer.writerows([
        ['order id','item','quan','price','pay mode'],
        [101,'a',25,100,'o'],
        [102,'s',10,200,'c'],
        [103,'d',12,150,'o'],
        [104,'f',21,50,'o'],
        [105,'g',5,300,'c']
    ])
df=pd.read_csv('sales.csv')
total=df['quan']*df['price']
df['Total']=total
df.to_csv('sales.csv')
print(df['Total'].sum())
most=df['quan'].max()
print(df[df['quan']==most])
print(df['Total'].max())
print(df['Total'].min())
print(df['Total'].mean())

x=df['item']
y=df['Total']
plt.bar(x,y)
plt.show()

data=df['Total']
plt.hist(data)
plt.show() """

#10
""" df=pd.read_csv('country.csv')
#print(df.isnull())
#print(df.isnull().sum())
print(df[df['Population']>100])
print(df[df['Literacy Rate']>90])
print(df['GDP'].max())
print(df['GDP'].min())
print(df['GDP'].mean())
df=df.dropna()
print(df)
df.to_csv('world_population_cleaned.csv')
df=pd.read_csv('country.csv')

x=df['Country']
y=df['GDP']
plt.bar(x,y)
plt.show()

conti_count=df['Continent'].value_counts()
plt.pie(
    conti_count,
    autopct="%1.1f%%",
    labels=conti_count.index
)
plt.show()

x=df['GDP']
y=df['Population']
plt.scatter(x,y)
plt.show()

daata=df['Literacy Rate']
plt.hist(daata)
plt.show() """

#Challenge
""" df=pd.read_csv("movies_dataset.csv")
clean_df=df.dropna()
print(f'cleaned dataset:\n{clean_df}')
ratfil=df[df['Rating']>8]
yearfil=df[df['Release Year']>2020]
viewfil=df[df['Views (Millions)']>100]
print(f'Rating above 8\n{ratfil}\nAfter 2020:\n{yearfil}\nViews>100:\n{viewfil}')
filtered=df[(df['Rating']>8) & (df['Release Year']>2020) & (df['Views (Millions)']>100)]
print(f'All follows:\n{filtered}')
print(df.describe())
filtered.to_csv("top_movies.csv",index=False)
df=pd.read_csv("movies_dataset.csv")
x=clean_df['Movie Name']
y=clean_df['Views (Millions)']
plt.plot(x,y)
plt.show()

x=clean_df['Movie Name']
y=clean_df['Rating']
plt.bar(x,y)
plt.show()

gencc=df['Genre'].value_counts()
plt.pie(
    gencc,
    autopct='%1.1f%%',
    labels=gencc.index
)
plt.show()

x=clean_df['Rating']
y=clean_df['Duration']
plt.scatter(x,y)
plt.show()

data=clean_df['Views (Millions)']
plt.hist(data)
plt.show() """


#