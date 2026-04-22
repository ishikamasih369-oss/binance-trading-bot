def validate_symbol(symbol):
    symbol = symbol.upper()

    if len(symbol) < 6:
        return False, "Invalid Symbol"

    if not symbol.endswith("USDT"):
        return False, "Only USDT pairs allowed"

    return True, "Valid Symbol"


def validate_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        return False, "Side must be BUY or SELL"
    return True, "Valid Side"


def validate_order_type(order_type):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        return False, "Type must be MARKET or LIMIT"
    return True, "Valid Type"


def validate_quantity(qty):
    try:
        qty = float(qty)
        if qty <= 0:
            return False, "Quantity must be greater than 0"
        return True, "Valid Quantity"
    except:
        return False, "Quantity must be numeric"


def validate_price(price):
    try:
        price = float(price)
        if price <= 0:
            return False, "Price must be greater than 0"
        return True, "Valid Price"
    except:
        return False, "Price must be numeric"