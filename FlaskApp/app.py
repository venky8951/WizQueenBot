from flask import Flask
from source_configurator.OI_filter import OIFilter
from trade_executor.jugaad_trade_executor import JugaadTradeExecutor
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

@app.route('/')
def hello():
    filtered_stocks= OIFilter().filter(stock_data=any)
    for stock in filtered_stocks:
        JugaadTradeExecutor().gtt(symbol=stock)
    return filtered_stocks


def test():
    print("invoked")

sched = BackgroundScheduler(daemon=True)
sched.add_job(test,'interval',minutes=10)
sched.start()

app.run(port=5001)