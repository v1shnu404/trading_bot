def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either 'BUY' or 'SELL'")
    return side

def validate_order_type(order_type):
    valid_types = ["MARKET", "LIMIT"]
    if order_type not in valid_types:
        raise ValueError(f"Order type must be one of {valid_types}")
    return order_type

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    return quantity