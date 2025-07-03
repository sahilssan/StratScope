import numpy as np

def calculate_performance(data):
    returns = data['Portfolio_Value'].pct_change().dropna()
    sharpe_ratio = (returns.mean() / returns.std()) * (252 ** 0.5)

    equity_curve = data['Portfolio_Value']
    roll_max = equity_curve.cummax()
    drawdown = (equity_curve - roll_max) / roll_max
    max_drawdown = drawdown.min()

    total_return = (equity_curve.iloc[-1] / equity_curve.iloc[0]) - 1

    return {
        'Sharpe Ratio': sharpe_ratio,
        'Max Drawdown': max_drawdown,
        'Total Return': total_return
    }
