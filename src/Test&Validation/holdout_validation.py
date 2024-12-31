from sklearn.metrics import accuracy_score

def evaluate_on_new_data(model, new_data, new_labels):
    """
    Evaluate the trained model on new unseen data to test its generalization ability.
    """
    # Make predictions on the new data
    y_pred_new = model.predict(new_data)

    # Calculate accuracy on the new data
    accuracy = accuracy_score(new_labels, y_pred_new)
    print(f"Accuracy on New Data: {accuracy:.4f}")
