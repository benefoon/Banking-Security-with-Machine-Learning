from sklearn.model_selection import RandomizedSearchCV
import numpy as np
import xgboost as xgb

def tune_xgboost_model(X_train, y_train):
    # Define the XGBoost model
    model = xgb.XGBClassifier(eval_metric='mlogloss', use_label_encoder=False)

    # Define the hyperparameter space for RandomizedSearchCV
    param_dist = {
        'max_depth': [3, 5, 7, 9],
        'learning_rate': [0.01, 0.1, 0.2],
        'n_estimators': [100, 200, 300],
        'subsample': [0.8, 0.9, 1.0],
        'colsample_bytree': [0.7, 0.8, 0.9]
    }

    # RandomizedSearchCV with 5-fold cross-validation
    random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist,
                                       n_iter=10, cv=5, verbose=1, n_jobs=-1, random_state=42, scoring='accuracy')

    # Fit the model
    random_search.fit(X_train, y_train)

    # Print best parameters
    print(f"Best Parameters: {random_search.best_params_}")
    
    return random_search.best_estimator_
