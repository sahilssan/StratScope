import pandas as pd

def apply_strategy(data, window=14):
    signals = {}

    for ticker in data.columns:
        temp = pd.DataFrame()
        temp['Price'] = data[ticker]

        delta = temp['Price'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

        rs = gain / loss
        temp['RSI'] = 100 - (100 / (1 + rs))
        temp['Position'] = (temp['RSI'] < 30).astype(int)  # Buy when oversold
        temp['Signal'] = temp['Position'].diff()

        signals[ticker] = temp

    return signals
