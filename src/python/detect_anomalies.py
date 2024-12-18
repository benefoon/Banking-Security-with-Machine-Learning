import joblib
import pandas as pd

def detect_anomalies(file_path):
    # Load the trained model
    model = joblib.load('../models/anomaly_detection_model.pkl')

    # Load the data
    data = pd.read_csv(file_path)
    X = data.drop(columns=['label'])

    # Predict anomalies
    predictions = model.predict(X)

    # Add predictions to the data
    data['anomaly'] = predictions
    data['anomaly'] = data['anomaly'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')

    # Save results
    data.to_csv('../data/detection_results.csv', index=False)
    print("Anomaly detection complete. Results saved.")

if __name__ == "__main__":
    detect_anomalies('../data/sample_data.csv')
