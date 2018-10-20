from catalyst import run_algorithm
from catalyst.api import order, record, symbol
import pandas as pd
import matplotlib.pyplot as plt


def initialize(context):
    context.asset = symbol('zil_btc')


def handle_data(context, data):
    order(context.asset, 1)
    record(btc=data.current(context.asset, 'price'))


def analyze(context, perf):
    ax1 = plt.subplot(211)
    perf.portfolio_value.plot(ax=ax1)
    ax1.set_ylabel('portfolio value')
    ax2 = plt.subplot(212, sharex=ax1)
    perf.btc.plot(ax=ax2)
    ax2.set_ylabel('zil price')
    plt.show()


if __name__ == '__main__':
    run_algorithm(
        capital_base=10,
        data_frequency='minute',
        initialize=initialize,
        handle_data=handle_data,
        analyze=analyze,
        algo_namespace='ALGONAMESPACE',
        exchange_name='binance',
        quote_currency='btc',
        live=True,
        simulate_orders=True,
    )
