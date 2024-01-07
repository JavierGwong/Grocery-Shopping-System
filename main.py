def menu():
    print('''
1. Display category
2. Display items in alphabetical order
3. Display items in ascending price
4. View the shopping cart
5. Check-out
6. Edit items in cart
7. Clear cart
8. Payment
9. Exit''')


# Extra function def pay and exit

def ShowCategories(items):
    Counter = 1
    for i in items:
        print(str(Counter) + ". " + str(i))
        Counter += 1
    while 1:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3, 4, 5]:
                # Only displayCategories() will come here.
                inputChoice = 1
                for i in items:
                    if inputChoice == choice:
                        return i
                    inputChoice += 1
                return
        except:
            continue


def displayItems(items):
    Counter = 1
    for i in items:
        print(str(Counter) + ". " + str(i[0]).ljust(30) + '$' + str(i[1]))
        Counter += 1
    while 1:
        try:
            count = []
            j = 1
            for i in items:
                count.append(j)
                j += 1
            choice = int(input("Enter your choice: "))
            if choice in count:
                # displayCategories(items, cart) , displayAlphabetical(items, cart) , displayAscendingPrice(items, cart) will use this
                inputchoice = 1
                for i in items:
                    if inputchoice == choice:
                        return i[0]
                    inputchoice += 1
                return
        except:
            continue


# Return to the 3 functions, whichever that was used

def displayCategories(items, cart):
    cat = ShowCategories(items)

    ilist = []
    for i in items[cat]:
        ilist.append([i, items[cat][i]])

    key = displayItems(ilist)
    val = 0
    for i in ilist:
        if i[0] == key:
            val = i[1]
            break
    # Break to exit the (For) and (If) to ask for quantity.
    while 1:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                # set the i[0] = name of item, i[1] = price of item, i[2] = is the quantity from user input().
                cart.append([key, val, quantity])
                return
            else:
                print('Please enter a number greater than 0')
                continue
        except:
            print('Please enter a number greater than 0')
            continue


def displayAlphabetical(items, cart):
    ilist = []
    for i in items:
        for j in items[i]:
            ilist.append([j, items[i][j]])
    # j is the name of item first, so it will be sorted by name below.
    ilist.sort()
    key = displayItems(ilist)

    val = 0
    for i in items:
        for j in items[i]:
            if j == key:
                val = items[i][key]

    while 1:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                # set the i[0] = name of item, i[1] = price of item, i[2] = is the quantity from user input().
                cart.append([key, val, quantity])
                return
            else:
                print('Please enter a number greater than 0')
                continue
        except:
            print('Please enter a number greater than 0')
            continue


def displayAscendingPrice(items, cart):
    ilist = []
    for i in items:
        for j in items[i]:
            ilist.append([items[i][j], j])
    # The j here is the name, but they want to sort in price, so we place it behind the price
    ilist.sort()
    sortedlist = []
    for i in ilist:
        sortedlist.append([i[1], i[0]])
    # Since the name is i[1] behind the price = i[0]. ^^^
    key = displayItems(sortedlist)
    val = 0
    for i in sortedlist:
        if i[0] == key:
            val = i[1]
            break

    while 1:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                # set the i[0] = name of item, i[1] = price of item, i[2] = is the quantity from user input().
                cart.append([key, val, quantity])
                return
            else:
                print('Please enter a number greater than 0')
                continue
        except:
            print('Please enter a number greater than 0')
            continue


def displayCart(cart):
    finalList = []
    for i in cart:
        total = i[1] * i[2]
        finalList.append(total)
    total_price = sum(finalList)
    if total_price > 0:
        print('Great choice!!!\U0001f44d\U0001f44d\U0001F92A')
        print("------------------------------------------------------------------------")
        print("|Item|                    |Quantity|     |Unit Price|      |Total|")
        print("------------------------------------------------------------------------")
        total = 0
        for i in cart:
            print(i[0].ljust(29), str(i[2]).ljust(14), ('$' + str(i[1])).ljust(14), '$' + str(round(i[1] * i[2], 2)))
            total += i[1] * i[2]
        print("------------------------------------------------------------------------")
        print("TOTAL:                                                      " + '$' + str(round(total, 2)))
        print("------------------------------------------------------------------------")
        return total
    else:
        print('You have nothing in your cart')
        return


# Return total for checkOut(cart), so we don't need to do (total += i[1] * i[2]) again.

def checkOut(cart):
    finalList = []
    for i in cart:
        total1 = i[1] * i[2]
        finalList.append(total1)
    total_price = sum(finalList)
    if total_price > 0:
        total = displayCart(cart)
        discount = 0
        voucher = input("Do you have a discount voucher(y/n): ").lower()
        if voucher[0] == 'y':
            discount = total * 0.1
        total -= discount
        print("------------------------------------------------------------------------")
        print("GST:                                                        " + '$' + str(
            round(total_price / 1.07 * 0.07, 2)))
        print("Discount:                                                   " + '$' + str(round(discount, 2)))
        print("GRAND TOTAL:                                                " + '$' + str(round(total, 2)))
        print("------------------------------------------------------------------------")
        return
    else:
        print('You have nothing in your cart')
        return


def clearcart(cart):
    cart.clear()
    print('Your cart has been cleared')
    return


def editItem(cart):
    displayCart(cart)
    finalList = []
    for i in cart:
        total = i[1] * i[2]
        finalList.append(total)
    total_price = sum(finalList)
    if total_price > 0:
        while 1:
            try:
                count = []
                j = 1
                for i in cart:
                    count.append(j)
                    j += 1
                # x = len(cart)
                # print(x) instead of doing this, did cart.__len__ below then string it
                item = int(input("Which item do you want to edit (1 - " + str(cart.__len__()) + " ): "))
                if item in count:
                    temp = cart[item - 1]
                    x = int(input('Enter amount to change to:'))
                    if x <= 0:
                        cart.remove(temp)
                        print('Item has been removed')
                        return
                    else:
                        temp[2] = x
                        print('Cart updated')
                    return
            except:
                continue
    else:
        return


def payment(cart):
    finalList = []
    for i in cart:
        total1 = i[1] * i[2]
        finalList.append(total1)
    total_price = sum(finalList)
    if total_price > 0:
        total = displayCart(cart)
        discount = 0
        voucher = input("Do you have a discount voucher(y/n): ").lower()
        if voucher[0] == 'y':
            discount = total * 0.1
        total -= discount
        print("------------------------------------------------------------------------")
        print("GST:                                                        " + '$' + str(
            round(total_price / 1.07 * 0.07, 2)))
        print("Discount:                                                   " + '$' + str(round(discount, 2)))
        print("GRAND TOTAL:                                                " + '$' + str(round(total, 2)))
        print("------------------------------------------------------------------------")
        while 1:
            # Did not add try and except for this, it is an extra function.
            # It should simulate cash transaction,impossible to enter 'string'
            print('Type any letter to return to main menu')
            amount_payed = float(input('Payment amount: $'))
            if amount_payed >= total:
                change = amount_payed - total
                print('Your change : $%.2f' % change)
                print('Thank you for shopping at JSC mart\U0001f44d')
                print('Your cart has been cleared, you may buy more items or press 8 to exit')
                cart.clear()
                break
            elif amount_payed < total:
                print('Not enough, enter again')
                continue
    else:
        print('You have nothing in your cart')
        return


items = {"Dairy": {"Milk": 2.3, "Butter": 4.5, "Eggs": 3.4, "Cheese slices": 3.15,
                   "Evaporated milk creamer": 1.4, "Milo": 12.5, "Biscuits": 5.30,
                   "Yogurt": 0.95},

         "Packaged Goods": {"Bread": 2.7, "Cereal": 7.0, "Crackers": 3.1, "Chips": 2.6,
                            "Raisin": 2.1, "Nuts": 2.0, "Green Bean": 1.05, "Barley": 1.05},

         "Canned Goods": {"Tomato": 1.45, "Button Mushroom": 1.15, "Baking Bean": 1.35, "Tuna Fish": 1.45,
                          "Kernel Corn": 1.25, "Sardine Fish": 1.1, "Chicken Luncheon Meat": 1.95,
                          "Pickled Lettuce": 0.95},

         "Condiments/Sauces": {"Fine Salt": 0.8, "Sea Salt Flakes": 1.3, "Chicken Stock": 3.15, "Chilli Sauce": 2.65,
                               "Oyster Sauce": 4.5, "Sweet Soy Sauce": 3.75, "Tomato Ketchup": 3.2,
                               "Sesame Oil": 4.95},

         "Beverages": {"Green Tea Canned 330 ML": 15.0, "Blackcurrant Ribena 330 ML": 31.0, "100 Plus 24 Cans": 15.0,
                       "Orange Cordial 2 Litre": 3.9, "Mineral Water 24 x 600 ML": 7.0, "Pineapple Juice": 0.8,
                       "Nescafe Coffee": 9.9, "Coke 24 Cans": 12.4}}

for i in items:
    for j in items[i]:
        items[i][j] = round(items[i][j] + (items[i][j] * 0.07), 2)
# Added items with GST first, so we don't have to add again
# If needed, possible to (total + (items[i][j] * 0.07), 2)) instead. Gst = round(total / 1.07 * 0.07, 2)
cart = []

print('Hello!\U0001F44B,Welcome to JSC mart!!')
while 1:
    menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            displayCategories(items, cart)
        elif choice == 2:
            displayAlphabetical(items, cart)
        elif choice == 3:
            displayAscendingPrice(items, cart)
        elif choice == 4:
            displayCart(cart)
        elif choice == 5:
            checkOut(cart)
        elif choice == 6:
            editItem(cart)
        elif choice == 7:
            clearcart(cart)
        elif choice == 8:
            payment(cart)
        elif choice == 9:
            print('\U0001F44BThank you, we hope to see you again\U0001F44B')
            break
        else:
            print("invalid option")
    except:
        print('Invalid input')
        continue
