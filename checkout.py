import math
import database
import product
import promotion
from setup import *
import setup

def GetRegularPrice(item):
    # database
    for i in database.inv.find({"Product Code": item}):
        return (i["Price"])


def GetPromo(item, nth):
    cost = GetRegularPrice(item)
    reg_price = cost
    name = ""
    current = 0
    # keeep track of the most attracting discount
    if item in promo_dict:
        for promo in promo_dict[item]:
            deal = promo.discount(item, nth)
            current = deal[0]
            if cost > reg_price+float(current):
                cost += current
            else:
                continue
            name = deal[1]
    return (cost, name)


def PrintBasket():
    total = 0.00
    print('Item' + ' '*16 + 'Price')
    print('-'*4 + ' '*16 + '-'*5)
    basket = setup.GetBasket()
    for i in basket:
        total = round(i.regular_price + i.discount + total, 2)
        print(i.item_name + ' '*17 + str(i.regular_price))
        if i.discount != 0:
            print(' '*9 + i.promotion_name + ' '*7 + str(i.discount))
    print ('-'*25)
    print(total)
    print (' '*20 + str(total) + '\n')
    # for testing
    return total

def printHelp():
    # print the inventory list and current promotion
    print ("Here is the inventory and the regular price!")
    for i in item_list:
        print(i)

def setPromoDict():
    for i in get_pro:
        promo = promotion.Promotion(i["Pre Item"], i["Apply Item"], i["Number"], i["Bar Number"], i["Promo Code"],
                                    i["Func"],
                                    i["Limitation"], i["Regular Price"], i["Discount"])
        if i["Pre Item"] == i["Apply Item"]:
            promo_dict[i["Pre Item"]] = []
            promo_dict[i["Pre Item"]].append(promo)
        else:
            promo_dict.setdefault(i["Pre Item"], []).append(promo)
            promo_dict.setdefault(i["Apply Item"], []).append(promo)
    return promo_dict

if __name__== "__main__":

    # number of items purchased indexed by item

    # item list storing items
    item_list = []

    print("Item in Stock")
    for i in get_inv:
        print(i["Product Code"])
        item_list.append(i["Product Code"])

    # storing global variables
    setup.init()

    # store Promotion object, indexed by Preitem or Applyitem or both

    promo_dict = {}

    setPromoDict()
    while True:
        try:
            fruit = input()
        except:
            break
        if (fruit in item_list):
            # store the number of each item bought
            setup.total_items[fruit] = setup.total_items.get(fruit, 0) +1
            reg_price = GetRegularPrice(fruit)
            # PriceandDeal[0] is discount, PriceandDeal[1] is promotion name
            PriceandDeal = GetPromo(fruit, setup.total_items[fruit] )
            theitem = product.Product(fruit, setup.total_items[fruit], PriceandDeal[1] , reg_price, PriceandDeal[0]-reg_price)
            setup.basket.append(theitem)
            PrintBasket()
        elif (fruit == ""):
            break
        elif (fruit == "help"):
            printHelp()
        elif (fruit not in item_list):
            print("Wrong item, Scan again")
        else:
            pass




