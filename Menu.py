# Temur Khabibullaev 3/11/2020
from Stacks import Stacks as S
# Creating two instances for amount and price
instance_amount = S()
instance_price = S()
# These are temporary variables
profit = 0
inventory = 0
while True:
    print("""Welcome! Choose below to proceed!
    MENU:
    1. Add to the inventory.
    2. Sell items in inventory.
    3. Check profit to date.
    4. Display inventory.
    5. Enter 5 to exit.""")
    select = int(input("\n>>>"))
    # Process of storing in inventory
    if select == 1:
        amount = int(input("Please specify how many:\n>>>"))
        instance_amount.push(int(amount))
        inventory += amount
        price = int(input("Please specify hom much it cost:\n>>>"))
        instance_price.push(int(price))
    # Process to sell items from the inventory
    if select == 2:
        amount_to_sell = int(input("Specify how many will be deleted:\n>>>"))
        # If specified amount is too much
        if amount_to_sell > inventory:
            print("You specified too large amount.")
            break
        # Actual process of selling
        else:
            # Subtracting selling amount from inventory
            inventory -= amount_to_sell
            # Having always changing variable for price
            last_price = None
            # X is the first number in the Stack
            x = instance_amount.display()[0]
            # If first number is less than intended amount for sell
            if x < amount_to_sell:
                # Temporary variable to control popping method
                storage = 0
                while storage != amount_to_sell and storage < amount_to_sell:
                    selling_item = instance_amount.pop()
                    storage += selling_item
                    last_price = instance_price.pop()
                # When storage is surpassed do this
                if storage > amount_to_sell:
                    difference = storage - amount_to_sell
                    instance_amount.push(difference)
                    instance_price.push(last_price)
                    profit += (last_price * 0.1) * amount_to_sell
            # When amount for sell is less than first number in Stack
            if amount_to_sell < x and amount_to_sell > 0:
                # Process is easy
                selling_item = instance_amount.pop()
                last_price = instance_price.pop()
                difference = selling_item - amount_to_sell
                instance_amount.push(difference)
                instance_price.push(last_price)
                profit += (last_price * 0.1) * amount_to_sell
            # When it happens that first number equals to selling amount
            if x == amount_to_sell:
                selling_item = instance_amount.pop()
                last_price = instance_price.pop()
                profit += (last_price * 0.1) * selling_item
    # Display so far made profit
    if select == 3:
        print("So far you have made:")
        print(profit)
    # Display leftover items
    if select == 4:
        print(instance_amount.display())
    # Quit
    if select == 5:
        break

