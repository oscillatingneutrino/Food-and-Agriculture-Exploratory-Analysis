import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('first_scatter.csv')

y = df['emissions_avg']

x = df['temperatures_avg']


plt.figure(figsize=(8,6))

plt.scatter(x,y)
plt.ylabel("Average Emissions (kt)")
plt.xlabel("Average Temperatures (\u00b0 C)")
plt.title("Average Total Emissions vs Average Changes in Temperature", loc = 'center')
