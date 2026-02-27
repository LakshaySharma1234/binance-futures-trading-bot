import argparse
import logging

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import setup_logging



def main():
    print("CLI started")
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--order_type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.order_type)
        validate_price(args.order_type, args.price)

        client = get_client()

        print("\n📌 Order Request Summary")
        print(vars(args))

        order = place_order(
            client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n✅ Order Response")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")

        print("\n🎉 SUCCESS")

    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        logging.error(f"CLI Failure: {e}")

if __name__ == "__main__":
    main()