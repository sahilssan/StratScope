import matplotlib.pyplot as plt

def plot_equity_curve(portfolio):
    plt.figure(figsize=(12, 6))
    plt.plot(portfolio.index, portfolio['Portfolio_Value'], label='Portfolio Equity Curve', color='blue')
    plt.title('Portfolio Equity Curve')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.legend()
    plt.grid()
    plt.show()

def plot_multiple_equity_curves(portfolios):
    plt.figure(figsize=(12, 6))

    for strategy_name, portfolio in portfolios.items():
        plt.plot(portfolio.index, portfolio['Portfolio_Value'], label=strategy_name)

    plt.title('Strategy Performance Comparison')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.legend()
    plt.grid()
    plt.show()