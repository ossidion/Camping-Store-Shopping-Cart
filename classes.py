from tabulate import tabulate

class Item:
    
    def __init__(self, name, price, stock, quantity=0):
        self.name = name
        self.price = price
        self.stock = stock
        self.quantity = quantity
        # self.available_products = []

    def __str__(self, name, price, stock, quantity):
        self.name = name
        self.price = price
        self.stock = stock
        self.quantity = quantity
        return self.name, self.price, self.stock, self.quantity
    
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

    def display_shopping_cart(self):
        self.shopping_cart = list(dict.fromkeys(self.shopping_cart))

        headers = ["", "Item", "Price", "Quantity"]
        data = []


        for i, item in enumerate(self.shopping_cart, 1):
            data.append([i, item.name, item.price, item.quantity])
        print(tabulate(data, headers=headers))

        
    def get_item(self, user_index):
        return self.shopping_cart[user_index]

        
    def remove_item_by_index(self, index):
        if index.quantity == 1:
            self.shopping_cart.remove(index)
        elif index.quantity > 1:
            index.quantity -1

        
    def add_item_by_index(self, user_index):
        self.shopping_cart.append(user_index)