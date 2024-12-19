# Assuming 'text_column' contains the text data for sentiment analysis
df['sentiment'] = df['text_column'].apply(analyze_sentiment)

# Show the first few rows with the sentiment column added
print(df[['text_column', 'sentiment']].head())

import matplotlib.pyplot as plt
import seaborn as sns

# Count the occurrences of each sentiment
sentiment_counts = df['sentiment'].value_counts()

# Plot the sentiment distribution
plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
plt.title('Sentiment Distribution of Global Supply Chain Data')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
