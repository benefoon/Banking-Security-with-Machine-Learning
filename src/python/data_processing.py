import pandas as pd

def clean_data(file_path):
    """Cleans raw transaction data."""
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    data['amount'] = data['amount'].apply(lambda x: abs(x))
    return data

def detect_outliers(data, column, threshold=3):
    """Detects outliers in a dataset using z-score."""
    mean = data[column].mean()
    std = data[column].std()
    data['z_score'] = (data[column] - mean) / std
    return data[data['z_score'].abs() > threshold]

if __name__ == "__main__":
    raw_data = clean_data("data/raw/transactions.csv")
    outliers = detect_outliers(raw_data, "amount")
    raw_data.to_csv("data/processed/cleaned_transactions.csv", index=False)
    outliers.to_csv("data/processed/outliers.csv", index=False)
