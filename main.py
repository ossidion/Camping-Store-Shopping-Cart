from classes import *


msr_tent = Item("MSR Tent", 450, 10)
thermarest_quilt = Item("Thermarest Quilt", 390, 7)
nemo_fillo_pillow = Item("Nemo Fillow Pillow", 45, 22)
deuter_backpack = Item("Deuter Backpack", 110, 14)
msr_pocket_rocket = Item("MSR Pocket Rocket", 55, 19)
thermarest_sleeping_pad = Item("Thermarest Sleeping Pad", 240, 11)

stock_list = StockList()

stock_list.add_item(msr_tent)
stock_list.add_item(thermarest_quilt)
stock_list.add_item(nemo_fillo_pillow)
stock_list.add_item(deuter_backpack)
stock_list.add_item(msr_pocket_rocket)
stock_list.add_item(thermarest_sleeping_pad)



shopping_cart = ShoppingCart()


def get_num_input(prompt):
    user_input = input(prompt)
    if user_input.isdigit():
        return int(user_input)
    else:
        return None


def main():

    print("\n")
    print("Welcome to Incline!\n")
    
    MENU = "\n""""Options
    
1. Display Products
2. Add Item to Cart
3. Remove Item from Cart
4. Continue to Checkout

0. Quit
"""

    while True:
        print("\nYour shopping cart: \n")
        shopping_cart.display_shopping_cart()
        user_option = input(MENU)
        
        if user_option == "1":
            stock_list.display_items()
            
        elif user_option == "2":
            
            stock_list.display_items()
            while True:
                user_index = get_num_input(": ")
                if isinstance(user_index, int):
                    break
                print("Invalid input.")
            item_to_add = stock_list.get_item(user_index-1)
            shopping_cart.add_item_by_index(item_to_add)
            item_to_add.add_to_cart()
            print("\nItem has been added")
                
        elif user_option == "3":
            
            shopping_cart.display_shopping_cart()
            while True:
                user_index = get_num_input(": ")
                if isinstance(user_index, int):
                    break
                print("Invalid input.")
            item_to_remove = shopping_cart.get_item(user_index-1)
            shopping_cart.remove_item_by_index(item_to_remove)
            item_to_remove.remove_from_cart()
            print("\nItem has been removed")


if __name__ == "__main__":
    main()
