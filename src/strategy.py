import pandas as pd

def moving_average_strategy(data, window=20):
    signals = {}

    for ticker in data.columns:
        temp = pd.DataFrame()
        temp['Price'] = data[ticker]
        temp['MA'] = temp['Price'].rolling(window=window).mean()
        temp['Position'] = (temp['Price'] > temp['MA']).astype(int)
        temp['Signal'] = temp['Position'].diff()

        signals[ticker] = temp

    return signals
