import seaborn as sns
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1
""" df=pd.read_csv('airport_traffic.csv')
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull())
df=df.dropna()
df=df.drop_duplicates()
df.to_csv('airport_traffic.csv',index=False)

plt.figure(figsize=(25,10))

plt.subplot(2, 3, 1)
sns.scatterplot(
    data=df,
    x='Flight_Duration',
    y='Ticket_Price',
    hue=df['Travel_Class']
)
plt.xticks(rotation=0)

avgtp=df.groupby('Airline')['Ticket_Price'].mean()
plt.subplot(2, 3, 2)
sns.lineplot(
    x=avgtp.index,
    y=avgtp
)
plt.xticks(rotation=90)

avgd=df.groupby('Airline')['Delay_Minutes'].mean()
print(avgd)
plt.subplot(2, 3, 3)
sns.barplot(
    x=avgd.index,
    y=avgd
)
plt.xticks(rotation=90)

plt.subplot(2, 3, 4)
sns.boxplot(
    x=df['Travel_Class'],
    y=df['Delay_Minutes']
)
plt.xticks(rotation=90)

plt.subplot(2, 3, 5)
sns.histplot(
    x=df['Ticket_Price'],
    bins=30
)


plt.tight_layout()
plt.show()

print(df.groupby('Airline')['Ticket_Price'].max().sort_values(ascending=False))
print(df.groupby('Travel_Class')['Delay_Minutes'].mean().sort_values(ascending=False))
print(df.groupby('Destination_City')['Passenger_ID'].nunique().sort_values(ascending=False)) """

#2
""" df=pd.read_csv('ev_charging.csv')
print(df.isnull())
print(df.duplicated())
print(df.isnull().sum())
df=df.dropna()
df=df.drop_duplicates()
df.to_csv('ev_charging.csv',index=False)

plt.figure(figsize=(15,10))

plt.subplot(231)
sns.scatterplot(
    data=df,
    x='Energy_Consumed',
    y='Charging_Time',
    hue='Charging_Type'
)

plt.subplot(232)
data=df.groupby('City')['Energy_Consumed'].mean()
sns.lineplot(
    x=data.index,
    y=data
)
plt.xticks(rotation=90)

plt.subplot(233)
data=df.groupby('City')["Cost"].sum()
sns.barplot(
    x=data.index,
    y=data
)
plt.xticks(rotation=90)

plt.subplot(234)
sns.boxplot(
    data=df,
    x='Charging_Type',
    y='Cost',
)

plt.subplot(235)
sns.histplot(
    x=df['Charging_Time']
)

plt.tight_layout()
plt.show()

print(df.groupby('City')['Cost'].sum().sort_values(ascending=False))
print(df.groupby('Vehicle_Type')["Charging_Time"].mean().sort_values(ascending=False))
print(df['Charging_Type'].value_counts().sort_values(ascending=False).head(1)) """

#3
""" dtdf=pd.read_csv('farm_data.csv')
print(dtdf.describe())
print(dtdf.info())
print(dtdf.isnull().sum())
print(dtdf.duplicated())
df=dtdf.drop_duplicates().dropna()
df.to_csv('farm_data.csv',index=False)

plt.figure(figsize=(15,10))
plt.subplot(231)
sns.scatterplot(
    x=df['Rainfall'],
    y=df['Yield'],
    hue=df['Crop']
)

plt.subplot(232)
data=df.groupby('State')['Yield'].mean()
sns.lineplot(
    y=data,
    x=data.index
)
plt.xticks(rotation=90)

plt.subplot(233)
data=df.groupby('Crop')['Yield'].mean()
sns.barplot(
    x=data.index,
    y=data
)
plt.xticks(rotation=90)

plt.subplot(234)
sns.boxplot(
    x=df['Crop'],
    y=df['Yield']
)
plt.xticks(rotation=90)

plt.subplot(235)
sns.histplot(
    data=df['Rainfall']
)

plt.subplot(236)
sns.barplot(
    x=df['Rainfall'].sort_values(ascending=False),
    y=df['Yield']
)
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

print(df.groupby('Crop')['Yield'].sum().sort_values(ascending=False))
print(df.groupby('State')['Yield'].mean().sort_values(ascending=False))
print('No') """

#4
""" dtdf=pd.read_csv('online_courses.csv')
print(dtdf.describe())
print(dtdf.isnull().sum())
print(dtdf.isnull())
print(dtdf.info())
df=dtdf.dropna().drop_duplicates()
df.to_csv('online_courses.csv',index=False)

plt.figure(figsize=(15,10))
plt.subplot(231)
sns.scatterplot(
    x=df['Hours_Studied'],
    y=df['Quiz_Score'],
    hue=df['Device']
)

plt.subplot(232)
data=df.groupby('Course')['Quiz_Score'].mean()
sns.lineplot(
    x=data.index,
    y=data
)
plt.xticks(rotation=90)

plt.subplot(233)
sns.barplot(
    x=df['Course'],
    y=df['Completion_Percentage']
)
plt.xticks(rotation=90)

plt.subplot(234)
sns.boxplot(
    x=df['Device'],
    y=df['Quiz_Score']
)
plt.xticks(rotation=90)

plt.subplot(235)
sns.histplot(
    data=df['Hours_Studied']
)

plt.tight_layout()
plt.show()

print(df.groupby('Course')['Completion_Percentage'].max().sort_values(ascending=False))
print(df['Device'].value_counts().sort_values(ascending=False))
print(df.groupby('Country')['Quiz_Score'].mean().sort_values(ascending=False)) """

#5
""" dtdf=pd.read_csv('space_missions.csv')
print(dtdf.info())
print(dtdf.describe())
print(dtdf.duplicated())
print(dtdf.isnull().sum())
df=dtdf.dropna().drop_duplicates()
df.to_csv('space_missions.csv',index=False)

plt.figure(figsize=(15,10))
plt.subplot(231)
sns.scatterplot(
    x=df['Payload_Weight'],
    y=df['Mission_Cost'],
    hue=df['Success']
)

plt.subplot(232)
result=df['Launch_Year'].value_counts()
sns.lineplot(
    x=result.index,
    y=result
)

plt.subplot(233)
result1=df.groupby('Country')['Mission_Cost'].mean()
sns.barplot(
    x=result1.index,
    y=result1
)
plt.xticks(rotation=90)

plt.subplot(234)
sns.boxplot(
    x=df['Rocket_Type'],
    y=df['Payload_Weight']
)
plt.xticks(rotation=90)

plt.subplot(235)
sns.histplot(
    data=df['Mission_Cost']
)

plt.tight_layout()
plt.show()

valuecc = df.groupby('Country')['Success'].value_counts()
print(valuecc)
print(df.groupby("Country")['Mission_Cost'].mean().sort_values(ascending=False))
print(df.groupby('Rocket_Type')['Payload_Weight'].max().sort_values(ascending=False))
print(df['Success'=='Yes'].groupby(df['Country'].mean())*100) """