import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1
""" df=pd.read_csv("employee_records.csv")
print(df.info())
print(df.isnull().sum())
numeric_cols = ['Experience (Years)', 'Salary', 'Performance Rating']
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())
print(df.duplicated().sum())
df=df.drop_duplicates()
df.to_csv('employee_records.csv',index=False)
avg=df.groupby('Department')['Salary'].mean()
result=avg.sort_values(ascending=False)
print(result.head(5))
result2=df.groupby('City')['Performance Rating'].mean()
result2=result2.sort_values(ascending=False)
print(result2.head())
result3=df.sort_values('Salary',ascending=False)
print(result3.head())
x=avg.index
y=avg
plt.bar(x,y)
plt.show()

empcc=df.groupby('City')['Name'].nunique()
plt.pie(empcc,autopct="%1.1f%%",labels=empcc.index)
plt.show()

plt.hist(df['Salary'])
plt.show() """

#2
""" df=pd.read_csv('retail_sales_intelligence.csv')
Finalam=(df['Quantity']*df['Price'])-df['Discount']
df['FinalAmount']=Finalam
df.to_csv('retail_sales_intelligence.csv',index=False)
print(df[df['FinalAmount']==df['FinalAmount'].max()])
print(df[df['FinalAmount']==df['FinalAmount'].min()])
result1=df.groupby('Category')['FinalAmount'].mean()
print(result1)
result2=df.groupby('City')['FinalAmount'].sum()
result2=result2.sort_values(ascending=False)
print(result2.head(1))
result3=df.groupby('Product')['FinalAmount'].sum()
result3=result3.sort_values(ascending=False)
print(result3)

x=result1.index
y=result1
plt.bar(x,y)
plt.show()

data=df['FinalAmount']
plt.hist(data)
plt.show()

citycc=df['City'].value_counts()
plt.pie(
    citycc,
    labels=citycc.index,
    autopct="%1.1f%%"
)
plt.show() """

#3
""" df=pd.read_csv("hospital_management_data.csv")
print(df[df.duplicated()==True])
df=df.dropna()
df.to_csv('hospital_management_data.csv',index=False)
result=df.groupby('Department')['Bill Amount'].sum()
result1=result.sort_values(ascending=False)
print(result1.head())
result2=df.groupby('Doctor')['Patient ID'].nunique()
result2=result2.sort_values(ascending=False)
print(result2.head(1))
result3=df.groupby('Department')['Bill Amount'].mean()
print(result3)
result4=df.groupby('City')['Bill Amount'].sum()
result4=result4.sort_values(ascending=False)
print(result4.head(1))

plt.figure(figsize=(15,5))

plt.subplot(1, 3, 1)
x=result.index
y=result1
plt.xticks(rotation=45)
plt.bar(x,y)

plt.subplot(1, 3, 2)
result51=df.groupby('Department')['Patient ID'].nunique()
plt.pie(
    result51,
    labels=result51.index,
    autopct="%1.1f%%"
)

plt.subplot(1, 3, 3)
data=df['Bill Amount']
plt.hist(data)
plt.show()

plt.tight_layout() """

#4
""" df=pd.read_csv('netflix_content_analytics.csv')
df=df.drop_duplicates()
df.to_csv('netflix_content_analytics.csv',index=False)
df['Rating']=df['Rating'].fillna(df['Rating'].mean())
result11=df.groupby('Genre')['Title'].nunique()
print(result11)
result12=result11.sort_values(ascending=False)
print(result12.head(2))
print(df[df['Rating']==df['Rating'].max()])
print(df[df["Release Year"]>2020])
result21=df.sort_values('Rating',ascending=False)
print(result21)

data=df.groupby('Genre')['Rating'].mean()
x=data.index
y=data
plt.bar(x,y)
plt.show()

langcc=df['Language'].value_counts()
plt.pie(
    langcc,
    labels=langcc.index,
    autopct="%1.1f%%"
)
plt.show() """

#5
""" df=pd.read_csv('ecommerce_sales_dirty_dataset.csv')
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())
df=df.drop_duplicates()
df.to_csv('e',index=False)
result1=df['Category'].value_counts()
print(result1)
result2=df['Payment Method'].value_counts()
print(result2)

result5=df.sort_values(
    ["Quantity", "Unit Price"],
    ascending=[True, False]
)
print(result5)

df['totalPayment']=df['Unit Price']*df['Quantity']
df.to_csv("ecommerce_sales_dirty_dataset.csv",index=False)
print(df.groupby('Category')['totalPayment'].sum())
print(df.groupby('Payment Method')['totalPayment'].sum())
print(df.groupby('Customer ID')['totalPayment'].sum())

plt.figure(figsize=(15,5))
plt.subplot(1, 3, 1)
x=result2.index
y=result2
plt.xticks(rotation=45)
plt.bar(x,y)

plt.subplot(1, 3, 2)
citycc=df['City'].value_counts()
plt.pie(
    citycc,
    labels=citycc.index,
    autopct="%1.1f%%"
)

plt.subplot(1, 3, 3)
plt.hist(df['Unit Price'])
plt.tight_layout()
plt.show() """