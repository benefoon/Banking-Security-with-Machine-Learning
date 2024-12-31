import xgboost as xgb
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import accuracy_score, classification_report

def train_xgboost_model(X_train, y_train, X_test, y_test):
    # Define the XGBoost model
    model = xgb.XGBClassifier(eval_metric='mlogloss', use_label_encoder=False)

    # Define parameter grid for hyperparameter tuning
    param_grid = {
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2],
        'n_estimators': [100, 200],
        'subsample': [0.8, 1.0],
    }

    # Set up GridSearchCV for hyperparameter tuning
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, 
                               cv=StratifiedKFold(n_splits=5), scoring='accuracy', n_jobs=-1, verbose=1)
    
    # Train the model using GridSearchCV
    grid_search.fit(X_train, y_train)
    
    # Get the best model
    best_model = grid_search.best_estimator_
    
    # Predict on the test set
    y_pred = best_model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f"Best Hyperparameters: {grid_search.best_params_}")
    print(f"Accuracy: {accuracy}")
    print(report)
    
    return best_model
