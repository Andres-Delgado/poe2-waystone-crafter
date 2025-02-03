import math


class Item:
  def __init__(self, name: str, values: list):
    self.name: str = name
    self.rateValues: list = values
    self.rate: float = float(values[1] / values[0])

    self.needed: int = 0
    self.aquired: int = 0
    self.costEstimated: int = 0
    self.costActual: int = 0
    self.isDistilled: bool = False
    
  def update(self, tuple: tuple, isDistilled: bool = False):
    if tuple is None or len(tuple) != 2:
      return

    self.needed: int = tuple[0]
    self.aquired: int = tuple[1]
    self.costEstimated: int = math.ceil(self.needed * self.rate)
    self.costActual: int = math.ceil((self.needed - self.aquired) * self.rate)
    self.isDistilled: bool = isDistilled

  def print(self):
    print(f'{self.name}: {round(self.rate, 4)}, {self.rateValues}, {self.needed}, {self.costEstimated}, {self.costActual}')
