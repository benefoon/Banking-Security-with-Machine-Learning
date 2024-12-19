def detect_outliers(data, column, threshold=3):
    """Detects outliers in a dataset using z-score."""
    mean = data[column].mean()
    std = data[column].std()
    data['z_score'] = (data[column] - mean) / std
    return data[data['z_score'].abs() > threshold]
