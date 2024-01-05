print("\n")
print("Welcome to Incline!")

cart = ""
total = 0
price = 0
item_1 = "1"
item_2 = "2"
item_3 = "3"

done = False
while (not done):
    print("\n")
    print("-"*80)
    print("This is your shopping cart: ")
    print("\n")
    print(cart + "\t" + (str(total)))
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


    if choice == "1":
        print("1. Tent ($500) \n2. Treking Poles ($50) \n3. Camping Meal ($5)")

    elif choice =="2":
        #find out item and price and it to cart
        item = input("Which item would you like to add to your cart: ")
        price = float(input("How much does the item cost: $"))

        print("{} has been added to your cart successfully.".format(item))
        cart += item
        total += price

    # elif choice == "2":
        

    elif choice == "3":
        print("The total cost of your cart is {}.".format(total))
    
    elif choice == "4":
        print("Thank you for shopping at Incline!")
        done = True
else:
    print("")