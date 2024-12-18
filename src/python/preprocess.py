import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(file_path):
    # Load dataset
    data = pd.read_csv(file_path)

    # Handle missing values
    data = data.dropna()

    # Extract features and labels
    X = data.drop(columns=['label'])  # Assuming 'label' column exists
    y = data['label']

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data('../data/sample_data.csv')
    print("Data preprocessing complete.")
