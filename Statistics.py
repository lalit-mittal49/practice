import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

""" a= range(0,100)
my_num=np.random.choice(a,size=1)
for x in range(1,4):
    print("\nEnter number")
    ent_num=int(input())
    if(ent_num>my_num):
        print("Entered number is too high")
    elif(ent_num<my_num):
        print("Entered number is too low")
    elif(ent_num==my_num):
        print('Correct')
        break;
    print("Chances remaining: ",3-x)
    if(x==3):
        print('correct number was',my_num) """

#1
""" df=pd.read_csv('house_details.csv')
print('City: Nominal\nHouse ID: Nominal\nArea: Continous\nbedrooms: discrete\nPrice: Continuous\nAge of house: Continuous')
print(df['Price'].mean())
print(df['Price'].median())
print(df['Bedrooms'].mode())

print(df['Price'].max()-df['Price'].min())
print(df['Price'].var())
print(df['Price'].std())

print(df['Price'].quantile(0.25))
print(df['Price'].quantile(0.50))
print(df['Price'].quantile(0.75))
iqr=df['Price'].quantile(0.75)-df['Price'].quantile(0.25)
print(iqr)
ll=(df['Price'].quantile(0.25))-1.5*iqr
up=(df['Price'].quantile(0.75))+1.5*iqr
outlyer=df[(df['Price']<ll)|(df['Price']>up)]
print(outlyer) """

#2
""" df=pd.read_csv('mobile_app_usage_200.csv')
print('User ID: Nominal\nDaily screen time: Continuous\nNum of apps: Discrete\nAge: Discrete\nSubscription Type: Ordinal\nCity: Nominal')
print(df['dst'].mean())
print(df['dst'].median())
print(df['st'].mode())

print(df['dst'].var())
print(df['dst'].std())

print(np.percentile(df['dst'],10))
print(np.percentile(df['dst'],25))
print(np.percentile(df['dst'],75))
print(np.percentile(df['dst'],95))
ul=((df['dst'].quantile(0.75))+1.5*(df['dst'].quantile(0.75)-df['dst'].quantile(0.25)))
unusual=df[df['dst']>ul]
print(unusual) """

#3
""" df=pd.read_csv('athlete.csv')
print('Athlete: Nominal\nCountry: Nominal\nSport: Nominal\nHeight: Continuous\nWeight: Continuous\nGold Medal: Discrete')
print(df['Age'].mean())
print(df['Height'].median())
print(df['Sport'].mode())

print(df['Weight'].max()-df['Weight'].min())
print(df['Height'].var())
print(df['Age'].std())

print(df['GM'].quantile(0.25))
print(df['GM'].quantile(0.50))
print(df['GM'].quantile(0.75))
iqr=df['GM'].quantile(0.75)-df['GM'].quantile(0.25)
print(iqr)
ul=df['GM'].quantile(0.75)+1.5*iqr
print(df[df['GM']>ul]) """

#4
""" df=pd.read_csv('song.csv')
print(df['Streams'].mean())
print(df['Duration'].median())
print(df['Genre'].mode())

print(df['Duration'].max()-df['Duration'].min())
print(df['Duration'].var())
print(df['Streams'].std())

print(np.percentile(df['Streams'],5))
print(np.percentile(df['Streams'],25))
print(np.percentile(df['Streams'],50))
print(np.percentile(df['Streams'],90))

iqr=df['Streams'].quantile(0.75)-df['Streams'].quantile(0.25)
ul=df['Streams'].quantile(0.75)+1.5*iqr
ll=df['Streams'].quantile(0.25)-1.5*iqr
print(df[(df['Streams']<ll)|(df['Streams']>ul)]) """

#5
""" df=pd.read_csv('wc.csv')
print('House ID: Nominal\nfamily size: Discrete\nDWU: Continuous\nArea: Nominal\nIncome Group: ordinal')
print(df['dwu'].mean())
print(df['dwu'].median())
print(df['dwu'].mode())
print(df['dwu'].max()-df['dwu'].min())
print(df['dwu'].quantile(0.25))
print(df['dwu'].quantile(0.50))
print(df['dwu'].quantile(0.75))
iqr=df['dwu'].quantile(0.75)-df['dwu'].quantile(0.25)
print(iqr)
ul=df['dwu'].quantile(0.75)+1.5*iqr
print(df[df['dwu']>ul]) """

#6
""" df=pd.read_csv('stbatch')
print('Discrete: Interview Score\nContinuous: CGPA, Package')
print(df['Package'].mean())
print(df['Package'].median())
print(df['Company'].mode())

print(df['Package'].var())
print(df['Package'].std())

print(np.percentile(df['Package'],80))
iqr=df['Package'].quantile(0.75)-df['Package'].quantile(0.25)
ul=df['Package'].quantile(0.75)+1.5*iqr
print(df[df['Package']>ul]) """

#7
""" df=pd.read_csv('tckbook.csv')
print('Booking ID: nominal\nMovie: Nominal\nSeat type: Ordinal\nTicket price: Continuous\nNum: Discrete\nBooking Day: Nominal')
print(df['Ticket_Price'].mean())
print(df['Ticket_Price'].median())
print(df['Seat_Type'].mode())

print(df['Ticket_Price'].var())
print(df['Ticket_Price'].std())

print(df['Ticket_Price'].quantile(0.25))
print(df['Ticket_Price'].quantile(0.75))
iqr=df['Ticket_Price'].quantile(0.75)-df['Ticket_Price'].quantile(0.25)
ul=df['Ticket_Price'].quantile(0.75)+1.5*iqr

print(df[df['Ticket_Price']>ul]) """

#8
""" df=pd.read_csv('delivery.csv')
print('Delivery ID: Nominal\nRestaurent: Nominal\nDistance: Continuous\nTime: Continuous\nDP: Nominal\nRating: ordinal')
print(df['Delivery_Time'].mean())
print(df['Distance'].median())
print(df['Restaurant'].mode())
print(df['Distance'].max()-df['Distance'].min())
print(df['Delivery_Time'].var())
print(df['Delivery_Time'].std())

iqr=df['Delivery_Time'].quantile(0.75)-df['Delivery_Time'].quantile(0.25)
ll=df['Delivery_Time'].quantile(0.25)-1.5*iqr
print(df[df['Delivery_Time'<ll]]) """

#9
""" df = pd.read_csv('hotel_bookings.csv')
print('Booking ID: Nominal\nHotel Type: Nominal\nStay Days: Discrete\nRoom Price: Continuous\nGuests: Discrete\nCity: Nominal')

print(df['Room_Price'].mean())
print(df['Room_Price'].median())
print(df['Room_Price'].mode()[0])

print(df['Room_Price'].max() - df['Room_Price'].min())
print(df['Room_Price'].var())
print(df['Room_Price'].std())

print(df['Room_Price'].quantile(0.20))
print(df['Room_Price'].quantile(0.50))
print(df['Room_Price'].quantile(0.95))

iqr = df['Room_Price'].quantile(0.75) - df['Room_Price'].quantile(0.25)
ul = df['Room_Price'].quantile(0.75) + 1.5 * iqr
print(df[df['Room_Price'] > ul]) """

#10
""" df = pd.read_csv('daily_electricity.csv')

print(df['Units_Consumed'].mean())
print(df['Units_Consumed'].median())
print(df['City'].mode())

print(df['Units_Consumed'].max() - df['Units_Consumed'].min())
print(df['Units_Consumed'].var())
print(df['Units_Consumed'].std())

iqr = df['Units_Consumed'].quantile(0.75) - df['Units_Consumed'].quantile(0.25)
ll = df['Units_Consumed'].quantile(0.25) - 1.5 * iqr
ul = df['Units_Consumed'].quantile(0.75) + 1.5 * iqr
print(df[(df['Units_Consumed'] < ll) | (df['Units_Consumed'] > ul)]) """

#11
""" df = pd.read_csv('flights_250.csv')

print('Flight: Nominal\nAirline: Nominal\nDelay Minutes: Continuous\nDestination: Nominal\nTicket Class: Ordinal')

print(df['Delay_Minutes'].mean())
print(df['Delay_Minutes'].median())
print(df['Delay_Minutes'].mode()[0])

print(df['Delay_Minutes'].max() - df['Delay_Minutes'].min())
print(df['Delay_Minutes'].var())
print(df['Delay_Minutes'].std())

print(df['Delay_Minutes'].quantile(0.25)) 
print(df['Delay_Minutes'].quantile(0.50)) 
print(df['Delay_Minutes'].quantile(0.75))
print(df['Delay_Minutes'].quantile(0.95)) 

iqr = df['Delay_Minutes'].quantile(0.75) - df['Delay_Minutes'].quantile(0.25)
ul = df['Delay_Minutes'].quantile(0.75) + 1.5 * iqr
print(df[df['Delay_Minutes'] > ul]) """

#12
""" df = pd.read_csv('crypto_150.csv')

print('Coin: Nominal\nMarket Cap: Continuous\nDaily Return: Continuous\nTrading Volume: Continuous\nCategory: Nominal')

print(df['Daily_Return'].mean())
print(df['Market_Cap'].median())
print(df['Category'].mode()[0])

print(df['Daily_Return'].var())
print(df['Daily_Return'].std())

iqr = df['Daily_Return'].quantile(0.75) - df['Daily_Return'].quantile(0.25)
ll = df['Daily_Return'].quantile(0.25) - 1.5 * iqr
ul = df['Daily_Return'].quantile(0.75) + 1.5 * iqr
print(df[(df['Daily_Return'] < ll) | (df['Daily_Return'] > ul)]) """

#13
""" df=pd.read_csv('wildlife.csv')
print('Animal: Nominal\nSpecies: Nominal\nWeight: Continuous\nAge: Discrete\nForest: Nominal')
print(df['Weight'].mean())
print(df['Weight'].median())
print(df['Weight'].mode)

print(df['Weight'].max()-df['Weight'].min())
print(df['Weight'].var())
print(df['Weight'].std())

print(df['Weight'].quantile(0.25))
print(df['Weight'].quantile(0.50))
print(df['Weight'].quantile(0.75))

iqr=df['Weight'].quantile(0.75)-df['Weight'].quantile(0.25)
ul=df['Weight'].quantile(0.75)+1.5*iqr
print(df[df['Weight']>ul]) """

#14
""" df=pd.read_csv('influencer.csv')
print(df['Followers'].mean())
print(df['Engagement_Rate'].median())
print(df['Platform'].mode())

print(df['Engagement_Rate'].var())
print(df['Engagement_Rate'].std())
print(np.percentile((df['Engagement_Rate'],90)))

iqr=df['Engagement_Rate'].quantile(0.75)-df['Engagement_Rate'].quantile(0.25)
ul=df['Engagement_Rate'].quantile(0.75)+1.5*iqr
ll=df['Engagement_Rate'].quantile(0.25)-1.5*iqr
print(df[(df['Engagement_Rate']>ul)|(df['Engagement_Rate']<ll)])
print('No they are not') """

#15
""" df=pd.read_csv('mars.csv')
print('Reading ID: Nominal\nTemp: Continuous\nPressure: Continuous\nBattery_level: Discrete\nTerrain: Nominal\nSignal Strength: Ordinal')

print(df['temp'].mean())
print(df['temp'].median())
print(df['Terrain_Type'].mode())

print(df['Pressure'].max()-df['Pressure'].min())
print(df['Pressure'].var())
print(df['Pressure'].std())

print(df['temp'].quantile(0.25))
print(df['temp'].quantile(0.50))
print(df['temp'].quantile(0.75))
iqr=df['temp'].quantile(0.75)-df['temp'].quantile(0.25)
print(iqr)
print(np.percentile(df['Pressure'],10))
print(np.percentile(df['Pressure'],90))

plt.boxplot(df['temp'])
plt.show()

iqr=df['temp'].quantile(0.75)-df['temp'].quantile(0.25)
ul=df['temp'].quantile(0.75)+1.5*iqr
ll=df['temp'].quantile(0.25)-1.5*iqr
print(ul)
print(ll) """