def clean_transaction_data(file_path):
    """Clean raw transaction data."""
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)  # Remove missing values
    data = data[data['amount'] > 0]  # Remove transactions with invalid amounts
    data['time'] = pd.to_datetime(data['time'])  # Convert time to datetime
    return data

# Clean data
cleaned_data = clean_transaction_data("data/raw/generated_transactions.csv")
cleaned_data.to_csv("data/processed/cleaned_transactions.csv", index=False)
print("Cleaned data saved to 'data/processed/cleaned_transactions.csv'.")
