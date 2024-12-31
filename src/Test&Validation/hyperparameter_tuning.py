from sklearn.model_selection import GridSearchCV

def tune_hyperparameters(model, X_train, y_train):
    """
    Tune model hyperparameters using GridSearchCV to find the best combination.
    """
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [10, 20, 30, None],
        'learning_rate': [0.01, 0.05, 0.1]
    }
    
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    
    print("Best Parameters Found: ", grid_search.best_params_)
    print("Best Cross-validation Score: ", grid_search.best_score_)
    
    return grid_search.best_estimator_
