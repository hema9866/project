import pandas as pd
#Mount Google Drive


# Replace the path with your actual file path in Google Drive
file_path = '/content/desktop/mccp/supply_chain_sample_data.csv'  # Adjust this path
df = pd.read_csv(file_path)

# Display the first few rows of the data to verify it's loaded correctly
print(df.head())
import schedule
import time

# Function to run the sentiment analysis job
def run_analysis():
    # Reload data, perform sentiment analysis, and visualize results
    df = pd.read_csv(file_path)  # Re-read the file if it's updated
    df['sentiment'] = df['text_column'].apply(analyze_sentiment)
    
    # Visualize the updated sentiment analysis
    sentiment_counts = df['sentiment'].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
    plt.title('Sentiment Distribution of Global Supply Chain Data')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

# Schedule the analysis to run every day at 9 AM
schedule.every().day.at("09:00").do(run_analysis)

# Keep the script running to check and run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
