import csv


class Item:
    # Class variable
    pay_rate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # If the price should not be negative, we can run validations using assert
        assert price >= 0, f"Price {price} should not be greater than zero!!!"
        assert quantity > 0, f"Quantity {quantity} should not be greater than Zero!!!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Adding all objects into a list
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            things = list(reader)

        for item in things:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # To print all the values in the instance
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # If the price should not be negative, we can run validations using assert
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken phones {broken_phones} should not be greater than Zero!!!"

        # Assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)
item = Item("Samsung", 500, 4)
print(Item.all)
print(Phone.all)
