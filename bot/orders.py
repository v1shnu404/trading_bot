from bot.client import client
from binance.exceptions import BinanceAPIException
from bot.logging_config import logging

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            return order

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
            return order

    except BinanceAPIException as e:
        logging.error(f"Binance API error: {e.status_code} - {e.message}")
        raise
    except Exception as e:
        logging.error(f"Network or unexpected error: {e}")
        raise