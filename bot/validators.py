
def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Invalid side. Must be 'BUY' or 'SELL'")

def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type. Must be 'MARKET' or 'LIMIT'")

def validate_price(order_type, price):
    if order_type.upper() == "LIMIT" and price is None:
        raise ValueError("Price must be specified for LIMIT orders")
