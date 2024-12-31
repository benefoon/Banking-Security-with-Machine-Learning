from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def evaluate_model_on_test_set(model, X_test, y_test):
    """
    Evaluate the trained model on the test data and display accuracy, classification report, and confusion matrix.
    """
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate and print the accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Test Set Accuracy: {accuracy:.4f}")

    # Generate and display the classification report
    report = classification_report(y_test, y_pred)
    print("Classification Report:\n", report)

    # Generate and plot the confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Class 0", "Class 1"], yticklabels=["Class 0", "Class 1"])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.show()
