# Quant Backtester

Minimal Python-based quant strategy backtester.

# StratScope – Quant Strategy Backtester

StratScope is a Python-based quantitative strategy backtester with a live Streamlit web interface. It supports multi-ticker, multi-strategy backtesting, automated performance logging, and real-time portfolio visualization.

---

## 🚀 Features
- Multi-ticker backtesting
- Modular strategy selection (Moving Average, RSI)
- Real-time portfolio performance visualization
- Automated daily logging and email summaries
- Deployed on Streamlit Cloud for public access

---

## 🌐 Live App
[Launch StratScope](https://stratscope-hycyxrjm4iyzabkctpqcec.streamlit.app/)

---

## 📸 Preview

---

## 📂 Project Structure
```plaintext
StratScope/
├── app.py                # Streamlit web app
├── src/                  # Backtesting engine, strategies, logger, scheduler
│   ├── backtester.py
│   ├── data_loader.py
│   ├── email_sender.py
│   ├── logger.py
│   ├── metrics.py
│   ├── plotter.py
│   ├── scheduler.py
│   ├── strategy_selector.py
│   └── strategies/
│       ├── moving_average.py
│       └── rsi.py
├── logs/                 # Portfolio logs
├── requirements.txt      # Project dependencies
├── Dockerfile            # (Optional: for future containerization)
├── README.md
└── .gitignore
