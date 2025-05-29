import os , sys 
import pandas as pd
import numpy as np
import maplotlib.pyplot as plt
import seaborn as sns



def load_stock_data(file_path):
    """
    Load stock data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file containing stock data.
    
    Returns:
    pd.DataFrame: DataFrame containing the stock data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error loading data from {file_path}: {e}")
def preprocess_stock_data(df):
    """
    Preprocess stock data by converting date column to datetime and setting it as index.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing stock data.
    
    Returns:
    pd.DataFrame: Preprocessed DataFrame with date as index.
    """
    if 'Date' not in df.columns:
        raise ValueError("DataFrame must contain a 'Date' column.")
    
    df['Date'] = pd.to_datetime(df['Date']).dt.date 
    if df['Date'].isnull().any():
        raise ValueError("Date column contains invalid dates.")
    df.set_index('Date', inplace=True)
    
    return df
