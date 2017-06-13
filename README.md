# Checkout System for Farmers' Market
The whole program is written Python, also use PyMongo in order to workwith MongoDB, the test is unit testing

## usage:

'''
python3 checkout.py
'''
Simple enter product code, most recent basket information will come up.
Enter "help" to check item list
Promotions will be applied automatically to the basket
Basket will be updated and printed out every time new item is added

There are 4 different promotions:
1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
4. APOM -- Buy 1 bag Oatmeal and 50% off of one bag of apple

Sometimes, there are multiple promotions on one item, and in this case, we choose the promotion with the most discount
For example, the item bought is MK1, AP1, AP1, AP1, OM1, and the basket will be like this :

| MK1 | | 4.75 | 
| --- | --- | --- |
| AP1 | | 6.0 | 
| | APOM | -3.0 |
| AP1 | | 6.0 |
| | APPL | -1.5 |
| AP1 | | 6.0 |
| | APPL| -1.5 |
| OM1 | | 3.69 |

