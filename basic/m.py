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

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # To print all the values in the instance
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


item1 = Item("Phone", 1000, 1)
item2 = Item("Laptop", 50000, 3)

print(item1.calculate_total_price())
item1.apply_discount()
print(item1.price)

# Class variable can be overridden, when it is used in instance level.
# Don't forget to declare this class variable as an instance variable.
item2.calculate_total_price()
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

# Listing all the attributes for Class level
print(Item.__dict__)
# Listing all the attributes for instance level
print(item1.__dict__)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

for instance in Item.all:
    print(instance.name)

print(Item.all)
