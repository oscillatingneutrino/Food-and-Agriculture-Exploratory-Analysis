import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('first_scatter.csv')
df2 = pd.read_csv('second_scatter.csv')
df3 = pd.read_csv('third_scatter.csv')


y = 'emissions_avg'
y2 = 'avg_yields'

x = 'temperatures_avg'

colors = {'Canada': 'red', 'Mexico': 'mediumaquamarine', 'United States of America': 'dodgerblue'}


plt.figure(figsize=(8,6))

for Country, group in df.groupby('Country'):
    plt.scatter(group[x],group[y], color = colors[Country], label = Country)


#plt.scatter(x,y)
plt.ylabel("Average Emissions (kt)")
plt.xlabel("Average Temperature Change (\u00b0 C)")
plt.title("Average Total Emissions vs Average Changes in Temperature", loc = 'center')
plt.legend()
plt.grid(True)


plt.figure(figsize=(8,6))

for Country, group in df2.groupby('Country'):
    plt.scatter(group[x],group[y2], color = colors[Country], label = Country)

#plt.scatter(x,y2)
plt.ylabel("Average Yields (kg/ha)")
plt.xlabel("Average Temperature Change (\u00b0 C)")
plt.title("Average Yields vs Average Changes in Temperature", loc = 'center')
plt.legend()
plt.grid(True)

plt.figure(figsize=(8,6))

for Country, group in df3.groupby('Country'):
    plt.scatter(group[y],group[y2], color = colors[Country], label = Country)


#plt.scatter(y,y2)
plt.ylabel("Average Yields (kg/ha)")
plt.xlabel("Average Total Emissions (kt)")
plt.title("Average Yields vs Average Total Emissions", loc = 'center')
plt.legend()
plt.grid(True)
