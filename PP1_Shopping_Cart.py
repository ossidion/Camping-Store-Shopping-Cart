# Print welcome message to user. 
print("\n")
print("Welcome to Incline!")

cart = ""
total = 0
price = 0
item_1 = "1"
item_2 = "2"
item_3 = "3"

# Store the current merchandise, prices and quantities in variables. 
items = ["MSR Tent", "Lanshan Tent", "Trecking Poles", "Camping Meals"]
prices = [350, 150, 100, 6]
quantities = [0, 0, 0, 0]


# item_prices = {
#                 items[0]: 350,    # This dictionary contains the price value for each item on the menu.
#                 items[1]: 150,    # The keys of the dictionary are set to the corresponding indices of
#                 items[2]: 100,    # the 'menu' list. The price values are stored next to each key within
#                 items[3]: 6       # the dictionary.
#                 }

#                                                    # each item when multiplied by the quantity 
#                                                     # of that item.

# Display menu for user and provide functionality for the user selection.
 
done = False
while (not done):
    print("\n")
    print("-"*80)
    print("This is your shopping cart: ")
    print("\n")
    # print(cart + "\t" + (str(total)))
    print("-"*80)
    print("Would you like to: ")
    print("\n")
    print("1. View range")
    print("2. Add an item to your cart")
    print("3. Remove an item from your cart")
    print("4. View the total cost of your cart")
    print("5. Checkout")
    print("\n")
    choice = input("Enter the number of the option you would like to choose: ")
    print("\n")

    # User selection 1
    item_prices = list(zip(items, prices))
    our_range = "Here is our current range:"
    
    if choice == "1":
        print(our_range, "\n")
        for i in item_prices:
            print(i)

        
        # for count, items, in enumerate(items, start = 1):
        #     print(count,"-", items)
    
    #find out item and price and it to cart
    elif choice =="2":
        item = input("Which item would you like to add to your cart: ")
        price = float(input("How much does the item cost: $"))

        print("{} has been added to your cart successfully.".format(item))
        cart += item
        total += price

    # elif choice == "2":
        
    # Display the total cost of the shopping cart. 
    elif choice == "3":
        print("The total cost of your cart is {}.".format(total))
    
    # Exit message. 
    elif choice == "4":
        print("Thank you for shopping at Incline!")
        done = True
else:
    print("")