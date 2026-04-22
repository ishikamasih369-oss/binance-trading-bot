import os
from bot.orders import place_order,view_open_orders,cancel_open_orders
from bot.logging_config import setup_logger
from bot.mean_reversion_bot import run_mean_reversion

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def show_menu():
    print("\n===== Binance Trading Bot =====")
    print("1. Place Order")
    print("2. Run Mean Reversion Bot")
    print("3. View Logs")
    print("4. View Open Orders")
    print("5. Cancel Open Orders") 
    print("6. Exit")   



def place_order_menu():
    symbol = input("Enter Symbol: ").upper()
    valid, msg = validate_symbol(symbol)
    if not valid:
        print("❌", msg)
        return

    side = input("Enter Side (BUY/SELL): ").upper()
    valid, msg = validate_side(side)
    if not valid:
        print("❌", msg)
        return

    order_type = input("Enter Type (MARKET/LIMIT): ").upper()
    valid, msg = validate_order_type(order_type)
    if not valid:
        print("❌", msg)
        return

    quantity = input("Enter Quantity: ")
    valid, msg = validate_quantity(quantity)
    if not valid:
        print("❌", msg)
        return

    price = None

    if order_type == "LIMIT":
        price = input("Enter Price: ")
        valid, msg = validate_price(price)
        if not valid:
            print("❌", msg)
            return

    print("\n===== Order Request Summary =====")
    print("Symbol   :", symbol)
    print("Side     :", side)
    print("Type     :", order_type)
    print("Quantity :", quantity)

    if price:
        print("Price    :", price)

    confirm = input("\nConfirm Order? (Y/N): ").upper()

    if confirm == "Y":
        print("\nPlacing order...\n")
        place_order(symbol, side, order_type, quantity, price)
    else:
        print("❌ Order Cancelled")


def view_logs():
    path = "logs/trading.log"

    if os.path.exists(path):
        print("\n===== Trading Logs =====\n")
        with open(path, "r") as file:
            print(file.read())
    else:
        print("❌ No logs found.")


def main():
    setup_logger()

    while True:
        show_menu()
        choice = input("\nEnter Choice: ")

        if choice == "1":
            place_order_menu()

        elif choice == "2":
            run_mean_reversion()

        elif choice == "3":
            view_logs()
        elif choice == "4":
           symbol = input("Enter Symbol: ").upper()
           view_open_orders(symbol)

        elif choice == "5":
            symbol = input("Enter Symbol: ").upper()
            cancel_open_orders(symbol)

        elif choice == "6":
            print("Goodbye")
            break    

        else:
            print("❌ Invalid Choice")


if __name__ == "__main__":
    main()