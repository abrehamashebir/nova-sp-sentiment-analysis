import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure sorted by date
    df = df.sort_values(by='Date').copy()
    
    # Simple Moving Averages
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    # Exponential Moving Averages
    df['EMA_12'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['EMA_26'] = df['Close'].ewm(span=26, adjust=False).mean()

    # MACD and Signal
    df['MACD'] = df['EMA_12'] - df['EMA_26']
    df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['MACD_Hist'] = df['MACD'] - df['MACD_Signal']

    # RSI (Relative Strength Index)
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    return df

def plot_macd(df, ticker):
    plt.figure(figsize=(10, 4))
    plt.plot(df['Date'], df['MACD'], label='MACD')
    plt.plot(df['Date'], df['MACD_Signal'], label='Signal')
    plt.bar(df['Date'], df['MACD_Hist'], color='gray', alpha=0.3)
    plt.title(f'{ticker} - MACD')
    plt.legend()
    plt.tight_layout()
    plt.show()
