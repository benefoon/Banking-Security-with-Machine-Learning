from sklearn.model_selection import cross_val_score
import numpy as np

def cross_validate_model(model, X_train, y_train, cv=5):
    """
    Perform k-fold cross-validation to evaluate model performance across different data splits.
    """
    # Perform cross-validation
    cv_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy')
    print(f"Cross-validation Scores (for {cv}-fold): {cv_scores}")
    print(f"Mean Cross-validation Score: {np.mean(cv_scores):.4f}")
