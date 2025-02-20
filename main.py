from product import Product

csvFile = open("products-data.csv", "r")
lines = csvFile.readlines()
csvFile.close()

logFile = open("outputLog.txt", "a")

products = []
lines = lines[1:] # remove first line (contains headers)

for line in lines:
  newProduct = Product(line)
  products.append(newProduct)
  #print(newProduct.sourceURLs.replace('^', ','))


uniqueIds = []

for product in products:
  try:
    if uniqueIds.index(product.id) >= 0:
      logFile.write("%s already exists\n" % product.id)
  except ValueError:
    uniqueIds.append(product.id)

print("there are %d unique product ids" % len(uniqueIds))

pricesAvailability = []

for product in products:
  try:
    if pricesAvailability.index(product.availability) >= 0:
      logFile.write("%s already exists\n" % product.availability)
  except ValueError:
    pricesAvailability.append(product.availability)

print("there are %d unique price availabilities" % len(pricesAvailability))
    
for data in pricesAvailability:
  logFile.write(data + "\n")

for product in products:
  if product.availability.lower() == "yes":
    product.availability = True
  elif product.availability.lower() == "in stock":
    product.availability = True
  elif product.availability.lower() == "true":
    product.availability = True
  elif product.availability.lower() == "out of stock":
    product.availability = False
  elif product.availability.lower() == "undefined":
    product.availability = False
  elif product.availability.lower() == "special order":
    product.availability = True
  elif product.availability.lower() == "no":
    product.availability = False
  elif product.availability.lower() == "more on the way":
    product.availability = True
  elif product.availability.lower() == "sold":
    product.availability = False
  elif product.availability.lower() == "false":
    product.availability = False
  elif product.availability.lower() == "retired":
    product.availability = False
  elif product.availability.lower() == "32 available":
    product.availability = True
  elif product.availability.lower() == "7 available":
    product.availability = True
  else:
    product.availability = False

for product in products:
  logFile.write(str(product.availability) + "\n")

for product in products:
  if product.condition.lower() == "new":
    product.condition = "New"
  elif "refurbished" in product.condition.lower():
    product.condition = "Refurbished"
  elif product.condition.lower() == "used":
    product.condition = "Used"
  elif product.condition.lower() == "pre-owned":
    product.condition = "Used"
    product.condition = "Refurbished"
  elif product.condition.lower() == "new other (see details)":
    product.condition = "New"
  elif product.condition.lower() == "refurbished":
    product.condition = "Refurbished"
  else:
    product.condition = "Unknown"

uniqueConditions = []
for product in products:
  try:
    if uniqueConditions.index(product.condition) >= 0:
      logFile.write("%s condition exists\n" % product.condition)
  except ValueError:
    uniqueConditions.append(product.condition)

for uc in uniqueConditions:
  logFile.write(uc + "\n")

for product in products:
  if product.isSale == "TRUE":
    product.isSale = True
  else:
    product.isSale = False
  logFile.write(str(product.isSale) + "\n")

rawUniqueAsins = []
for product in products:
  try:
    if rawUniqueAsins.index(product.asins) >= 0:
      logFile.write("%s asins exists\n" % product.asins)
  except ValueError:
    rawUniqueAsins.append(product.asins)

for asin in rawUniqueAsins:
  logFile.write(asin + "\n")
print("unique asins = %d" % len(rawUniqueAsins))

rawUniqueBrands = []
for product in products:
  try:
    if rawUniqueBrands.index(product.brand) >= 0:
      logFile.write("%s brand exists\n" % product.brand)
  except ValueError:
    rawUniqueBrands.append(product.brand)

for brand in rawUniqueBrands:
  logFile.write(brand + "\n")
print("unique brands = %d" % len(rawUniqueBrands))

rawUniqueManufacturerNumber = []
for product in products:
  try:
    if rawUniqueManufacturerNumber.index(product.manufacturerNumber) >= 0:
      logFile.write("%s manufacturer num exists\n" % product.manufacturerNumber)
  except ValueError:
    rawUniqueManufacturerNumber.append(product.manufacturerNumber)

for manufacturerNumber in rawUniqueManufacturerNumber:
  logFile.write(manufacturerNumber + "\n")
print("there are %d unique manufacturer's numbers" % len(rawUniqueManufacturerNumber))


foundProducts = []
for product in products:
  if product.id == "AVpgNkVc1cnluZ0-yJB6":
    foundProducts.append(product)
print("there are %d products with id = AVpgNkVc1cnluZ0-yJB6" % len(foundProducts))
printProducts = input("print Products? ")
if printProducts == "y":
  for product in foundProducts:
    print("%s %s" % (product.name, product.minAmount))
logFile.close()