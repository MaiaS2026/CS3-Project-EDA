import pandas as pd
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

# Often need to rotate labels on x axis for readability
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