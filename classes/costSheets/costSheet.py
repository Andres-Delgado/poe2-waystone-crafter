from classes.craftSheets.craftSheet import CraftSheet
from classes.priceTables.priceTable import PriceTable

class CostSheet:
  def __init__(self, priceTable: PriceTable, craftSheet: CraftSheet):
    self.priceTable = priceTable
    self.craftSheet = craftSheet
