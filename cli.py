from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import logging
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="e.g. BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price")

    return parser.parse_args(), parser

if __name__ == "__main__":
    args, parser = parse_args()
    if args.type == "LIMIT" and args.price is None:
        parser.error("Price is required for LIMIT orders")


    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        order = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

    
        logging.info(f"Placing order for {args.quantity} {args.symbol} at {args.price if args.price else 'market price'}")
        logging.info(f"{args.type} {args.side} order placed successfully for {args.quantity} {args.symbol}")
        logging.info(f"Order details: {order}")
        print("Order placed successfully! Check trading_bot.log for details.")

    
    except ValueError as e:
        logging.error(f"Validation error: {e}")
        print("Error occured, check trading_bot.log for details.")
    
    
