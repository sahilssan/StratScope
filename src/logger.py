import pandas as pd
import os
from datetime import datetime
from metrics import calculate_performance
from email_sender import send_email  # Add this import

def log_portfolio(portfolio, strategy_name):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{log_dir}/{strategy_name}_log.csv"

    # Calculate performance metrics
    performance = calculate_performance(portfolio)

    log_entry = pd.DataFrame([{
        "Date": today,
        "Portfolio_Value": portfolio['Portfolio_Value'].iloc[-1],
        "Sharpe_Ratio": performance['Sharpe Ratio'],
        "Max_Drawdown": performance['Max Drawdown'],
        "Total_Return": performance['Total Return']
    }])

    if os.path.exists(filename):
        log_entry.to_csv(filename, mode='a', header=False, index=False)
    else:
        log_entry.to_csv(filename, index=False)

    print(f"Logged {strategy_name}: {log_entry.iloc[0].to_dict()}")

    # ====== Email Section ======
    from_email = "sahilsandasani@gmail.com"
    to_email = "sahilsandasani@gmail.com"
    app_password = "elyssxxczhxmtdkn"  # No spaces!

    email_subject = f"Portfolio Update: {strategy_name}"
    email_body = f"""Portfolio Log for {strategy_name}

Date: {log_entry.iloc[0]['Date']}
Portfolio Value: {log_entry.iloc[0]['Portfolio_Value']}
Sharpe Ratio: {log_entry.iloc[0]['Sharpe_Ratio']}
Max Drawdown: {log_entry.iloc[0]['Max_Drawdown']}
Total Return: {log_entry.iloc[0]['Total_Return']}
"""

    send_email(email_subject, email_body, to_email, from_email, app_password)
