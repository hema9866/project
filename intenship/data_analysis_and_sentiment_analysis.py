import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Define the function for API request
def analyze_sentiment(text):
    # API URL and headers
    api_url = "https://api.example.com/sentiment"
    headers = {
        "Authorization": "Bearer eb865677d8e5403a9243cf0941fca679",
        "Content-Type": "application/json"
    }
    data = {"text": text}
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['label']
    else:
        return "Error"

# Load the data
file_path = 'supply_chain_data.csv'  # Adjust path
df = pd.read_csv(file_path)

# Apply sentiment analysis to the text column
df['sentiment'] = df['text_column'].apply(analyze_sentiment)

# Visualize sentiment distribution
sentiment_counts = df['sentiment'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
