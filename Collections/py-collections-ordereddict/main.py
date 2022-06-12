# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from collections import OrderedDict
ordered_dictionary = OrderedDict()

n = int(input(""))
for _ in range(n):
    string = str(input(""))
    item_name = str(" ".join(re.findall('([A-Za-z]+)', string)))
    net_price = int(" ".join(re.findall('(\d+)', string)))
    if item_name in ordered_dictionary:
        net_price += int(ordered_dictionary[item_name])
    ordered_dictionary[item_name] = net_price
for item, value in ordered_dictionary.items():
    print(f"{item} {value}")
