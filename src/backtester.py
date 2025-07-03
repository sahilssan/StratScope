import pandas as pd

def backtest(signals, initial_cash=10000):
    portfolio_value = pd.Series(dtype=float)

    for ticker, data in signals.items():
        data['Daily_Return'] = data['Price'].pct_change()
        data['Strategy_Return'] = data['Daily_Return'] * data['Position'].shift(1)
        data['Equity_Curve'] = (1 + data['Strategy_Return'].fillna(0)).cumprod()

        if portfolio_value.empty:
            portfolio_value = data['Equity_Curve']
        else:
            portfolio_value += data['Equity_Curve']

    # Average the portfolio value across all tickers
    portfolio_value = portfolio_value / len(signals)
    portfolio_value = portfolio_value * (initial_cash / portfolio_value.iloc[0])  # Normalize starting value

    portfolio = pd.DataFrame()
    portfolio['Portfolio_Value'] = portfolio_value

    return portfolio
