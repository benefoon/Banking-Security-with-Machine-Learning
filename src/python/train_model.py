
def train_anomaly_detection_model(file_path, model_output_path, contamination=0.1, random_state=42):
    """
    Trains an anomaly detection model and saves it.

    Args:
        file_path (str): Path to the dataset file.
        model_output_path (str): Path to save the trained model.
        contamination (float): Proportion of anomalies in the dataset (default: 0.1).
        random_state (int): Random seed for reproducibility (default: 42).
    """
    # Validate input file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file '{file_path}' does not exist.")

    # Preprocess data
    X_train, _, _, _ = preprocess_data(file_path)

    # Initialize the model
    model = IsolationForest(n_estimators=100, contamination=contamination, random_state=random_state)

    # Train the model
    model.fit(X_train)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)

    # Save the model
    joblib.dump(model, model_output_path)
    print(f"Model training complete. Saved to {model_output_path}.")

if __name__ == "__main__":
    train_anomaly_detection_model('../data/sample_data.csv', '../models/anomaly_detection_model.pkl')
