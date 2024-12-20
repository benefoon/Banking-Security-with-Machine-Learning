def flag_suspicious_transactions(file_path):
    """Flag suspicious transactions based on basic thresholds."""
    data = pd.read_csv(file_path)
    suspicious = data[data['amount'] > 15000]  # Example: flag transactions over $15,000
    suspicious.to_csv("data/processed/suspicious_transactions.csv", index=False)
    print("Suspicious transactions saved to 'data/processed/suspicious_transactions.csv'.")

# Flag suspicious transactions
flag_suspicious_transactions("data/processed/featured_transactions.csv")
