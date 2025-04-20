import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_fake_stock_data(start_price=150, num_days=365):
    """Generates a Pandas DataFrame with fake OHLC data for a given number of days."""
    start_date = datetime(2024, 4, 20)  # Starting from today last year
    dates = [start_date + timedelta(days=i) for i in range(num_days)]
    open_prices = [start_price]
    high_prices = []
    low_prices = []
    close_prices = []

    for _ in range(num_days - 1):
        last_close = open_prices[-1]
        change = np.random.normal(0, 2)  # Simulate a daily price change
        new_open = max(1, last_close + change) # Ensure price stays positive

        high = max(last_close, new_open, new_open + np.random.uniform(0, 3))
        low = min(last_close, new_open, new_open - np.random.uniform(0, 3))
        close = np.clip(new_open + np.random.normal(0, 1.5), low, high)

        open_prices.append(new_open)
        high_prices.append(high)
        low_prices.append(low)
        close_prices.append(close)

    # Append the final high, low, and close for the last day
    high_prices.append(max(open_prices[-1], close_prices[-1] if close_prices else open_prices[-1], open_prices[-1] + np.random.uniform(0, 3)))
    low_prices.append(min(open_prices[-1], close_prices[-1] if close_prices else open_prices[-1], open_prices[-1] - np.random.uniform(0, 3)))
    close_prices.append(np.clip(open_prices[-1] + np.random.normal(0, 1.5), low_prices[-1], high_prices[-1]))

    df = pd.DataFrame({
        'time': dates,
        'open': open_prices,
        'high': high_prices,
        'low': low_prices,
        'close': close_prices
    })
    return df
