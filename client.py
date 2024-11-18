import requests
import matplotlib.pyplot as plt
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

# Function to get RSI data
def get_rsi(window: int):
    url = f"{BASE_URL}/stocks/indicators/rsi"
    params = {"window": window}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("RSI Data:", data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to get Bollinger Bands data
def get_bollinger(window: int, std_dev: int):
    url = f"{BASE_URL}/stocks/indicators/bollinger"
    params = {"window": window, "std_dev": std_dev}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Bollinger Bands Data:", data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to get EMA data
def get_ema(window: int):
    url = f"{BASE_URL}/stocks/indicators/ema"
    params = {"window": window}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("EMA Data:", data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to get SMA data
def get_sma(window: int):
    url = f"{BASE_URL}/stocks/indicators/sma"
    params = {"window": window}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("SMA Data:", data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to get Highs and Lows data
def get_highs_lows(window: int):
    url = f"{BASE_URL}/stocks/indicators/highs-lows"
    params = {"window": window}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Highs and Lows Data:", data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to get Consolidation data
def get_consolidation(window: int):
    url = f"{BASE_URL}/stocks/indicators/consolidation"
    params = {"window": window}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Consolidation Data:", data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to plot all indicators
def plot_indicators(rsi_data, bb_data, ema_data, sma_data, highs_lows_data, consolidation_data, window):
    fig, axs = plt.subplots(3, 2, figsize=(15, 15))

    # Plotting RSI
    if rsi_data:
        print(f"rsi_data: {rsi_data}")
        try:
            rsi_dates = [item['date'] for item in rsi_data]
            rsi_values = [item['RSI'] for item in rsi_data]
            axs[0, 0].plot(rsi_dates, rsi_values, label='RSI', color='orange')
            axs[0, 0].axhline(70, color='red', linestyle='--')
            axs[0, 0].axhline(30, color='green', linestyle='--')
            axs[0, 0].set_title('RSI (Relative Strength Index)')
            axs[0, 0].set_ylabel('RSI Value')
            axs[0, 0].legend()
        except KeyError as e:
            print(f"KeyError: {e}. Adjusting the key names.")

    # Plotting Bollinger Bands
    if bb_data:
        print(f"bb_data: {bb_data}")
        try:
            bb_dates = [item.get('date', 'unknown') for item in bb_data]
            bb_upper = [item['BB_Upper'] for item in bb_data]
            bb_lower = [item['BB_Lower'] for item in bb_data]
            axs[0, 1].plot(bb_dates, bb_upper, label='Upper Band', color='red')
            axs[0, 1].plot(bb_dates, bb_lower, label='Lower Band', color='green')
            axs[0, 1].set_title('Bollinger Bands')
            axs[0, 1].set_ylabel('Price')
            axs[0, 1].legend()
        except KeyError as e:
            print(f"KeyError: {e}. Adjusting the key names.")

    # Plotting EMA
    if ema_data:
        print(f"ema_data: {ema_data}")
        try:
            ema_dates = [item.get('date', 'unknown') for item in ema_data]
            ema_values = [item[f"EMA_{window}"] for item in ema_data]
            axs[1, 0].plot(ema_dates, ema_values, label=f"EMA_{window}", color='blue')
            axs[1, 0].set_title(f'EMA ({window}-period)')
            axs[1, 0].set_ylabel('EMA Value')
            axs[1, 0].legend()
        except KeyError as e:
            print(f"KeyError: {e}. Adjusting the key names.")

    # Plotting SMA
    if sma_data:
        print(f"sma_data: {sma_data}")
        try:
            sma_dates = [item.get('date', 'unknown') for item in sma_data]
            sma_values = [item[f"SMA_{window}"] for item in sma_data]
            axs[1, 1].plot(sma_dates, sma_values, label=f"SMA_{window}", color='purple')
            axs[1, 1].set_title(f'SMA ({window}-period)')
            axs[1, 1].set_ylabel('SMA Value')
            axs[1, 1].legend()
        except KeyError as e:
            print(f"KeyError: {e}. Adjusting the key names.")

    # Plotting Highs and Lows
    if highs_lows_data:
        print(f"highs_lows_data: {highs_lows_data}")
        try:
            hl_dates = [item.get('date', 'unknown') for item in highs_lows_data]
            highs = [item['High_HH'] for item in highs_lows_data]
            lows = [item['Low_LL'] for item in highs_lows_data]
            axs[2, 0].plot(hl_dates, highs, label='High HH', color='green')
            axs[2, 0].plot(hl_dates, lows, label='Low LL', color='red')
            axs[2, 0].set_title('Highs and Lows (HH, LL)')
            axs[2, 0].set_ylabel('Price')
            axs[2, 0].legend()
        except KeyError as e:
            print(f"KeyError: {e}. Adjusting the key names.")

    # Plotting Consolidation
    if consolidation_data:
        print(f"consolidation_data: {consolidation_data}")
        try:
            cons_dates = [item.get('date', 'unknown') for item in consolidation_data]
            cons_values = [item['Consolidation'] for item in consolidation_data]
            axs[2, 1].plot(cons_dates, cons_values, label='Consolidation', color='orange')
            axs[2, 1].set_title('Consolidation Detection')
            axs[2, 1].set_ylabel('Consolidation Value')
            axs[2, 1].legend()
        except KeyError as e:
            print(f"KeyError: {e}. Adjusting the key names.")

    plt.tight_layout()
    plt.show()

# Example usage
window = 14  # Defining window size
rsi_data = get_rsi(window)
bb_data = get_bollinger(window, std_dev=2)
ema_data = get_ema(window)
sma_data = get_sma(window)
highs_lows_data = get_highs_lows(window)
consolidation_data = get_consolidation(window)

plot_indicators(rsi_data, bb_data, ema_data, sma_data, highs_lows_data, consolidation_data, window)
