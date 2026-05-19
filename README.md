# Binance Futures Trading Bot

A command-line trading bot for placing orders on the **Binance Futures Testnet (USDT-M)**. Supports Market and Limit orders with structured logging and input validation.

---

## Project Structure

```
trading_bot/
  bot/
    __init__.py
    client.py           # Binance client wrapper
    orders.py           # Order placement logic
    validators.py       # Input validation
    logging_config.py   # Logging setup
  cli.py                # CLI entry point
  README.md
  requirements.txt
  .env.example
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/trading_bot.git
cd trading_bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file

```bash
cp .env.example .env
```

Then open `.env` and fill in your Binance Futures Testnet API credentials:

```
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

To get testnet credentials:
1. Go to [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Log in with GitHub
3. Navigate to **API Key** and generate a key pair

---

## How to Run

All commands are run from the `trading_bot/` root directory.

### Market Order

```bash
# BUY
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

# SELL
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01
```

### Limit Order

```bash
# BUY LIMIT (price below market — resting bid)
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 102000

# SELL LIMIT (price above market — resting ask)
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 107000
```

> **Note:** `--price` is required for LIMIT orders. The bot will error if it's missing.

### Arguments

| Argument     | Required | Description                          |
|--------------|----------|--------------------------------------|
| `--symbol`   | Yes      | Trading pair, e.g. `BTCUSDT`         |
| `--side`     | Yes      | `BUY` or `SELL`                      |
| `--type`     | Yes      | `MARKET` or `LIMIT`                  |
| `--quantity` | Yes      | Order quantity in base asset         |
| `--price`    | No*      | Limit price (* required for LIMIT)   |

---

## Logs

All activity is logged to `trading_bot.log` in the project root. This includes:
- Order request details
- Full order response (orderId, status, executedQty, avgPrice, etc.)
- Validation errors
- API errors

---

## Assumptions

- Only **USDT-M Futures Testnet** is supported; not intended for mainnet use.
- Minimum order notional is **$50** (Binance requirement). Ensure `quantity × price ≥ 50`.
- For LIMIT orders, price must be within ~10% of the current mark price (Binance `PERCENT_PRICE` filter).
- Credentials are loaded from a `.env` file in the project root using `python-dotenv`.
- The bot uses `timeInForce=GTC` (Good Till Cancelled) for all Limit orders.
