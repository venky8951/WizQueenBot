from itechnical_indicator import ITechnicalIndicator

class CompositeIndicator(ITechnicalIndicator):

    def __init__(self):
        self.indicators = []

    def add_indicator(self, indicator):
        self.indicators.append(indicator)

    def remove_indicator(self, indicator):
        self.indicators.remove(indicator)

    def calculate(self, data):
        results = {}
        for indicator in self.indicators:
            results[indicator.__class__.__name__] = indicator.calculate(data)
        return results
