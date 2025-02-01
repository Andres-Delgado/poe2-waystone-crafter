from classes.priceTables.priceItem import PriceItem

class PriceTable:

  def __init__(self):
    # TODO: add omens
    self.Alchemy = PriceItem('Alchemy', [1, 1])
    self.Augmentation = PriceItem('Augmentation', [1, 1])
    self.Regal = PriceItem('Regal', [1, 1])
    self.Vaal = PriceItem('Vaal', [1, 1])
    self.Exalted = PriceItem('Exalted', [1, 1])

    self.Ire = PriceItem('Ire', [1, 1])
    self.Guilt = PriceItem('Guilt', [1, 1])
    self.Greed = PriceItem('Greed', [1, 1])
    self.Paranoia = PriceItem('Paranoia', [1, 1])
    self.Envy = PriceItem('Envy', [1, 1])
    self.Disgust = PriceItem('Disgust', [1, 1])
    self.Despair = PriceItem('Despair', [1, 1])
    self.Fear = PriceItem('Fear', [1, 1])
    self.Suffering = PriceItem('Suffering', [1, 1])
    self.Isolation = PriceItem('Isolation', [1, 1])

  def __init__(self, ptDict: dict):
    self.Alchemy = PriceItem('Alchemy', ptDict['Alchemy'])
    self.Augmentation = PriceItem('Augmentation', ptDict['Augmentation'])
    self.Regal = PriceItem('Regal', ptDict['Regal'])
    self.Vaal = PriceItem('Vaal', ptDict['Vaal'])
    self.Exalted = PriceItem('Exalted', ptDict['Exalted'])

    self.Ire = PriceItem('Ire', ptDict['Ire'])
    self.Guilt = PriceItem('Guilt', ptDict['Guilt'])
    self.Greed = PriceItem('Greed', ptDict['Greed'])
    self.Paranoia = PriceItem('Paranoia', ptDict['Paranoia'])
    self.Envy = PriceItem('Envy', ptDict['Envy'])
    self.Disgust = PriceItem('Disgust', ptDict['Disgust'])
    self.Despair = PriceItem('Despair', ptDict['Despair'])
    self.Fear = PriceItem('Fear', ptDict['Fear'])
    self.Suffering = PriceItem('Suffering', ptDict['Suffering'])
    self.Isolation = PriceItem('Isolation', ptDict['Isolation'])

  def prettyPrint(self):
    for name, value in vars(self).items():
      value.prettyPrint()
    print()
