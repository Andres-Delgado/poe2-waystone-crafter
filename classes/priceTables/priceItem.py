class PriceItem:
  def __init__(self):
    self.name = ''
    self.values = []
    self.rate = 1

  def __init__(self, name: str, values: list):
    self.name = name
    self.values = values
    self.rate = float(values[1] / values[0])

  def prettyPrint(self):
    print(f'{self.name}: {round(self.rate, 4)}, {self.values}')
