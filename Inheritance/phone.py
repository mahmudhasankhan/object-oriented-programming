from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)
        # Run validations
        assert broken_phones >= 0, f'Broken Phones {broken_phones} cannot be less than zero'
        # Assign to self objects
        self.broken_phones = broken_phones