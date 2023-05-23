from trade_executor.itrade_executor import ITradeExecutor
from jugaad_trader import Zerodha
from source_configurator.stock_filter import StockFilter
kite = Zerodha()

class JugaadTradeExecutor(ITradeExecutor):

    def execute(self, symbol, stop_loss, quantity):
        order_resp = kite.place_order(variety=kite.VARIETY_REGULAR,
			tradingsymbol=symbol,
			exchange=kite.EXCHANGE_NSE,
			transaction_type=kite.TRANSACTION_TYPE_BUY,
			quantity=1,
			order_type=kite.ORDER_TYPE_MARKET,
			product=kite.PRODUCT_CNC,
            trailing_stoploss=stop_loss)
        print(order_resp)
    def gtt(self,symbol):
        kite.set_access_token()
        ORDER= [
			{
			"exchange":"NSE",
			"tradingsymbol": symbol,
			"transaction_type": kite.TRANSACTION_TYPE_BUY,
			"quantity": 1,
			"order_type": "LIMIT",
			"product": "NRML",
			"price": 10000
			}]
        trigger_id = kite.place_gtt(trigger_type=kite.GTT_TYPE_SINGLE,
                            tradingsymbol=symbol, 
                            exchange='NSE',
                            trigger_values=[10001],
                            last_price=9000,orders=ORDER)
