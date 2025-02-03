from classes.items.Item import Item

class CraftItem(Item):
  def __init__(self, item: Item):
    self.name = item.name
    self.rateValues = item.rateValues
    self.rate = item.rate
    
    self.cost = 0
    self.isDistilled = False