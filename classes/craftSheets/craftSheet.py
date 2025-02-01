from classes.craftSheets.distillSheet import DistillSheet

class CraftSheet:
  def __init__(self):
    self.Waystones = 0
    self.Normal = 0
    self.Magic = 0
    self.Rare = 0
    self.Distill = DistillSheet()
    # TODO: add omens

  def __init__(self, sheetDict: dict, prettyPrint: bool = False):
    self.Waystones = sheetDict.get('Waystones', 0)
    self.Normal = sheetDict.get('Normal', 0)
    self.Magic = sheetDict.get('Magic', 0)
    self.Rare = sheetDict.get('Rare', 0)
    self.Distill = DistillSheet(sheetDict)

  def prettyPrint(self):
    for name, value in vars(self).items():
      if name == 'Distill':
        print("\nDistill")
        self.Distill.prettyPrint()
      else:
        print(f'{name}: {value}')
    print()
