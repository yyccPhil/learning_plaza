from collections import OrderedDict

shop_dict = OrderedDict()
for i in range(int(input())):
    item_price = input().split()
    item = " ".join(item_price[:-1])
    price = int(item_price[-1])
    shop_dict[item] = shop_dict.get(item, 0) + price
    
for i in shop_dict:
    print(i, end = ' ')
    print(shop_dict[i])
    
