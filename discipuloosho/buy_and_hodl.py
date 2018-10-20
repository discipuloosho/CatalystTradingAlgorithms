# Buy and Hodl
from catalyst import run_algorithm
from catalyst.api import order, record, symbol
import pandas as pd

# Init
def initialize(context):
    context.asset = symbol('zil_btc')
    context.bought = False

# Execute on each candlextick
def handle_data(context, data):
    if not context.bought:
        order(context.asset, 1000)
        record(zil=data.current(context.asset, 'price'))
        context.bought = True

# Run Algorithm
if __name__ == '__main__':
    run_algorithm(
        capital_base=1,
        data_frequency='minute',
        initialize=initialize,
        handle_data=handle_data,
        exchange_name='binance',
        quote_currency='btc',
        live=False,
        start=pd.to_datetime('2018-06-24', utc=True),
        end=pd.to_datetime('2018-06-25', utc=True)
    )