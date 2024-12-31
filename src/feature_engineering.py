import numpy as np

def feature_engineering(data):
    # Example of feature engineering: Creating interaction features
    data['amount_per_transaction'] = data['transaction_amount'] / (data['transaction_count'] + 1)

    # Example of time-based features (if relevant)
    data['hour_of_day'] = pd.to_datetime(data['transaction_time']).dt.hour

    # Example of aggregating features
    data['avg_transaction_amount'] = data.groupby('user_id')['transaction_amount'].transform('mean')

    return data
