# scripts/merge_all_stocks.py

from src.stock_data import StockData
import pandas as pd
import os

def process_and_merge_stocks(tickers, base_dir="./datasets/"):
    all_dfs = []

    for ticker in tickers:
        print(f"\n📥 Processing {ticker}...")
        stock = StockData(ticker=ticker, base_dir=base_dir)
        stock.load_data()
        stock.clean_data()
        stock.calculate_returns()
        all_dfs.append(stock.get_dataframe())

    merged_df = pd.concat(all_dfs, ignore_index=True)
    
    return merged_df
