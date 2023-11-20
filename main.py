# STD Modules
from lib.api import API
import time

# User Modules
from lib.indicator import SMA

# Authentication keys
secret_key = "8517b4a7e07104f5605d03680859fb88ea03486608beadc093155f258904019c"
api_key = "df7e0c08e87cf7d974a8acb2044ba36412b6c909a7d3a6cb073097a03a726f48"

# Create API Object
api_connector = API(secret_key, api_key)

# Position Status
status = -1

# Looping for Action
while True:
    # Get SMA Signal and Current High Price
    sma_signal, high_price, low_price = SMA(9, 21)    
    buy_quantity = int(200/high_price)
    sell_quantity = int(200/low_price)

    # Probability Checking and Take Action
    if sma_signal == 1 and status == -1:
        # Buy Order
        payload = {
            "side": "buy",
            "symbol": "matic/inr",
            "type": "limit",
            "price": high_price,
            "quantity": buy_quantity,
            "exchange": "coinswitchx"
        }
        print(api_connector.create_order(payload=payload))
        status = 1
    
    elif sma_signal == -1 and status == 1:
        # Sell Order
        payload = {
            "side": "sell",
            "symbol": "matic/inr",
            "type": "limit",
            "price": low_price,
            "quantity": sell_quantity,
            "exchange": "coinswitchx"
        }
        print(api_connector.create_order(payload=payload))
        status = -1

    elif sma_signal == 0:
        print("Waiting for Enough Dataset...")

    else:
        print("Waiting for Signal...")

    # Time Interval for 30 min    
    time.sleep(3)
