from logger import log_portfolio
from data_loader import fetch_sp500_data
from strategy_selector import get_strategy
from backtester import backtest
from plotter import plot_multiple_equity_curves

def run_backtest():
    tickers = ["SPY", "AAPL", "MSFT"]
    strategies = ["moving_average", "rsi"]

    data = fetch_sp500_data(tickers)

    portfolios = {}
    for strategy_name in strategies:
        strategy_function = get_strategy(strategy_name)
        signals = strategy_function(data)
        portfolio = backtest(signals)
        portfolios[strategy_name] = portfolio
        log_portfolio(portfolio, strategy_name)

    plot_multiple_equity_curves(portfolios)

if __name__ == "__main__":
    run_backtest()
