# Data Preprocessing Script
import pandas as pd

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    # Preprocessing steps
    data.fillna(method='ffill', inplace=True)
    return data
