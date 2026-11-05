# Devlog — Stock Watchlist Agent

## 2024-11-05

### Architecture decisions
- Started with a single `main.py` instead of pre-planning folder structure — build structure as complexity demands it
- Used `yfinance` over Alpha Vantage — no API key needed, no rate limit, faster to get to the agent-building part
- Swapped Anthropic SDK for Gemini — Anthropic promo credits expired, Gemini free tier works for a practice project
- Alert deduplication: flag-based per ticker — `alerted` flips True on alert, resets to False when price returns to range

### Issues & fixes
- **`google.generativeai` deprecated** — Google moved to `google-genai` package with a different API surface (`genai.Client` instead of `genai.configure`)
- **`gemini-2.0-flash` removed** — model no longer available, switched to `gemini-3.8-flash`
- **Gemini 503 UNAVAILABLE** — free tier gets throttled under high demand. Fix: wrapped `analyze_alert` in try/except so the alert still fires with basic info even when the AI summary fails. Lesson: never let a dependency failure crash your agent

### What's working
- Price fetching loop with 30s interval
- Threshold-based alerts with deduplication
- Gemini-powered alert summaries with error fallback