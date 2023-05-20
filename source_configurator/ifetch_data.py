from abc import ABC, abstractmethod

class IFetchData(ABC):

    @abstractmethod
    def fetch_stock_data(self, symbol, start_date, end_date):
        pass
