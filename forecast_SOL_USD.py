"""     libs        """
# External
from forecast_price_class import crypto_price_AI


"""     Run & price forecast      """
crypto_name = "SOL-USD"
crypto_price_AI(crypto=crypto_name, period="1d", interval="1m")
crypto_price_AI(crypto=crypto_name, period="1mo", interval="1d")
crypto_price_AI(crypto=crypto_name, period="1y", interval="1mo")