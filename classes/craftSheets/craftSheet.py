from classes.craftSheets.distillSheet import DistillSheet
from classes.items.Item import Item
from classes.priceTables.priceTable import PriceTable

class CraftSheet:
  # TODO: add omens

  def __init__(self, sheetDict: dict, priceTable: PriceTable, debug: bool = False):
    self.Waystones = sheetDict.get('Waystones', 0)
    self.Normal = sheetDict.get('Normal', 0)
    self.Magic = sheetDict.get('Magic', 0)
    self.Rare = sheetDict.get('Rare', 0)

    priceTable.Alchemy.update(sheetDict.get('Alchemy', None))
    priceTable.Augmentation.update(sheetDict.get('Augmentation', None))
    priceTable.Regal.update(sheetDict.get('Regal', None))
    priceTable.Vaal.update(sheetDict.get('Vaal', None))
    priceTable.Exalted.update(sheetDict.get('Exalted', None))
    priceTable.Ire.update(sheetDict.get('Ire', None), True)
    priceTable.Guilt.update(sheetDict.get('Guilt', None), True)
    priceTable.Greed.update(sheetDict.get('Greed', None), True)
    priceTable.Paranoia.update(sheetDict.get('Paranoia', None), True)
    priceTable.Envy.update(sheetDict.get('Envy', None), True)
    priceTable.Disgust.update(sheetDict.get('Disgust', None), True)
    priceTable.Despair.update(sheetDict.get('Despair', None), True)
    priceTable.Fear.update(sheetDict.get('Fear', None), True)
    priceTable.Suffering.update(sheetDict.get('Suffering', None), True)
    priceTable.Isolation.update(sheetDict.get('Isolation', None), True)

    self.priceTable: PriceTable = priceTable

    if debug: self.print()

  @staticmethod
  def calculate(self):
    pass

  def print(self):
    for name, value in vars(self.priceTable).items():
      if isinstance(value, Item):
        value: Item
        value.print()
      else:
        print(f'{name}: {value}')
    print()
