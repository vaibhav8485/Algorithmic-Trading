# STD Modules
import  ccxt
import pandas as pd

# Initialize CCXT exchange
exchange = ccxt.wazirx()

# Historical Dataset
def historical_data(symbol, timeframe, limit):
    historical_data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(historical_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    return df

