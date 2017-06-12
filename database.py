import pymongo
# Create an instance of the MongoClient, a database called checkout,
# a collection called inventory for product information, and promotion
# collection for promotion info
client = pymongo.MongoClient()
db = client.checkout
inv = db.inventory
pro = db.promotion

db.inventory.remove({})
db.promotion.remove({})

inv = db.inventory
pro = db.promotion

# Here is the inventory list based on the product information
inventory_list = [
    {"Product Code": "CH1", "Name": "Chai", "Price": 3.11},
    {"Product Code": "AP1", "Name": "Apples", "Price": 6.00},
    {"Product Code": "CF1", "Name": "Coffee", "Price": 11.23},
    {"Product Code": "MK1", "Name": "Milk", "Price": 4.75},
    {"Product Code": "OM1", "Name": "Oatmeal", "Price": 3.69}]

promotion_list = [
    {"Promo Code": "BOGO", "Pre Item": "CF1", "Apply Item": "CF1", "Number": 2, "Bar Number": 0, "Func": "",
     "Limitation": 0, "Regular Price": 11.23, "Discount": 11.23},

    {"Promo Code": "APPL", "Pre Item": "AP1", "Apply Item": "AP1", "Number": 1, "Bar Number": 3, "Func": "UpdatePrice",
     "Limitation": 0, "Regular Price": 6.00, "Discount": 1.5},

    {"Promo Code": "CHMK", "Pre Item": "CH1", "Apply Item": "MK1", "Number": 1, "Bar Number": 1, "Func": "UpdatePrice",
     "Limitation": 1, "Regular Price": 4.75, "Discount": 4.75},

    {"Promo Code": "APOM", "Pre Item": "OM1", "Apply Item": "AP1", "Number": 1, "Bar Number": 1, "Func": "UpdatePrice",
     "Limitation": 1, "Regular Price": 6.00, "Discount": "50%"}]

inv.insert(inventory_list)
pro.insert(promotion_list)
