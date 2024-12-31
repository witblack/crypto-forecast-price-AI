# Crypto forecast price AI
A simple artificial intelligence (AI) to forecast crypto/carrencies price.

## Price forecast AI Python code usage
1. Make a instance of original class:
```
from forecast_price_class import crypto_price_AI
```
3. Run that class in any format you want:
```
crypto_name = "Crypto name example"  # Example: "SOL-USD"
crypto_price_AI(crypto=crypto_name, period="1d", interval="1m")
crypto_price_AI(crypto=crypto_name, period="1mo", interval="1d")
crypto_price_AI(crypto=crypto_name, period="1y", interval="1mo")
```
