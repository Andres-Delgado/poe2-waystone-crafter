class Item:
  def __init__(self, name: str, values: list):
    self.name = name
    self.rateValues = values
    self.rate = float(values[1] / values[0])
    
  def update():
    pass

  def print(self):
    print(f'{self.name}: {round(self.rate, 4)}, {self.rateValues}')
