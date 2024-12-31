"""     libs    """
# External
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from pandas import to_datetime
from yfinance import download


"""     Get price & forecast price"""
# Notes:
#   period can be once: ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', 'ytd', 'max']
#   Interval can be once: ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
class crypto_price_AI:
    def __init__(self, crypto: str = "SOL-USD", period: str = "1y", interval: str = "1d", show_in_multiple_windows: bool = False):
        # Setting up values
        self.data = download(crypto, period=period, interval=interval)
        self.interval = interval
        self.period = period
        self.crypto = crypto
        # Go process
        if show_in_multiple_windows:
            self.preview_data()
        self.forecast_future_price()

    def preview_data(self):
        plt.figure(figsize=(10, 6))
        # Fill chart with close price
        plt.plot(self.data['Close'])
        # Set page title
        plt.title(f"Price of {self.crypto}, Period: {self.period}, Interval: {self.interval}")
        # Set label for x/y
        plt.xlabel('Date')
        plt.ylabel(f"{self.crypto} Price")
        # Show dialog page
        plt.legend()
        plt.grid()
        plt.show()

    def forecast_future_price(self):
        # Get close prices
        data = self.data[['Close']].dropna()
        # Convert date to standard format
        data['Date'] = to_datetime(data.index)
        data['Date_ordinal'] = data['Date'].apply(lambda date: date.toordinal())
        # Extract x/y data from sheet
        date_frames = data['Date_ordinal'].values.reshape(-1, 1)
        price_frames = data['Close'].values
        # Forecast next price
        model = LinearRegression()
        model.fit(date_frames, price_frames)
        data['Predicted'] = model.predict(date_frames)
        plt.figure(figsize=(10, 6))
        # Forecast buy/sell action
        data_list = list(data['Predicted'])[-2:]
        if data_list[-2] > data_list[-1]:
            # Market is down
            time_to_buy = True
        elif data_list[-2] < data_list[-1]:
            # Market is up
            time_to_buy = False
        else:
            # Market is equal
            time_to_buy = None
        # Set x/y values
        plt.plot(data['Close'], label=f"Real {self.crypto} price", color='blue')
        plt.plot(data['Predicted'], label='Model forecast', color='red', linestyle='--')
        # Set page title
        plt.title(f'Linear-Regression model, Forecast of price, Period: {self.period}, Interval: {self.interval}, Time to buy: {time_to_buy}')
        # Set label for x/y
        plt.xlabel('Date')
        plt.ylabel(f"Price of {self.crypto}")
        # Show dialog page
        plt.legend()
        plt.grid()
        plt.show()
