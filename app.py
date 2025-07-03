import streamlit as st
import matplotlib.pyplot as plt
from src.data_loader import fetch_sp500_data
from src.strategy_selector import get_strategy
from src.backtester import backtest

st.title("Quant Strategy Backtester")

# Ticker input
tickers = st.text_input("Enter tickers separated by commas", "SPY, AAPL, MSFT")

# Strategy selection
selected_strategies = st.multiselect(
    "Select strategies",
    ["moving_average", "rsi"],
    default=["moving_average"]
)

# Run button
if st.button("Run Backtest"):
    tickers = [ticker.strip().upper() for ticker in tickers.split(",")]
    data = fetch_sp500_data(tickers)

    portfolios = {}
    for strategy_name in selected_strategies:
        strategy_function = get_strategy(strategy_name)
        signals = strategy_function(data)
        portfolio = backtest(signals)
        portfolios[strategy_name] = portfolio

    st.subheader("Portfolio Performance")
    fig, ax = plt.subplots(figsize=(12, 6))

    for strategy_name, portfolio in portfolios.items():
        ax.plot(portfolio.index, portfolio['Portfolio_Value'], label=strategy_name)

    ax.set_title('Strategy Performance Comparison')
    ax.set_xlabel('Date')
    ax.set_ylabel('Portfolio Value')
    ax.legend()
    ax.grid()

    st.pyplot(fig)
