class Product:
  def __init__(self, line):
    columns = line.split(",")
    # CSV split by comma
    self.id = columns[0]
    self.maxAmount = columns[1]
    self.minAmount = columns[2]
    self.availability = columns[3]
    self.condition = columns[4]
    self.currency = columns[5]
    self.dateSeen = columns[6] # TODO convert to date object
    self.isSale = columns[7]
    self.merchant = columns[8]
    self.shipping = columns[9]
    self.priceSourceURLs = columns[10]
    self.asins = columns[11]
    self.brand = columns[12]
    self.categories = columns[13]
    self.dateAdded = columns[14] # TODO convert to date object
    self.dateUpdated = columns[15] # TODO convert to date object
    self.ean = columns[16]
    self.imageURLs = columns[17]
    self.keys = columns[18]
    self.manufacturer = columns[19]
    self.manufacturerNumber = columns[20]
    self.name = columns[21]
    self.primaryCategories = columns[22]
    self.sourceURLs = columns[23]
    self.upc = columns[24]
    self.weight = columns[25]
    