import yfinance as yf

WATCHLIST = {
    "AAPL": {"alert_below": 300, "alert_above": 350, "tracked": False},
    "NVDA": {"alert_below": 250, "alert_above": 300, "tracked": False},
    "MSFT": {"alert_below": 220, "alert_above": 250, "tracked": False},
}

for symbol, rules in WATCHLIST.items():
    price = yf.Ticker(symbol).info["currentPrice"]
    
    if not rules["tracked"]:
        if price < rules["alert_below"]:
            print(f"Alert: {symbol} price is below {rules['alert_below']}. Current price: {price}")
        elif price > rules["alert_above"]:
            print(f"Alert: {symbol} price is above {rules['alert_above']}. Current price: {price}")
        else:
            print(f"{symbol} price is within the alert range. Current price: {price}")
        
        # setting tracked to true to avoid repeated alerts
        rules["tracked"] = True
    else:
        print("Nothing new to report.")