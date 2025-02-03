from classes.priceTables.priceTable import PriceTable
from classes.craftSheets.craftSheet import CraftSheet

def getExaltedPriceTable() -> PriceTable:
  priceTable = {}

  with open("exalted.csv", "r") as file:
    currencyList = [str(line).strip() for line in file if not line.startswith("#") and len(str(line).strip()) > 0]

    for c in currencyList:
      currency = c.split(',')
      priceTable[currency[0]] = (float(currency[1]), float(currency[2]))

  return PriceTable(priceTable)

def getCraftSheet(sheetName: str, priceTable: PriceTable) -> CraftSheet:
  itemDict = {}

  with open(sheetName + ".wc", "r") as file:
    itemList = [str(line).strip() for line in file if not line.startswith("#") and len(str(line).strip()) > 0]

    for itemStr in itemList:
      item = itemStr.split(',')

      if len(item) == 2 and len(item[1]):
        itemDict[item[0]] = int(item[1])

      elif len(item) == 3:
        itemDict[item[0]] = (int(item[1]), int(item[2]))

  return CraftSheet(itemDict, priceTable, True)

if __name__ == '__main__':
  exPriceTable = getExaltedPriceTable()
  exPriceTable.print()

  craftSheet = getCraftSheet("craft1", exPriceTable)
