from classes.craftSheets.distillSheet import DistillSheet
from classes.priceTables.priceTable import PriceTable

class CraftSheet:
  # TODO: add omens

  def __init__(self, sheetDict: dict, priceTable: PriceTable, print: bool = False):
    self.Waystones = sheetDict.get('Waystones', 0)
    self.Normal = sheetDict.get('Normal', 0)
    self.Magic = sheetDict.get('Magic', 0)
    self.Rare = sheetDict.get('Rare', 0)

    # convert all priceTable items to craftItems
    self.Distill = DistillSheet(sheetDict)

    if print: self.print()

  def print(self):
    for name, value in vars(self).items():
      if name == 'Distill':
        print("\nDistill")
        self.Distill.print()
      else:
        print(f'{name}: {value}')
    print()
