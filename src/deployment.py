import joblib

def save_model(model, filename):
    # Save the trained model using joblib
    joblib.dump(model, filename)
    print(f"Model saved as {filename}")

def load_model(filename):
    # Load the saved model
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    return model
