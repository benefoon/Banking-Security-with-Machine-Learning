import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_file_path(file_path):
    """Validates the existence of the file path."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    if not file_path.endswith('.csv'):
        raise ValueError("The input file must be a CSV file.")

def ensure_directory(directory):
    """Ensures that a directory exists."""
    if not os.path.exists(directory):
        logging.info(f"Creating directory: {directory}")
        os.makedirs(directory)

def clean_data(file_path):
    """Cleans raw transaction data."""
    logging.info(f"Reading data from {file_path}")
    data = pd.read_csv(file_path)
    logging.info("Dropping missing values")
    data.dropna(inplace=True)
    logging.info("Converting amounts to absolute values")
    data['amount'] = data['amount'].apply(lambda x: abs(x))
    return data

def detect_outliers(data, column, threshold=3):
    """Detects outliers in a dataset using z-score."""
    logging.info(f"Detecting outliers in column '{column}'")
    data['z_score'] = (data[column] - data[column].mean()) / data[column].std()
    outliers = data.loc[data['z_score'].abs() > threshold]
    logging.info(f"Number of outliers detected: {len(outliers)}")
    return outliers

if __name__ == "__main__":
    try:
        input_file = "data/raw/transactions.csv"
        validate_file_path(input_file)
        ensure_directory("data/processed")
        
        raw_data = clean_data(input_file)
        outliers = detect_outliers(raw_data, "amount")
        
        raw_data.to_csv("data/processed/cleaned_transactions.csv", index=False)
        outliers.to_csv("data/processed/outliers.csv", index=False)
        logging.info("Processing completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
