class DistillSheet:

  # TODO: Assign tier values
  def __init__(self, sheetDict: dict):
    self.Ire = sheetDict.get('Ire', (0, 0))
    self.Guilt = sheetDict.get('Guilt', (0, 0))
    self.Greed = sheetDict.get('Greed', (0, 0))
    self.Paranoia = sheetDict.get('Paranoia', (0, 0))
    self.Envy = sheetDict.get('Envy', (0, 0))
    self.Disgust = sheetDict.get('Disgust', (0, 0))
    self.Despair = sheetDict.get('Despair', (0, 0))
    self.Fear = sheetDict.get('Fear', (0, 0))
    self.Suffering = sheetDict.get('Suffering', (0, 0))
    self.Isolation = sheetDict.get('Isolation', (0, 0))

  def print(self):
    for name, value in vars(self).items():
      print(f'{name}: {value}')
    print()
