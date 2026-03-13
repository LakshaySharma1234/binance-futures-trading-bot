# Trading Bot 

 Setup

1. Create Binance Futures Testnet account
2. Generate API Keys
3. Add keys to `.env`

 Install

pip install -r requirements.txt

Run

MARKET:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000

