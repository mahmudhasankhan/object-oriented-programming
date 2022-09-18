"""
some tips
there are two types of attributes inside a class
 1. class level
 2. instance level
you can access a class attribute by writing CLASS.attribute_name
you can access a instance attribute by writing OBJECT.attribute_name

** assert keyword is used when you want to achieve some sort of validation
for class or instance level attributes
** non-default argument should not follow the default argument, meaning
writing this (a='b', c) is wrong, instead it should be (c, a='b')

** while creating functions, self parameter is always passed as default.

** name of a method that start with __ and end with __ is called a
magic method

"""


class Item:
    # class level attributes
    discount_rate = 0.2
    item_list = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validations
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self objects
        self.name = name  # instance level attributes
        self.quantity = quantity
        self.price = price

        # Actions that follows after execution
        Item.item_list.append(self)

    def __repr__(self):
        return f'Item(Name:{self.name}, Price:{self.price}, Quantity:{self.quantity})'

    def calculate_total_price(self):
        return self.price * self.quantity

    def is_not_used(self):
        pass

    def apply_discount(self):
        self.price = self.price - (self.price * self.discount_rate)
        return self.price


# Instantiating instances of class Item
item1 = Item('phone', 25_000, 4)
item2 = Item('laptop', 100_000, 2)

# print(Item.__dict__)  # used to get all the attributes of an instance,
# print(item1.__dict__)  # can be used for debugging reasons
print(f'Without discount price = {item1.price}')
print(f'discounted price = {item1.apply_discount()}')

# changing a class attribute for a specific instance
item2.discount_rate = 0.3
print(f'without discount price of {item2.name} = {item2.price}')
print(f'with discount price of {item2.name}= {item2.apply_discount()}')

for item in Item.item_list:
    print(f' #{Item.item_list.index(item)} Object name = {item.name}')

print(Item.item_list)

