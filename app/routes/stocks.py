from fastapi import APIRouter, HTTPException
from app.indicators import (
    load_stock_data, calculate_rsi, calculate_bollinger_bands,
    calculate_ema, calculate_sma, calculate_highs_lows, detect_consolidation
)
import os
import pandas as pd

router = APIRouter()

# Getting the current working directory
current_dir = os.getcwd()

# Defining the CSV file name
csv_file = 'stock_data.csv'

# Joining the current directory with the CSV file name
FILE_PATH = os.path.join(current_dir, 'app', 'routes', csv_file)

try:
    stock_data = load_stock_data(FILE_PATH)
except Exception as e:
    raise RuntimeError(f"Error loading stock data: {e}")

@router.get("/indicators/rsi")
async def get_rsi(window: int = 14):
    # Endpoint to get RSI values.
    data = calculate_rsi(stock_data.copy(), window)
    return data[["Close", "RSI"]].dropna().to_dict(orient="records")

@router.get("/indicators/bollinger")
async def get_bollinger_bands(window: int = 20, std_dev: int = 2):
    # Endpoint to get Bollinger Bands.
    data = calculate_bollinger_bands(stock_data.copy(), window, std_dev)
    return data[["Close", "BB_Upper", "BB_Lower"]].dropna().to_dict(orient="records")

@router.get("/indicators/ema")
async def get_ema(window: int = 20):
    # Endpoint to get EMA values.
    data = calculate_ema(stock_data.copy(), window)
    return data[["Close", f"EMA_{window}"]].dropna().to_dict(orient="records")

@router.get("/indicators/sma")
async def get_sma(window: int = 20):
    # Endpoint to get SMA values.
    data = calculate_sma(stock_data.copy(), window)
    return data[["Close", f"SMA_{window}"]].dropna().to_dict(orient="records")

@router.get("/indicators/highs-lows")
async def get_highs_lows(window: int = 20):
    # Endpoint to get Highest Highs and Lowest Lows.
    data = calculate_highs_lows(stock_data.copy(), window)
    return data[["High", "Low", "High_HH", "Low_LL"]].dropna().to_dict(orient="records")

@router.get("/indicators/consolidation")
async def get_consolidation(window: int = 20):
    # Endpoint to detect consolidation periods.
    data = detect_consolidation(stock_data.copy(), window)
    return data[["Close", "Consolidation"]].dropna().to_dict(orient="records")
