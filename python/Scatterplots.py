import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('first_scatter.csv')
df2 = pd.read_csv('second_scatter.csv')


y = df['emissions_avg']
y2 = df2['avg_yields']

x = df['temperatures_avg']


plt.figure(figsize=(8,6))

plt.scatter(x,y)
plt.ylabel("Average Emissions (kt)")
plt.xlabel("Average Temperatures (\u00b0 C)")
plt.title("Average Total Emissions vs Average Changes in Temperature", loc = 'center')

plt.figure(figsize=(8,6))

plt.scatter(x,y2)
plt.ylabel("Average Yields (kg/ha)")
plt.xlabel("Average Temperatures (\u00b0 C)")
plt.title("Average Yields vs Average Changes in Temperature", loc = 'center')

plt.figure(figsize=(8,6))

plt.scatter(y,y2)
plt.ylabel("Average Yields (kg/ha)")
plt.xlabel("Average Total Emissions (kt)")
plt.title("Average Yields vs Average Total Emissions", loc = 'center')
