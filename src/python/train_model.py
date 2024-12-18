import joblib
from sklearn.ensemble import IsolationForest
from preprocess import preprocess_data

def train_anomaly_detection_model(file_path):
    X_train, _, _, _ = preprocess_data(file_path)

    # Initialize the model
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)

    # Train the model
    model.fit(X_train)

    # Save the model
    joblib.dump(model, '../models/anomaly_detection_model.pkl')
    print("Model training and saving complete.")

if __name__ == "__main__":
    train_anomaly_detection_model('../data/sample_data.csv')
