""" Building E-commerce website from scratch"""

""" Super Class """


class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("Ratings: {}".format(self.ratings))
        print("You Save: {}".format(self.you_save))

    def get_deal_price(self):
        return self.deal_price


"""Sub Class"""

class ElectronicItems(Product):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)  # Method Overriding
        self.warranty_in_months = warranty_in_months

    def display_product_details(self):
        super().display_product_details()  # Method Overriding
        print("Warranty {} Months".format(self.warranty_in_months))


"""Sub Class"""

class GroceryItems(Product):
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)  # Method Overriding
        self.expiry_date = expiry_date

    def display_product_details(self):
        super().display_product_details()  # Method Overriding
        print("Expiry Date: {}".format(self.expiry_date))

"""Sub Class"""

class Laptop(ElectronicItems):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months, processor, ram, storage):
        super().__init__(name, price, deal_price, ratings, warranty_in_months)
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def display_product_details(self):
        super().display_product_details()  # Method Overriding
        print("Processor: {}".format(self.processor))
        print("RAM: {}".format(self.ram))
        print("Storage: {}".format(self.storage))


"""Order Class"""


class Order:
    delivery_charges = {"Normal": 15, "Prime": 30, "Express": 50}

    def __init__(self, delivery_method, address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.address = address

    def add_items_to_cart(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)

    def display_order_details(self):
        print("Delivery Method: {}".format(self.delivery_method))
        print("Delivery Charge: {}".format(self.delivery_charges[self.delivery_method]))
        print("Address: {}".format(self.address))
        print("--------------------------------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print("")
        total_bill = self.get_total_bill()
        print("--------------------------------")
        print("Total Bill: {}".format(total_bill))

    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            total_bill += product.get_deal_price() * quantity

        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        total_bill += order_delivery_charges
        return total_bill

    @classmethod
    def update_delivery_charges(cls, delivery_method, charges):
        cls.delivery_charges[delivery_method] = charges


# '''Creating instances of Product'''
# my_product = Product("Monitor", 11500, 9999, 4.9)
# my_product.display_product_details()

"""Creating instances of ElectronicItems"""
my_electronic_items = ElectronicItems("Television", 35000, 31000, 4.5, 10)
# my_electronic_items.display_product_details()

"""Creating instances of GroceryItems"""
my_grocery_items = GroceryItems("Sona Mysore Rice", 1120, 1050, 5.0, "20-12-2023")
# my_grocery_items.display_product_details()

"""Creating instances of Laptop"""
my_laptop = Laptop("Asus vivo book", 59000, 53000, 4.8, 12, "i7 6th Gen", "16GB DDR 5", "2TB Nvme")


"""Creating instances of Order"""
my_order = Order("Normal", "Vijayawada")
my_order.add_items_to_cart(my_electronic_items, 1)
my_order.add_items_to_cart(my_grocery_items, 3)
my_order.add_items_to_cart(my_laptop, 1)
Order.update_delivery_charges("Normal", 50)

my_order.display_order_details()
