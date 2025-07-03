import schedule
import time
import datetime
from main import run_backtest

def job():
    print(f"Running backtest at {datetime.datetime.now()}")
    run_backtest()

# Run daily at 6:00 AM (you can customize this)
schedule.every().day.at("06:00").do(job)

print("Scheduler started. Waiting for next run...")

while True:
    schedule.run_pending()
    time.sleep(60)
