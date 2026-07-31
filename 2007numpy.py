import csv
import numpy as np
import pandas as pd

#1
""" import numpy as np
arr = np.array([4,2,5,1,3,6,1,4,2,2])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr)) """

#2
""" import numpy as np
arr=np.arange(1,101)
print(arr)
reshaped=arr.reshape(10,10)
print(reshaped)
print(reshaped[0])
print(reshaped[9]) """

#3
""" import pandas as pd
distances=pd.Series([100,45,145,78,91],index=["Mercury","Venus","Earth","Mars","Jupiter"])
print(distances)
print(distances["Earth"])
print(distances[:3]) """

#4
""" water_data = [2.5, 3.0, 2.2, 3.5, 2.8, 3.1, 2.9]

with open("water_log.txt", "w") as file:
    for day_num, liters in enumerate(water_data, start=1):
        file.write(f"Day {day_num}: {liters} L\n")

# Read and display each day's intake
with open("water_log.txt", "r") as file:
    content = file.read()
    print(content)"""

#5
""" import numpy as np
arr=np.arange(1,37)
reshaped= arr.reshape(6,6)
print(reshaped.shape)
print(reshaped.size)
print(reshaped.ndim) """

#6
""" import numpy as np
prices=np.array([12000,54000,87000,23000,90000,45000,13000,87000,45000,65000,10000,13000])
print(np.max(prices))
print(np.min(prices))
print(np.mean(prices))
print(np.std(prices))
print(prices[prices>30000]) """

#7
""" import numpy as np
arr=np.arange(1001,1101)
reshaped=arr.reshape(10,10)
print(f'{reshaped}\n')
print(f'rows: \n{reshaped[::2, :]}\n')
print(f'columns: \n{reshaped[ :, ::2]}\n') """

#8
""" import numpy as np
bed_available=np.random.choice([True,False],size=100)
vacant_count=np.sum(bed_available)
occ_count=np.sum(~bed_available)
print(f'Vacant: {vacant_count}')
print(f'Occupied: {occ_count}')
print(f'Available beds: {np.where(bed_available)}') """

#9
""" import pandas as pd
ratings=pd.Series([1,5,2,4,9,6,7,4,1,3])
print(ratings.max())
print(ratings.min())
print(ratings.mean())
print(ratings[ratings>4]) """

#10
""" with open("electricity.csv",'w+') as file:
    writer=csv.writer(file)
    writer.writerows([
        ["House no","units"],
        [123,950],[121,600],[122,605],[124,300]
    ])
df_csv=pd.read_csv("electricity.csv")
print(df_csv["units"].sum())
print(df_csv["units"].mean())
print(df_csv["units"].max())
print(df_csv["units"].min())"""

#11
""" import numpy as np
passData=np.array([[1,300],[2,124],[3,450],[4,200],[5,351],[6,100],[7,900]])
print(np.sum(passData[:,1]))
busiest=np.argmax(passData[:,1])
print(f'Day : {passData[busiest,0]} is busiest')
least=np.argmin(passData[:,1])
print(f'Day : {passData[least,0]} is least busy')
avgPass=np.mean(passData[:,1])
print(avgPass)
abvAvg=passData[passData[:,1]>avgPass,0]
print(f'Days above average no. of passengers : {abvAvg}') """

#12
""" import numpy as np
steps=np.random.randint(low=5000,high=90000,size=30)
print(np.max(steps))
print(np.min(steps))
print(np.mean(steps))
print(np.median(steps))
print(np.std(steps))
days=(np.where(steps>10000))+1
print(days) """

#13
""" import numpy as np
low=5000
high=90001
step=5000
prices=np.arange(low,high,step)
roomMatrix=np.random.choice(prices,size=30)
reshaped=roomMatrix.reshape(5,6)
print(reshaped)
print(np.sum(reshaped))
expensive=np.max(reshaped)
rooms=np.argwhere(reshaped==expensive)
print(f'Most expensive rooms : \n{rooms}')
cheap=np.min(reshaped)
print(f'Cheapest rooms :\n{np.argwhere(reshaped==cheap)}')
print(f"revenue per floor:\n{np.sum(reshaped,axis=1)}")
print(f"revenue per room type:\n{np.sum(reshaped,axis=0)}") """

#14
""" import numpy as np
low = 10
high = 50
temp=np.arange(low,high)
daystemp=np.random.choice(temp,size=15)
print(daystemp)
print(f'Days above 35°C: {(np.argwhere(daystemp>35))+1}')
print(f'Days below 20°C: {(np.argwhere(daystemp<20))+1}')
print(f'Temperatures between 25°C and 30°C: {daystemp[(25<daystemp) & (daystemp<30)]}') """

#15
""" with open("medal.csv",'+w') as file:
    writer=csv.writer(file)
    writer.writerows([
        ['Country','Gold','Silver','Bronze'],
        ["India",10,12,14],
        ['china',4,7,0],
        ['pakistan',0,1,0],
        ['america',5,6,3]
    ])
df_csv=pd.read_csv('medal.csv')
print(df_csv.sum(axis=1,numeric_only=True)) """

#16
""" import numpy as np
runs_scored = np.array([185, 142, 210, 168, 195, 120, 175, 160, 205, 150, 188, 172, 190, 165])
runs_conceded = np.array([160, 145, 190, 170, 180, 155, 160, 165, 198, 140, 170, 180, 175, 160])

print(f"Highest Score: {np.max(runs_scored)}")
print(f"Lowest Score: {np.min(runs_scored)}")
print(f"Average Score: {np.mean(runs_scored)}")

net_run_diff = np.sum(runs_scored) - np.sum(runs_conceded)
print(f"Net Run Difference: {net_run_diff}")

avg_score = np.mean(runs_scored)
above_avg_matches = np.where(runs_scored > avg_score)[0] + 1
print(f"Matches above average score: {above_avg_matches}") """

#17
""" import numpy as np
np.random.seed(42)  # For reproducible sample data
aqi = np.random.randint(20, 180, size=30)
print(f"AQI Values: {aqi}")

good_days = np.sum(aqi < 50)
moderate_days = np.sum((aqi >= 50) & (aqi <= 100))
poor_days = np.sum(aqi > 100)

print(f"Good Days (<50): {good_days}")
print(f"Moderate Days (50-100): {moderate_days}")
print(f"Poor Days (>100): {poor_days}") """

#18
""" import numpy as np
np.random.seed(10)
marks = np.random.randint(35, 100, size=50)

avg_marks = np.mean(marks)
print(f"Class Average: {avg_marks:.2f}")
print(f"Median: {np.median(marks)}")
print(f"Standard Deviation: {np.std(marks):.2f}")

print(f"Students Above Average: {np.sum(marks > avg_marks)}")
print(f"Students Below Average: {np.sum(marks < avg_marks)}")

sorted_marks = np.sort(marks)
print(f"Top 10 Students Marks: {sorted_marks[-10:][::-1]}")
print(f"Bottom 10 Students Marks: {sorted_marks[:10]}") """

#19
""" import csv
import numpy as np
import pandas as pd

with open("fuel_sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows([
        ["Date", "Petrol Sold", "Diesel Sold"],
        ["2026-07-01", 1200, 1500],
        ["2026-07-02", 1400, 1350],
        ["2026-07-03", 1100, 1600],
        ["2026-07-04", 1550, 1700],
        ["2026-07-05", 950, 1100]
    ])

df_fuel = pd.read_csv("fuel_sales.csv")

petrol = df_fuel["Petrol Sold"].to_numpy()
diesel = df_fuel["Diesel Sold"].to_numpy()
dates = df_fuel["Date"].to_numpy()
total_daily = petrol + diesel

print(f"Total Petrol Sold: {np.sum(petrol)}")
print(f"Total Diesel Sold: {np.sum(diesel)}")

max_day_idx = np.argmax(total_daily)
min_day_idx = np.argmin(total_daily)

print(f"Highest Sales Day: {dates[max_day_idx]} ({total_daily[max_day_idx]} L)")
print(f"Lowest Sales Day: {dates[min_day_idx]} ({total_daily[min_day_idx]} L)")
print(f"Average Daily Sales: {np.mean(total_daily):.2f} L") """

#20
""" import numpy as np
np.random.seed(7)
temps = np.random.uniform(-50.0, 40.0, size=24)

print(f"Max Temp: {np.max(temps):.2f}°C")
print(f"Min Temp: {np.min(temps):.2f}°C")

avg_temp = np.mean(temps)
print(f"Average Temp: {avg_temp:.2f}°C")

print(f"Temps Above Avg: {np.round(temps[temps > avg_temp], 1)}")
print(f"Temps Below Avg: {np.round(temps[temps < avg_temp], 1)}")

reshaped_temps = temps.reshape(6, 4)
print(f"\nReshaped Array (6x4):\n{np.round(reshaped_temps, 1)}")

row_avg = np.mean(reshaped_temps, axis=1)
col_avg = np.mean(reshaped_temps, axis=0)

print(f"\nRow-wise Averages (axis=1): {np.round(row_avg, 1)}")
print(f"Col-wise Averages (axis=0): {np.round(col_avg, 1)}")

flattened = reshaped_temps.flatten()
rounded_temps = np.round(flattened, 1)
unique_temps = np.unique(rounded_temps)

print(f"\nFlattened & Rounded: {rounded_temps}")
print(f"Unique Temp Values: {unique_temps}") """