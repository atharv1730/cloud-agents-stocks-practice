import time
import yfinance as yf
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_alert(symbol, price, rule_type, threshold):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"{symbol} is at ${price} which is {rule_type} the threshold of ${threshold}. Give a 2 sentence summary - what happened and what the user should look at"
    )
    return response.text

WATCHLIST = {
    "AAPL": {"alert_below": 200, "alert_above": 250, "alerted": False},
    "NVDA": {"alert_below": 250, "alert_above": 300, "alerted": False},
    "MSFT": {"alert_below": 220, "alert_above": 250, "alerted": False},
}

while True:
    for symbol, rules in WATCHLIST.items():
        price = yf.Ticker(symbol).info["currentPrice"]
        out_of_range = price < rules["alert_below"] or price > rules["alert_above"]

        if out_of_range and not rules["alerted"]:
            rule_type = "below" if price < rules["alert_below"] else "above"
            threshold = rules["alert_below"] if price < rules["alert_below"] else rules["alert_above"]
            msg = analyze_alert(symbol, price, rule_type, threshold)
            print(f"{msg}")
            rules["alerted"] = True
        elif not out_of_range and rules["alerted"]:
            print(f"{symbol} back in range at ${price} — re-armed")
            rules["alerted"] = False
        else:
            print(f"{symbol}: ${price}")

    print("--- sleeping 30s ---")
    time.sleep(30)