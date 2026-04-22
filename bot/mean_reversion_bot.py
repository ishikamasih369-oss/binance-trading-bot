from bot.client import get_client
from bot.orders import place_order
import time

client = get_client()

def run_mean_reversion():
    symbol = "BTCUSDT"
    quantity = 0.001

    print("\n===== Mean Reversion Bot Started =====")

    prices = []

    for i in range(5):
        ticker = client.futures_symbol_ticker(symbol=symbol)
        price = float(ticker["price"])
        prices.append(price)
        print(f"Collected Price {i+1}: {price}")
        time.sleep(2)

    avg_price = sum(prices) / len(prices)

    current = prices[-1]

    print("\nAverage Price:", round(avg_price, 2))
    print("Current Price:", current)

    if current < avg_price:
        print("\nSignal: BUY")
        place_order(symbol, "BUY", "MARKET", quantity)

    elif current > avg_price:
        print("\nSignal: SELL")
        place_order(symbol, "SELL", "MARKET", quantity)

    else:
        print("\nNo Trade Signal")