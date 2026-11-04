import yfinance as yf

ticker = yf.Ticker("AAPL")
data = ticker.info

print(f"AAPL Stock Information: ${data['currentPrice']}")
print(f"Day high: ${data['dayHigh']}")
print(f"Day low: ${data['dayLow']}")