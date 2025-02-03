from classes.items.Item import Item

class PriceTable:
  def __init__(self, ptDict: dict):
    self.Alchemy = Item('Alchemy', ptDict['Alchemy'])
    self.Augmentation = Item('Augmentation', ptDict['Augmentation'])
    self.Regal = Item('Regal', ptDict['Regal'])
    self.Vaal = Item('Vaal', ptDict['Vaal'])
    self.Exalted = Item('Exalted', ptDict['Exalted'])

    self.Ire = Item('Ire', ptDict['Ire'])
    self.Guilt = Item('Guilt', ptDict['Guilt'])
    self.Greed = Item('Greed', ptDict['Greed'])
    self.Paranoia = Item('Paranoia', ptDict['Paranoia'])
    self.Envy = Item('Envy', ptDict['Envy'])
    self.Disgust = Item('Disgust', ptDict['Disgust'])
    self.Despair = Item('Despair', ptDict['Despair'])
    self.Fear = Item('Fear', ptDict['Fear'])
    self.Suffering = Item('Suffering', ptDict['Suffering'])
    self.Isolation = Item('Isolation', ptDict['Isolation'])

  def print(self):
    for _,  value in vars(self).items():
      value: Item
      value.print()
    print()
