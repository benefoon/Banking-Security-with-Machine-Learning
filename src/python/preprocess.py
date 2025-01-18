import pandas as pd
from sklearn.model_selection import train_test_split
import os

def preprocess_data(file_path, test_size=0.3, random_state=42):
    """
    Preprocesses the data for model training and testing.

    Args:
        file_path (str): Path to the input CSV file.
        test_size (float): Proportion of data to be used for testing (default: 0.3).
        random_state (int): Random seed for reproducibility (default: 42).

    Returns:
        tuple: X_train, X_test, y_train, y_test
    """
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file '{file_path}' does not exist.")

    # Load dataset
    data = pd.read_csv(file_path)

    # Ensure 'label' column exists
    if 'label' not in data.columns:
        raise ValueError("The dataset must contain a 'label' column.")

    # Handle missing values
    data = data.dropna()

    # Extract features and labels
    X = data.drop(columns=['label'])
    y = data['label']

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    input_file = '../data/sample_data.csv'

    try:
        X_train, X_test, y_train, y_test = preprocess_data(input_file)
        print("Data preprocessing complete.")
    except Exception as e:
        print(f"Error during preprocessing: {e}")
