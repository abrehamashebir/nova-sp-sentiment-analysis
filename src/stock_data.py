# src/stock_data.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class StockData:
    def __init__(self, ticker: str, base_dir: str):
        """
        ticker: Stock symbol (e.g., AAPL)
        base_dir: Directory containing the CSV files
        """
        self.ticker = ticker
        self.file_path = os.path.join(base_dir, f"{ticker}_historical_data.csv")
        self.df = None

    def load_data(self):
        """
        Load CSV into a DataFrame and parse dates.
        """
        self.df = pd.read_csv(self.file_path)
        self.df['stock'] = self.ticker
        self.df['Date'] = pd.to_datetime(self.df['Date']).dt.date
        return self.df

    def describe(self):
        """
        Print basic statistics and null values.
        """
        print(f"--- {self.ticker} Summary ---")
        print(self.df.describe())
        print("\nMissing values:")
        print(self.df.isnull().sum())

    def clean_data(self):
        """
        Forward-fill missing values.
        """
        self.df.fillna(method='ffill', inplace=True)

    def calculate_returns(self):
        """
        Compute daily percentage return based on closing price.
        """
        self.df.sort_values(by='Date', inplace=True)
        self.df['daily_return'] = self.df['Close'].pct_change()

    def visualize_price(self):
        """
        Line plot of closing prices over time.
        """
        plt.figure(figsize=(10, 4))
        plt.plot(self.df['Date'], self.df['Close'], label='Close Price')
        plt.title(f'{self.ticker} Stock Price Over Time')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def visualize_returns(self):
        """
        Histogram of daily returns.
        """
        plt.figure(figsize=(8, 4))
        sns.histplot(self.df['daily_return'].dropna(), bins=50, kde=True)
        plt.title(f'{self.ticker} Daily Return Distribution')
        plt.xlabel('Daily Return')
        plt.tight_layout()
        plt.show()

    def get_dataframe(self):
        """
        Return the internal DataFrame for merging or export.
        """
        return self.df
