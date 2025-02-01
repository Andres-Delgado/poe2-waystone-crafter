from classes.priceTable import PriceTable
from classes.craftSheet import CraftSheet

def getExaltedPriceTable() -> PriceTable:
  priceTable = {}

  with open("exalted.csv", "r") as file:
    currencyList = [str(line).strip() for line in file if not line.startswith("#") and len(str(line).strip()) > 0]

    for c in currencyList:
      currency = c.split(',')
      priceTable[currency[0]] = (float(currency[1]), float(currency[2]))

  return PriceTable(priceTable)

def getCraftSheet(sheetName: str) -> CraftSheet:
  itemDict = {}

  with open(sheetName + ".wc", "r") as file:
    itemList = [str(line).strip() for line in file if not line.startswith("#") and len(str(line).strip()) > 0]

    for itemStr in itemList:
      item = itemStr.split(',')

      if len(item[1]):
        itemDict[item[0]] = int(item[1])

  return CraftSheet(itemDict)

if __name__ == '__main__':
  exPriceTable = getExaltedPriceTable()
  exPriceTable.prettyPrint()

  craftSheet = getCraftSheet("craft1")
  craftSheet.prettyPrint()
