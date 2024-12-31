import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Handle missing values
    data.fillna(method='ffill', inplace=True)  # Forward fill missing values

    # Feature encoding (if needed)
    label_encoder = LabelEncoder()
    data['encoded_feature'] = label_encoder.fit_transform(data['categorical_feature'])

    # Scaling features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data[['feature1', 'feature2', 'feature3']])

    # Split data into training and testing sets
    X = data.drop(columns=['target'])
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_t
