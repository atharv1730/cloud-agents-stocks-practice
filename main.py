import yfinance as yf

tickers = ["AAPL", "NVDA", "MSFT"]
for symbol in tickers:
    price = yf.Ticker(symbol).info["currentPrice"]
    print(f"The current price of {symbol} is: ${price}")