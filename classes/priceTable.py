class PriceTable:

  def __init__(self):
    # TODO: add omens
    self.Alchemy = [0, 0]
    self.Augmentation = [0, 0]
    self.Regal = [0, 0]
    self.Vaal = [0, 0]
    self.Exalted = [0, 0]

    self.Ire = [0, 0]
    self.Guilt = [0, 0]
    self.Greed = [0, 0]
    self.Paranoia = [0, 0]
    self.Envy = [0, 0]
    self.Disgust = [0, 0]
    self.Despair = [0, 0]
    self.Fear = [0, 0]
    self.Suffering = [0, 0]
    self.Isolation = [0, 0]

  def __init__(self, ptDict: dict):
    self.Alchemy = ptDict['Alchemy']
    self.Augmentation = ptDict['Augmentation']
    self.Regal = ptDict['Regal']
    self.Vaal = ptDict['Vaal']
    self.Exalted = ptDict['Exalted']

    self.Ire = ptDict['Ire']
    self.Guilt = ptDict['Guilt']
    self.Greed = ptDict['Greed']
    self.Paranoia = ptDict['Paranoia']
    self.Envy = ptDict['Envy']
    self.Disgust = ptDict['Disgust']
    self.Despair = ptDict['Despair']
    self.Fear = ptDict['Fear']
    self.Suffering = ptDict['Suffering']
    self.Isolation = ptDict['Isolation']

  def prettyPrint(self):
    for name, value in vars(self).items():
      print(f'{name}: [{value[0]}, {value[1]}]')
    print()
