from google.colab import drive
drive.mount('/content/drive')
file_path = '/content/desktop/mccp/supply_chain_sample_data.csv'  # Adjust this path
df = pd.read_csv(file_path)

# Display the first few rows of the data to verify it's loaded correctly
print(df.head())
