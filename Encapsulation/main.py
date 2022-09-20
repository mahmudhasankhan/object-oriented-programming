"""
Examples of encapsulation where you get to manipulate class property
attributes by not accessing them directly but with the use of different
functions. You can control the access of your class attributes by getters
and setters and also by making your class attributes private.
"""

from item import Item

item1 = Item('Item', 750)
print(item1.get_name)  # getters
item1.get_name = 'NewItem'  # setters
print(item1.get_name)
print(f'before increment = {item1.get_price}')
item1.apply_increment(0.2)
print(f'after increment = {item1.get_price}')
item1.apply_discount()
print(f'after discount = {item1.get_price}')









