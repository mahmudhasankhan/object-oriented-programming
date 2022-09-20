import csv


class Item:
    # class level attributes
    discount_rate = 0.2
    item_list = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validations
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self objects
        self.__name = name  # instance level attributes
        self.quantity = quantity
        self.__price = price

        # Actions that follows after execution
        Item.item_list.append(self)

    @property
    # getters - encapsulation
    def get_price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price - (self.__price * self.discount_rate)
        return self.__price

    def apply_increment(self, percentage):
        self.__price += self.__price * percentage

    @property
    # getters (encapsulation)
    def get_name(self):
        return self.__name

    @get_name.setter
    # setters (encapsulation)
    def get_name(self, value):
        if len(value) > 10:
            raise Exception('The length of name is too long')
        else:
            self.__name = value

    def __repr__(self):
        return f'{self.__class__.__name__}(Name:{self.name}, Price:{self.__price}, Quantity:{self.quantity})'

    def calculate_total_price(self):
        return self.__price * self.quantity

    def is_not_used(self):
        pass


    @classmethod  # -> this is a decorator which is used to quickly change the behaviour of a function.
    def instantiate_from_csv(cls):
        with open('../methods/data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def check_integer(number):
        # we will count out the floats that are point zero
        # for i.e 5.0, 10.0
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
