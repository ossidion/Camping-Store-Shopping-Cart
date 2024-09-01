"""Tabulate is imorted to display the shopping cart in a clean manner.
"""
from tabulate import tabulate



class Item:

    """The Item class accounts for each item that the customer
    chooses to put into their shopping cart. Each instance
    is an item which can be added to the shopping cart. This
    item clsss includes the following methods:
    """

    # __init__(): which initialises the instance item with a name,
    # price, stock count and quantity, which can be used as a
    # counter for the number of this item type the user has within
    # their shopping cart.
    def __init__(self, name, price, stock, quantity=0):
        self.name = name
        self.price = price
        self.stock = stock
        self.quantity = quantity
        # self.available_products = []

    # __str__(): returns a string representation of an Item object.
    def __str__(self):
        return (f"Item: {self.name}\n"
                +f"Price: {self.price}\n"
                +f"Stock Count: {self.stock}\n"
                +f"Quantity in Shopping Carts: {self.quantity}")
    
    def __repr__(self):
        return print(f"Item: {self.name}\t"
              +f"${self.price}\t"
              +f"Stock: {self.stock}\n")

    def add_to_cart(self):
        if self.stock > 0:
            self.stock -= 1
            self.quantity += 1
        else: 
            print("This item is currently not in stock.")

    def remove_from_cart(self):
        if self.quantity > 0:
            self.quantity -= 1
            self.stock += 1
        else: 
            print("This item is currently not in your cart.")
        
    

class StockList(Item):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        headers = ["", "Item", "Price", "Stock"]
        data = []

        for i, item in enumerate(self.items, 1):
            data.append([i, item.name, item.price, item.stock])
        print(tabulate(data, headers=headers))

    def get_item(self, user_index):
        return self.items[user_index]


    
class ShoppingCart(Item):
    def __init__(self):
        self.shopping_cart = []
        self.total = []

    def display_shopping_cart(self):
        self.shopping_cart = list(dict.fromkeys(self.shopping_cart))

        headers = ["", "Item", "Price", "Quantity"]
        data = []


        for i, item in enumerate(self.shopping_cart, 1):
            data.append([i, item.name, item.price, item.quantity])
        print(tabulate(data, headers=headers))

    # Function to look through the object instances which have been added to the shopping cart and
    # provide a sum total. 
    def shopping_cart_total(self):
        total = []
        for i in self.shopping_cart:
            total.append(i.price * i.quantity)  # The object instance's prices are stored in a list and multiplied 
                                                # by each object instance quantity.

        sum_total = 0
        for i in total:
            sum_total += i         # The prices are taken from the list and storred as a total integer variable. 
        return print(f"\nTotal: {sum_total}")

        
    def get_item(self, user_index):
        return self.shopping_cart[user_index]

        
    def remove_item_by_index(self, index):
        if index.quantity == 1:
            self.shopping_cart.remove(index)
        elif index.quantity > 1:
            index.quantity -1

        
    def add_item_by_index(self, user_index):
        self.shopping_cart.append(user_index)