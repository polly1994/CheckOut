import checkout
import setup

class Promotion:

    #pre_item is the item you have to have before another item can apply the promotion
    #apply_item is the item gonna have the discount
    #number means the nth item will have the promotion, number = 1 inplies every apply_item could have promotion if they qualify
    #bar_number is the quantity that the pre_item has to reach in order to have the promotion
    #discount could be either float or string if the discount is a percentage
    def __init__(self, pre_item, apply_item, number, bar_number, promo_name, func, limitation, regular_price, discount=0):
        self.pre_item = pre_item
        self.apply_item = apply_item
        self.number = number
        self.bar_number = bar_number
        self.name = promo_name
        if type(discount) is str:
            discount = self.ConvPercentFloat(discount, regular_price)
        self.save = discount
        self.func = func
        self.limitation = limitation
        self.regular_price = regular_price

    # check if the number of the apply_item exceeds limitation

    # If the promotion is in percentage format, convert it to get the discount in decimal format
    def ConvPercentFloat(self, discount, regular_price):
        f = (float(discount[:-1]))
        discount = f / 100 * regular_price
        return discount

    # if within limitation
    def LimitationBool(self, num):
        if num > self.limitation and self.limitation!= 0 :
            return False
        else:
            return True

    def PromoApplys(self, buy_item, num):
        if self.LimitationBool(num):

            # if the item bought is the apply item instead of the pre_item
            if self.pre_item != self.apply_item and buy_item == self.apply_item :

                try:
                    # if the number of the bought item over the bar
                    number_buy_item = setup.GetNumber(self.pre_item)
                    if number_buy_item >= self.bar_number:
                        return num % self.number == 0
                except:

                    return False
            # if the pre_item is the apply_item
            elif self.pre_item == self.apply_item and num>= self.bar_number:

                return num % self.number == 0
            # if the item bought is the pre_item instead of the apply item
            elif self.pre_item != self.apply_item and buy_item == self.pre_item:

                try:

                    number_apply_item = setup.GetNumber(self.apply_item)

                    if number_apply_item >= self.number:
                        return num % self.number == 0

                except:

                    return False
            else:

                return False
        else:
            return False


    def discount(self, buy_item, num):
        #price = checkout.GetRegularPrice(buy_item)
        discount = 0.00
        deal_name = ""
        result = ()

        if (self.PromoApplys( buy_item, num)):
            deal_name = self.name
            # apply the promo
            if (self.save > 0):
                discount -=self.save
            if (self.func != None):
                try:
                    # get the function
                    function = getattr(self, self.func, self.func)
                    function(self.apply_item, discount)
                except:
                    pass
            # item bought is pre_item, promotion doesn't apply to pre_item
            if self.pre_item == buy_item and self.apply_item != self.pre_item:
                return (0, "")

        return (discount, deal_name)

    def UpdatePrice(self, apply_item, discount):
        counter = 0
        k = checkout.GetRegularPrice(apply_item)
        if self.limitation == 0:
            for i in setup.basket:
                if i.item_name == apply_item:
                    if discount < i.discount:
                        i.discount = discount
                        i.promotion_name = self.name
        else:

            for i in setup.basket:

                if i.item_name == apply_item and counter < self.limitation:
                    if discount < i.discount:
                        i.discount = discount
                        i.promotion_name = self.name
                    counter+=1
                elif i.item_name != apply_item and counter < self.limitation:
                    continue
                else:
                    break

