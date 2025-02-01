import json

def getExaltedPriceTable() -> dict:
  priceTable = {}

  with open("exalted.csv", "r") as file:
    currencyList = [str(line).strip() for line in file if not line.startswith("#") and len(str(line).strip()) > 0]

    for c in currencyList:
      currency = c.split(',')

      # TODO: initialize Price Object
      priceTable[currency[0]] = (float(currency[1]), float(currency[2]))

  return priceTable

def getCraftSheet(sheetName: str) -> dict:
  itemDict = {}

  with open(sheetName + ".wc", "r") as file:
    itemList = [str(line).strip() for line in file if not line.startswith("#") and len(str(line).strip()) > 0]

    for itemStr in itemList:
      item = itemStr.split(',')
      if len(item[1]):
        itemDict[item[0]] = int(item[1])


  return itemDict

if __name__ == '__main__':
  exPriceTable = getExaltedPriceTable()
  print(json.dumps(exPriceTable, indent=2), end='\n\n')
  print()

  craftSheet = getCraftSheet("craft1")
  print(json.dumps(craftSheet, indent=2))
