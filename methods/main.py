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
    
    @classmethod  # -> this is a decorator which is used to quickly change the behaviour of a function.
    def instantiate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )


Item.instantiate_from_csv()
print(Item.item_list)