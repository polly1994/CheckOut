import pymongo

#Create an instance of the MongoClient, and a database called checkout and a
#collection called inventory
client = pymongo.MongoClient()
db = client.checkout
inv = db.inventory

#Here is the inventory list based on the product information
inventory_list = [
{"Product Code": "CH1", "Name": "Chai", "Price": 3.11},
{"Product Code": "AP1", "Name": "Apples", "Price": 6.00},
{"Product Code": "CF1", "Name": "Coffee", "Price": 11.23},
{"Product Code": "MK1", "Name": "Milk", "Price": 4.75},
{"Product Code": "OM1", "Name": "Oatmeal", "Price": 3.69}]

"""
1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples

promotion_list = [
{"Promo Code": "BOGO", "Buy Item": "Coffee" ,"func": "BuyNGetN", "number": 2, "Price drop": 0, "Apply Item": "Coffee"  },
{"Promo Code": "APPL", "Buy Item": "Apple", "func": None , "Buy n": ,"Get n":, "Price drop":, "Apply Item"  },
{"Promo Code": "CHMK", "Buy Item": "Chai", "limit": 1,"func": None, "Buy n": ,"Get n":, "Price drop":, "Apply Item"  },
{"Promo Code": "APOM", "Buy Item": "Oatmeal", "func": None, "Buy n": ,"Get n":, "Price drop":, "Apply Item"  }
]
    #{ "Buy Item": ,"Apply Item":
    # "number", "bar_number":  "Promo Code"
    #  "func": , limitation
    #  "regular price", "Price drop": 0:},
"""
class Promotion:

    #pre_item is the item you have to have before another item can apply the promotion
    #apply_item is the item gonna have the discount
    #number means the nth item will have the promotion, number = 1 inplies every apply_item could have promotion if they qualify
    #bar_number is the quantity that the pre_item has to reach in order to have the promotion
    #discount could be either float or string if the discount is a percentage
    def __init__(self, pre_item, apply_item, number, bar_number, promo_name, expr, limitation, regular_price, discount = 0):
        self.pre_item = pre_item
        self.apply_item = apply_item
        self.number = number
        self.bar_number = bar_number
        self.name = promo_name
        if type(discount) is str:
            f = (float(discount[:-1]))
            discount = f/100*regular_price
        self.save = discount
        self.func = expr
        self.limitation = limitation
        self.regular_price = regular_price

    def LimitationBool(self, num):
        print("number and limitation")
        print(num, self.limitation)
        if num > self.limitation and self.limitation!= 0 :
            return False
        else:
            return True

    def promoDoesApply(self, buy_item, num, bar_number):
        global total_items
        print ("self.pre_item, self.apply_item")
        print (self.pre_item, self.apply_item)
        print ("\n")
        if self.LimitationBool(num):
            print ("11111111")
            print("self.pre_item, self.apply_item, self.buy_item")
            print(self.pre_item, self.apply_item, buy_item)
            print("\n")

            if self.pre_item != self.apply_item and buy_item == self.apply_item :
                print("222222222")

                try:
                    number_buy_item = total_items[self.pre_item]
                    print("number_buy_item, bar_number")
                    print(number_buy_item, bar_number)
                    print("\n")

                    if number_buy_item >= bar_number:
                        return num % self.number == 0
                    print("3333333")
                    print("\n")


                except:
                    print("444444")
                    print("\n")

                    return False
            elif self.pre_item == self.apply_item and num>= bar_number:
                print("555555")
                print("\n")

                return num % self.number == 0
            elif self.pre_item != self.apply_item and buy_item == self.pre_item:
                print("88888888")
                print("\n")

                try:
                    number_apply_item = total_items[self.apply_item]
                    print("number_apply_item, bar_number")
                    print(number_apply_item, bar_number)
                    print("\n")

                    if number_apply_item >= self.number:
                        return num % self.number == 0
                    print("3333333")
                    print("\n")


                except:
                    print("444444")
                    print("\n")

            else:
                print("666666")
                print("\n")

                return False
        else:
            print("7777777777")
            print("\n")

            return False


    def discount(self, buy_item, num):
        price = GetRegularPrice(buy_item)
        discount = 0
        if (self.promoDoesApply( buy_item, num, self.bar_number)):
            # apply the promo
            print("prododoesapplysuccessful")
            if (self.save > 0):
                discount = - self.save
            if (self.func != None):
                try:
                    # all promo functions are expected to have this argument list: item, cost, nth and return the new promo cost
                    #discount = self.func(self.buy_item, price, self.number)

                    function = getattr(self, self.func, self.func)
                    function(self.apply_item, discount, num)
                except:
                    # it didn't work, leave as is
                    pass
            #update the previous discount
            if self.pre_item == buy_item and self.apply_item != self.pre_item:
                return 0
        return discount

    def UpdatePrice(self, apply_item, discount, num ):
        """
        print("IN UPDATE PRICE")

        global basket
        print ("WHY")
        print(num)
        print(self.LimitationBool(num))
        for i in basket:
            print("Limitation bool successful")

            print ("counter and self.limitation")
            print (counter, self.limitation)
            print ("\n")
            if i.item_name == apply_item :
                print(i.discount, discount)
                i.discount = min(discount,i.discount)
            counter+=1
        """
        counter = 0
        global basket
        if self.limitation == 0:
            for i in basket:
                if i.item_name == apply_item:
                    i.discount = min(discount, i.discount)
        else:
            for i in basket:
                print("HERE IS I")
                print(i)

                if i.item_name == apply_item and counter < self.limitation:
                    print(i.discount, discount)
                    i.discount = min(discount, i.discount)
                    counter+=1
                else:
                    break


#inv.insert(inventory_list)
#db.inventory.remove({})
#doc_id = inventory.insert(inventory_list)

"""
for i in k:
    print (i)
    print ("\n\n\n")
for post in inv.find({"Name": "Apples"}):
    print(post["Name"])
"""
#print (my_doc["Price"])

def GetRegularPrice(item):
    for i in inv.find({"Product Code": item}):
        return (i["Price"])


def getPriceAndPromoTuple(item, nth):
    cost = GetRegularPrice(item)
    deal = ""
    global basket
    # check for promo
    if (item in promo_dict):
        for promo in promo_dict[item]:
          #if (promo.promoDoesApply(item, nth)):
            cost += promo.discount(item, nth)
            deal = promo.name

    return cost

class Product:
    def __init__(self, item_name, the_number, promotion_name, regular_price, discount):
        self.item_name = item_name
        self.the_number = the_number
        self.promotion_name = promotion_name
        self.regular_price = regular_price
        self.discount = discount

def PrintBasket():
    total = 0
    global basket
    print('Item' + ' '*16 + 'Price')
    print('-'*4 + ' '*16 + '-'*5)
    for i in basket:
        total += i.regular_price+i.discount
        print(i.item_name + ' '*17 + str(i.regular_price))
        if i.discount != 0:
            print(' '*9 + i.promotion_name + ' '*7 + str(i.discount))
    print ('-'*25)
    print (' '*20 + str(total) + '\n')

def printHelp():
    # print the inventory list and current promotion
    print ("Here is the inventory and the regular price!")
    for i in item_list:
        print(i)

if __name__== "__main__":
    # number of items purchased indexed by item
    total_items = {}
    get_inv = inv.find()
    item_list = []
    for i in get_inv:
        item_list.append(i["Product Code"])
    for i in item_list:
        print(i)

    basket = []

    # simulate the promotion classs
    promo_dict = {}
    #{ "Pre Item": ,"Apply Item":
    # "number", "bar_number":  "Promo Code"
    #  "func": , limitation
    #  "regular price", "Price drop": 0:},

    a = "CH1"
    promo_dict[a] = []
    promo = Promotion(a, "MK1", 1, 1, "CHMK", "UpdatePrice", 1, 4.75, 4.75 )
    promo_dict[a].append(promo)

    a = "AP1"
    promo_dict[a] = []
    promo = Promotion(a, "AP1", 1, 3, "APPL", "UpdatePrice", 0, 6.00, 1.5)
    promo_dict[a].append(promo)

    a = "CF1"
    promo_dict[a] = []
    promo = Promotion(a, "CF1", 2, 0, "BOGO", None, 0, 11.23, 11.23)
    promo_dict[a].append(promo)

    a = "MK1"
    print (a)
    promo_dict[a] = []
    promo = Promotion("CH1", a, 1, 1, "CHMK", "UpdatePrice", 1, 4.75, 4.75 )
    promo_dict[a].append(promo)

    a = "OM1"
    promo_dict[a] = []
    promo = Promotion(a, "AP1", 1, 1, "APOM", "UpdatePrice", 1, 6.00, "50%" )
    promo_dict[a].append(promo)
    promo_dict["AP1"].append(promo)


    while True:
        try:
            fruit = raw_input()
        except:
            break

        if (fruit in item_list):
            # keep track of the number of each item bought
            total_items[fruit] = total_items.get(fruit, 0) +1
            print ("fruit " + fruit + "total_items[fruit]" + str(total_items[fruit]))
            reg_price = GetRegularPrice(fruit)
            # expecting (price, promo text)
            tuple = getPriceAndPromoTuple(fruit, total_items[fruit] )

            print ("tuple " + str(tuple))
            theitem = Product(fruit, total_items[fruit], 'BOGO', reg_price, tuple-reg_price)
            basket.append(theitem)
            for i in basket:
                print("HERE IS I")
                print(i)

            PrintBasket()
        elif (fruit == ""):
            break
        elif (fruit == "help"):
            printHelp()
        elif (fruit not in item_list):
            print("Wrong item, Scan again")

        else:
            pass



