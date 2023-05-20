from stock_filter import StockFilter
from bhav_data_fetch import BhavDataFetch

# Get the nearest month end date
nearest_month_end = '25-May-2023'

class OIFilter(StockFilter):

    def filter(self, stock_data):

        # Filter stocks based on price and open interest changes
        filtered_stocks = []
        today_data,yesterday_data = BhavDataFetch.fetch_all_stock_data()
        for symbol in today_data['SYMBOL'].unique():
            today_df = today_data[today_data['SYMBOL'] == symbol]
            yesterday_df = yesterday_data[yesterday_data['SYMBOL'] == symbol]


            # Calculate percentage changes from previous day
            today_df['PRICE_CHANGE'] = (today_df['CLOSE'] - yesterday_df['CLOSE']) / yesterday_df['CLOSE'] * 100
            today_df['OI_CHANGE'] = (today_df['OPEN_INT'] - yesterday_df['OPEN_INT']) / yesterday_df['OPEN_INT'] * 100

            # Filter stocks based on criteria
            filtered_df = today_df[(today_df['PRICE_CHANGE'] >= 2) & (today_df['OI_CHANGE'] >= 10) & (today_df['EXPIRY_DT'] == nearest_month_end) & ((today_df['INSTRUMENT'] == 'FUTIDX') | (today_df['INSTRUMENT'] == 'FUTSTK'))]

            if not filtered_df.empty:
                filtered_stocks.append(symbol)

        # Print the filtered stocks
        print("Filtered Stocks:")
        for stock in filtered_stocks:
            print(stock)
        return filtered_stocks
