import joblib

def save_model(model, filename):
    """
    Save the trained model to a file using joblib for later deployment.
    """
    joblib.dump(model, filename)
    print(f"Model saved as {filename}")

def load_model(filename):
    """
    Load a trained model from a file.
    """
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    return model
