# My Modules
from lib.dataset import historical_data

# Get historical Data
df = historical_data('MATIC/INR', '1d', 200)

# SMA Indicator
def SMA(short_sma, long_sma):
    # Calculate SMAs
    df['short_SMA'] = df['close'].rolling(window=short_sma).mean()
    df['long_SMA'] = df['close'].rolling(window=long_sma).mean()

    # Generate buy and sell signals
    df['signal'] = 0  # 0 indicates no action, 1 indicates buy, -1 indicates sell

    # Buy signal: Short SMA crosses above Long SMA
    df.loc[df['short_SMA'] > df['long_SMA'], 'signal'] = 1

    # Sell signal: Short SMA crosses below Long SMA
    df.loc[df['short_SMA'] < df['long_SMA'], 'signal'] = -1

    # Correct the signals to avoid false positives/negatives
    df['position'] = df['signal'].diff()  # Calculate the position changes

    # # Download Dataset in CSV formate
    # df.to_csv('dataset_with_SMA.csv')

    # # To See Detail about Todays Dataset
    # print(df.iloc[-1])

    signal = df['signal'].iloc[-1]
    high = int(df['high'].iloc[-1])
    high+=1
    low = int(df['low'].iloc[-1])
    low-=1

    # Return SMA Signal with Current High Price
    return signal, high, low
