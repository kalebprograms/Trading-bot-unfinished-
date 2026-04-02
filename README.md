# Bitcoin/USDT XRP/USDT Algorithmic Trading Bot

A Python-based algorithmic trading strategy built with Freqtrade for Kraken spot markets on the 5-minute timeframe.

This repository contains a custom strategy focused on short-term momentum and pullback entries using technical confirmation from RSI, EMA structure, Bollinger Bands, candle behavior, and volume. The current repository setup is configured specifically for:

- BTC/USDT
- XRP/USDT

## Portfolio Overview

This project was developed as a practical algorithmic trading and strategy-testing workflow using Python and Freqtrade. It demonstrates:

- Strategy development for cryptocurrency markets
- Technical indicator-based entry logic
- Rule-based automation for trade execution
- Backtesting and performance evaluation
- Configuration management for reproducible testing
- Safe separation of strategy code and local credentials

The strategy is designed for educational, portfolio, and research purposes.

## Strategy Summary

`KrakenScalpHF` is a 5-minute strategy that looks for structured long entries under a narrow set of conditions. The strategy combines:

- Fast EMA above slow EMA to confirm local trend direction
- RSI within a controlled momentum range
- Rising RSI to confirm short-term recovery
- Price above the slow EMA but below the fast EMA to capture pullbacks
- Price below the Bollinger middle band to avoid extended entries
- Green candle confirmation
- Volume above rolling average threshold

The bot uses ROI-based exits and does not rely on exit signals in the current configuration.

## Current Repository Configuration

This repository is currently configured for the following setup:

- Exchange: Kraken
- Trading Mode: Spot
- Timeframe: 5m
- Pair Whitelist:
  - BTC/USDT
  - XRP/USDT
- Entry Type: Limit
- Exit Type: Limit
- Exit Logic: ROI only
- Trailing Stop: Disabled
- Exit Signals: Disabled

## Current Strategy Parameters

The current strategy file uses the following defaults:

- Timeframe: `5m`
- Startup candles: `50`
- Minimal ROI: `0.009`
- Stoploss: `-0.200`
- Buy RSI range parameter: `45` to `65`
- Default buy RSI: `55`
- EMA fast length: `12`
- EMA slow length: `34`
- Volume multiplier default: `0.9`

## Repository Structure

freqtrade-github-repo/
├── .gitignore
├── README.md
├── requirements.txt
├── user_data/
│   ├── config.example.json
│   └── strategies/
│       └── KrakenScalpHF.py
├── backtest-metadata/
└── strategies/
    └── KrakenScalpHF.py
## Important Folder Note

Freqtrade uses the strategy file inside:

user_data/strategies/KrakenScalpHF.py

If you see another KrakenScalpHF.py in a separate strategies folder outside user_data, treat that as a duplicate repository file and not the primary runtime file. The active strategy should be maintained in:

user_data/strategies/KrakenScalpHF.py
Backtest Snapshot

This repository is based on a BTC/USDT + XRP/USDT backtest configuration using the current setup. A recent run produced:

10 total trades
80.0% win rate
0.14% total profit
Profit factor of 1.24

Backtest results are historical simulations only and do not guarantee future live results.

Skills Demonstrated

This project demonstrates practical experience with:

Python strategy development
Quantitative trading workflow design
Technical indicator integration
Market-pair specific configuration
Debugging configuration and path issues
Running and interpreting backtests
Organizing code for portfolio presentation
Technologies Used
Python
Freqtrade
Pandas
TA-Lib
JSON configuration
Git and GitHub
Security Notice

This repository is intentionally structured to avoid committing real credentials.

Do not upload or publish:

Kraken API keys
Kraken API secrets
Telegram tokens
Telegram chat IDs
JWT secrets
API server usernames and passwords
Any local production config containing private credentials

Use the example configuration file for repository sharing and keep real credentials only in your local environment.

How to Open and Run This Project from GitHub
Step 1: Clone the repository

Open Command Prompt, PowerShell, or Git Bash and run:

git clone https://github.com/kalebprograms/KrakenScalpHF-Algorithmic-Trading-Bot.git
cd KrakenScalpHF-Algorithmic-Trading-Bot
Step 2: Create a virtual environment
python -m venv .venv
Step 3: Activate the virtual environment

Windows Command Prompt:

.venv\Scripts\activate

Windows PowerShell:

.venv\Scripts\Activate.ps1

Mac/Linux:

source .venv/bin/activate
Step 4: Install project dependencies
pip install -r requirements.txt
Step 5: Open the project folder

If using VS Code:

code .

If you are not using VS Code, simply open the cloned folder in your preferred code editor.

Step 6: Review the active strategy file

Open the strategy located at:

user_data/strategies/KrakenScalpHF.py

This is the strategy file Freqtrade should use for backtesting and local runs.

Step 7: Review the example config file

Open:

user_data/config.example.json

This file contains the repository-safe configuration template for the current setup.

Step 8: Create your local runtime config

Copy the example file into a local config file:

Windows Command Prompt:

copy user_data\config.example.json user_data\config.json

PowerShell:

Copy-Item user_data/config.example.json user_data/config.json

Mac/Linux:

cp user_data/config.example.json user_data/config.json
Step 9: Add your own local credentials

Edit:

user_data/config.json

Replace placeholders with your own local values:

YOUR_KRAKEN_API_KEY
YOUR_KRAKEN_API_SECRET
YOUR_TELEGRAM_BOT_TOKEN
YOUR_TELEGRAM_CHAT_ID
YOUR_RANDOM_JWT_SECRET
YOUR_RANDOM_WS_TOKEN
YOUR_USERNAME
YOUR_STRONG_PASSWORD

Do not push this local file to GitHub if it contains real credentials.

Step 10: Confirm the intended pair setup

This repository is currently meant to run with:

BTC/USDT
XRP/USDT

That setup is already reflected in the example config and should also be used in the backtest command below.

How to Run the Current Repository Setup

Run this exact command from the root project folder:

python -m freqtrade backtesting --strategy KrakenScalpHF --timeframe 5m --config user_data/config.example.json --pairs BTC/USDT XRP/USDT

If you want to run against your own local credential file instead of the example file, use:

python -m freqtrade backtesting --strategy KrakenScalpHF --timeframe 5m --config user_data/config.json --pairs BTC/USDT XRP/USDT
Recommended Local Workflow

A clean local workflow for this project is:

Pull or clone the repository
Open the project
Activate the virtual environment
Install dependencies
Edit only user_data/strategies/KrakenScalpHF.py
Keep the runtime config in user_data/config.json
Run the backtest command from the repository root
Review results and iterate
Notes for Recruiters and Reviewers

This project reflects hands-on experimentation with rule-based trading systems rather than production financial advice. The focus of the repository is:

strategy logic design
backtesting workflow
debugging and iteration
reproducible local execution
clean portfolio presentation on GitHub

The repository demonstrates the ability to build and maintain an end-to-end technical project involving Python, configuration files, command-line tooling, and data-driven testing.

Resume-Friendly Project Description

KrakenScalpHF Algorithmic Trading Bot

Developed a custom Python-based cryptocurrency trading strategy using Freqtrade
Designed momentum and pullback entry logic using RSI, EMA structure, Bollinger Bands, and volume confirmation
Configured and backtested the strategy for Kraken spot markets on BTC/USDT and XRP/USDT
Built a reproducible local project structure with separated strategy, configuration, and credentials workflow
Used backtesting metrics to evaluate profitability, trade frequency, win rate, and risk behavior
Disclaimer

This project is for educational, research, and portfolio purposes only. Historical backtest performance does not guarantee future live trading results. Use caution and perform your own validation before deploying any strategy in a live environment.

License

This project is shared for educational and portfolio use.
