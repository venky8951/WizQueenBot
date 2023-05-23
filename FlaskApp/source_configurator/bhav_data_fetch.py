import pandas as pd
from source_configurator.ifetch_data import IFetchData
from datetime import date, timedelta
from jugaad_data.nse import bhavcopy_fo_save


class BhavDataFetch(IFetchData):
    def fetch_stock_data(self, symbol, start_date, end_date):
        pass

    def fetch_all_stock_data(self, start_date, end_date):
        # Get today's and yesterday's dates
        today = date(2023, 5, 19)
        yesterday = today - timedelta(days=1)
        today_bhav_path = "../Artifacts/fo" + today.strftime("%d%b%Y") + "bhav.csv"
        yesterday_bhav_path = "fo" + yesterday.strftime("%d%b%Y") + "bhav.csv"
        output_directory = "../Artifacts"

        bhavcopy_fo_save(yesterday, output_directory)
        bhavcopy_fo_save(today, output_directory)

        # Load the bhavcopy data from the Excel files
        today_data = pd.read_csv(today_bhav_path)
        yesterday_data = pd.read_csv(yesterday_bhav_path)
        return today_data, yesterday_data