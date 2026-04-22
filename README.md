# Binance Futures Trading Bot (Python)

A modular Python CLI application for placing **Market** and **Limit** orders on **Binance Futures Testnet (USDT-M)**.
Built as an internship assignment with structured code, input validation, logging, and bonus CLI features.

---

# Features

## Core Features

* Place **MARKET** orders
* Place **LIMIT** orders
* Supports **BUY** and **SELL**
* Input validation for:

  * Symbol
  * Side
  * Order Type
  * Quantity
  * Price (required for LIMIT)
* Clear terminal output:

  * Order request summary
  * Order response details
  * Success / failure message

## Project Structure

* `bot/client.py` → Binance API client connection
* `bot/orders.py` → Order execution logic
* `bot/validators.py` → Input validation
* `bot/logging_config.py` → Logging setup
* `bot/mean_reversion_bot.py` → Bonus strategy module
* `cli.py` → Main CLI entry point

## Logging

Logs all:

* API requests
* API responses
* Errors / exceptions

Saved inside:


logs/


# Bonus Features Implemented

* Enhanced CLI UX (menu-driven interface)
* View Open Orders
* Cancel Open Orders
* Mean Reversion Bot Strategy



# Requirements

Install Python 3.x

Install dependencies:


pip install -r requirements.txt


# requirements.txt


python-binance
python-dotenv


# Environment Setup

Create a `.env` file in root folder:


API_KEY=your_binance_testnet_api_key
SECRET_KEY=your_binance_testnet_secret_key

Use Binance Futures Testnet / Demo API keys.


# How to Run

python cli.py


# CLI Menu


1. Place Order
2. Run Mean Reversion Bot
3. View Logs
4. View Open Orders
5. Cancel Open Orders
6. Exit


# Example Usage

## Market Order


Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001


## Limit Order

Symbol   : BTCUSDT
Side     : SELL
Type     : LIMIT
Quantity : 0.001
Price    : 80000



# Assumptions

* Binance Futures Testnet account is active
* Valid API keys are provided in `.env`
* Sufficient testnet balance is available
* Internet connection is active



# Sample Output


Order Success
Order ID: 13061191700
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00



# Folder Structure


trading_bot/
│── bot/
│   │── __init__.py
│   │── client.py
│   │── orders.py
│   │── validators.py
│   │── logging_config.py
│   │── mean_reversion_bot.py
│
│── logs/
│── cli.py
│── requirements.txt
│── README.md
│── .env


# Notes

* LIMIT orders remain open until market reaches target price.
* MARKET orders execute instantly.
* `.env` file should not be shared publicly.



# Author

Developed in Python as part of Binance Trading Bot Internship Assignment.
