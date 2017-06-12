import database
def init():
    global basket
    basket = []
    global total_items
    total_items = {}

def GetNumber(item):
    return total_items[item]

def GetBasket():
    return basket

# get database
get_inv = database.inv.find()
get_pro = database.pro.find()