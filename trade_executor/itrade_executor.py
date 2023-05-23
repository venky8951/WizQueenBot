from abc import ABC, abstractmethod

class ITradeExecutor(ABC):

    @abstractmethod
    def execute(self, symbol, stop_loss, quantity):
        pass
