import time
import yfinance as yf

WATCHLIST = {
    "AAPL": {"alert_below": 300, "alert_above": 350, "tracked": False},
    "NVDA": {"alert_below": 250, "alert_above": 300, "tracked": False},
    "MSFT": {"alert_below": 220, "alert_above": 250, "tracked": False},
}

while True:
    for symbol, rules in WATCHLIST.items():
        price = yf.Ticker(symbol).info["currentPrice"]
        out_of_range = price < rules["alert_below"] or price > rules["alert_above"]
        
        if out_of_range and not rules["tracked"]:
            print(f"Alert: {symbol} at ${price}")
            rules["tracked"] = True
        elif not out_of_range and rules["tracked"]:
            print(f"{symbol} back in range at ${price}")
            rules["tracked"] = False
        else:
            print(f"{symbol}: ${price}")
    
    print("Sleeping for 20 seconds...")
    time.sleep(20)