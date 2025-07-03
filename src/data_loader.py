import yfinance as yf
import pandas as pd

def fetch_sp500_data(tickers=["SPY"], period="5y", interval="1d"):
    data = yf.download(tickers, period=period, interval=interval, group_by='ticker', auto_adjust=False)

    # Prepare an empty DataFrame to store prices
    price_data = pd.DataFrame()

    for ticker in tickers:
        ticker_data = data[ticker] if len(tickers) > 1 else data
        if isinstance(ticker_data.columns, pd.MultiIndex):
            ticker_data.columns = [' '.join(col).strip() for col in ticker_data.columns.values]

        price_column = None
        for col in ticker_data.columns:
            if 'Adj Close' in col:
                price_column = col
                break
            elif 'Close' in col:
                price_column = col

        if price_column is None:
            raise KeyError(f"No usable price column found for {ticker}: {ticker_data.columns}")

        temp = ticker_data[[price_column]].rename(columns={price_column: ticker})
        price_data = pd.concat([price_data, temp], axis=1)

    price_data.dropna(inplace=True)
    return price_data
