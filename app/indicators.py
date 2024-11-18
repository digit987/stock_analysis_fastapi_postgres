import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands
from ta.trend import EMAIndicator, SMAIndicator

def load_stock_data(file_path: str):
    # Loading stock data from a CSV file.
    try:
        df = pd.read_csv(file_path, parse_dates=["Date"], dayfirst=True)
        df.set_index("Date", inplace=True)
        return df
    except Exception as e:
        raise ValueError(f"Error loading stock data: {e}")

def calculate_rsi(data: pd.DataFrame, window: int = 14):
    # Calculating the RSI (Relative Strength Index).
    rsi_indicator = RSIIndicator(close=data["Close"], window=window)
    data["RSI"] = rsi_indicator.rsi()
    return data

def calculate_bollinger_bands(data: pd.DataFrame, window: int = 20, std_dev: int = 2):
    # Calculating Bollinger Bands.
    bb_indicator = BollingerBands(close=data["Close"], window=window, window_dev=std_dev)
    data["BB_Upper"] = bb_indicator.bollinger_hband()
    data["BB_Lower"] = bb_indicator.bollinger_lband()
    return data

def calculate_ema(data: pd.DataFrame, window: int = 20):
    # Calculating Exponential Moving Average.
    ema_indicator = EMAIndicator(close=data["Close"], window=window)
    data[f"EMA_{window}"] = ema_indicator.ema_indicator()
    return data

def calculate_sma(data: pd.DataFrame, window: int = 20):
    # Calculating Simple Moving Average.
    sma_indicator = SMAIndicator(close=data["Close"], window=window)
    data[f"SMA_{window}"] = sma_indicator.sma_indicator()
    return data

def calculate_highs_lows(data: pd.DataFrame, window: int = 20):
    # Calculating Highest High and Lowest Low.
    data["High_HH"] = data["High"].rolling(window=window).max()
    data["Low_LL"] = data["Low"].rolling(window=window).min()
    return data

def detect_consolidation(data: pd.DataFrame, window: int = 20):
    # Detecting consolidation by measuring volatility (range of high and low).
    data["Range"] = data["High"] - data["Low"]
    data["Consolidation"] = data["Range"].rolling(window=window).mean() < 0.05 * data["Close"].mean()
    return data
