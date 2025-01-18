import joblib
import pandas as pd
import os

def detect_anomalies(file_path, model_path, output_path):
    """Detects anomalies using a pre-trained model and saves the results."""
    # Validate file paths
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file '{file_path}' not found.")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file '{model_path}' not found.")

    # Load the trained model
    model = joblib.load(model_path)

    # Load the data
    data = pd.read_csv(file_path)
    if 'label' not in data.columns:
        raise ValueError("Input data must contain a 'label' column.")
    X = data.drop(columns=['label'])
  
 # Predict anomalies
    predictions = model.predict(X)

    # Add predictions to the data
    data['anomaly'] = predictions
    data['anomaly'] = data['anomaly'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')

    # Save results
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Anomaly detection complete. Results saved to {output_path}.")

if __name__ == "__main__":
    detect_anomalies('../data/sample_data.csv', '../models/anomaly_detection_model.pkl', '../data/detection_results.csv')
