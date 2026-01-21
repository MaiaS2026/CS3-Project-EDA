import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

df_coffee = pd.read_csv('Coffe_sales.csv')

# SPLIT BAR CHART
print(df_coffee.info())
df = pd.read_csv('Coffe_sales.csv')

df_sorted = df.sort_values(by='money', ascending=False)
colors = ['#006884', '#a9c7ee', '#9ED7E6', '#7AA2C4']
plt.bar(df_sorted['Time_of_Day'], df_sorted['money'], color=colors, width=0.6)

plt.xticks(rotation=45)
plt.xlabel('Time of Day')
plt.ylabel('Money Spent')
plt.title('Money spent vs Time of Day')

plt.savefig('barchart.png', bbox_inches='tight')
plt.close()

# WORDCLOUD
name_series = df['coffee_name']
name_list = name_series.values
names = Counter(name_list)

wordcloud = WordCloud(width=800, height=400, background_color='beige', colormap='copper').generate_from_frequencies(names)
plt.figure(figsize=(6, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

plt.savefig('wordcloud.png', bbox_inches='tight')
plt.close()

print (df["coffee_name"].value_counts())

# SPAGHETTI PLOT
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14), 'y10': np.random.randn(10)+range(2,12) })
 
# Create a color palette
palette = plt.get_cmap('Set1')
 
# Plot multiple lines
num=0
for column in df.drop('x', axis=1):
    num+=1
    plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)

# Add legend
plt.legend(loc=2, ncol=2)
 
# Add titles
plt.title("Coffee Type vs Time of Day Ordered", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Time")
plt.ylabel("Coffee Ordered")

# Show the graph
plt.savefig('spahgetti.png', bbox_inches='tight')
