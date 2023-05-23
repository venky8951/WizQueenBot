from abc import ABC, abstractmethod

class ITechnicalIndicator(ABC):

    @abstractmethod
    def calculate(self, data):
        pass
