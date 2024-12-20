def feature_engineering(data):
    """Create new features for machine learning."""
    data['hour'] = pd.to_datetime(data['time']).dt.hour  # Extract hour of transaction
    data['day_of_week'] = pd.to_datetime(data['time']).dt.dayofweek  # Extract day of week
    data['is_high_amount'] = (data['amount'] > 10000).astype(int)  # Flag high transactions
    return data

# Apply feature engineering
data = pd.read_csv("data/processed/cleaned_transactions.csv")
data = feature_engineering(data)
data.to_csv("data/processed/featured_transactions.csv", index=False)
print("Feature engineering complete. File saved to 'data/processed/featured_transactions.csv'.")
