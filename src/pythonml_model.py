from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

def train_ml_model(data):
    """Trains a machine learning model to detect suspicious transactions."""
    X = data.drop(columns=['is_suspicious'])
    y = data['is_suspicious']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    return model

if __name__ == "__main__":
    data = pd.read_csv("data/processed/labeled_transactions.csv")
    model = train_ml_model(data)
