 



import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class news_data:
    def __init__(self):
        """
        Initialize the news_data class.
        This class is designed to handle news data operations.
        """
        pass
   
  

    def load_news_data(self,file_path):
        """
        Load news data from a CSV file.

        Parameters:
        file_path (str): Path to the CSV file containing news data.

        Returns:
        pd.DataFrame: DataFrame containing the news data.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            raise ValueError(f"Error loading data from {file_path}: {e}")
        
    

    def preprocess_news_data(self,df):
        """
        Preprocess news data by converting date column to datetime and setting it as index.

        Parameters:
        df (pd.DataFrame): DataFrame containing news data.

        Returns:
        pd.DataFrame: Preprocessed DataFrame with date as index.
        """
        if 'Unnamed:0' in df.columns:
            df.drop(columns=['Unnamed'], inplace=True)

        if 'date' not in df.columns:
            raise ValueError("DataFrame must contain a 'Ddte' column.")
        
        df['date'] = pd.to_datetime(df['date'], format='ISO8601').dt.date
        if df['date'].isnull().any():
            raise ValueError("Date column contains invalid dates.")
        
        df.set_index('date', inplace=True)
        
        return df
    def plot_news_data(df, column='Sentiment'):
        """
        Plot the specified column of the news data.
        Parameters:
        df (pd.DataFrame): DataFrame containing news data.
        column (str): Column to plot. Default is 'Sentiment'.
        """ 
        if column not in df.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df, x=df.index, y=column)
        plt.title(f"{column} Over Time")
        plt.xlabel("Date")
        plt.ylabel(column)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    def get_news_sentiment(df):
        """
        Calculate the average sentiment of the news data.
        Parameters:
        df (pd.DataFrame): DataFrame containing news data.
        Returns:
        float: Average sentiment value.
        """     
        if 'Sentiment' not in df.columns:
            raise ValueError("DataFrame must contain a 'Sentiment' column.")
        
        return df['Sentiment'].mean()
    def get_news_volume(df):
        """
        Calculate the total volume of news articles.
        Parameters:                                                 
        df (pd.DataFrame): DataFrame containing news data.
        Returns:
        int: Total number of news articles.
        """
        if 'Volume' not in df.columns:
            raise ValueError("DataFrame must contain a 'Volume' column.")
        
        return df['Volume'].sum()
    def get_news_summary(df):
        """
        Generate a summary of the news data.
        Parameters:
        df (pd.DataFrame): DataFrame containing news data.
        Returns:                
        dict: Summary containing average sentiment and total volume.
        """

        summary = {
            'Average Sentiment': get_news_sentiment(df),
            'Total Volume': get_news_volume(df)
        }
        return summary
    def save_news_data(df, file_path):
        """
        Save the news data to a CSV file.
        Parameters:
        df (pd.DataFrame): DataFrame containing news data.
        file_path (str): Path to save the CSV file.
        """
        try:
            df.to_csv(file_path)
            print(f"Data saved to {file_path}")
        except Exception as e:
            raise ValueError(f"Error saving data to {file_path}: {e}")
   