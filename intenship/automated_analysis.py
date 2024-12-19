import schedule
import time
from data_analysis_and_sentiment_analysis import analyze_sentiment, df

def job():
    print("Running sentiment analysis job...")

    # Re-load the data (if updated) and apply sentiment analysis
    df = pd.read_csv('supply_chain_data.csv')  # Adjust path
    df['sentiment'] = df['text_column'].apply(analyze_sentiment)

    # Visualize sentiment analysis result
    sentiment_counts = df['sentiment'].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

# Schedule to run daily at 9 AM
schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
