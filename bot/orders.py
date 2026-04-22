from bot.client import get_client

client = get_client()
def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        print("\nOrder Success")
        print("Order ID:", order["orderId"])
        print("Status:", order["status"])

    except Exception as e:
        print("Order Failed")
        print(e)


def view_open_orders(symbol):
    try:
        orders = client.futures_get_open_orders(symbol=symbol)

        if not orders:
            print("No Open Orders Found")
            return

        print("\n===== OPEN ORDERS =====")

        for order in orders:
            print("Order ID :", order["orderId"])
            print("Symbol   :", order["symbol"])
            print("Side     :", order["side"])
            print("Type     :", order["type"])
            print("Price    :", order["price"])
            print("Qty      :", order["origQty"])
            print("Status   :", order["status"])
            print("----------------------")

    except Exception as e:
        print("Error:", e)


def cancel_open_orders(symbol):
    try:
        result = client.futures_cancel_all_open_orders(symbol=symbol)

        print("\nAll Open Orders Cancelled for", symbol)
        print(result)

    except Exception as e:
        print("Error:", e)