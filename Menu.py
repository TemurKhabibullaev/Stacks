from Stacks import Stacks as S
instance_amount = S()
instance_price = S()
profit = 0
inventory = 0
while True:
    print("""Welcome! Choose below to proceed!
    MENU:
    1. Add to the inventory.
    2. Sell items in inventory.
    3. Check profit to date.
    4. Enter 0 to exit.""")
    select = int(input("\n>>>"))
    if select == 1:
        amount = int(input("Please specify how many:\n>>>"))
        instance_amount.push(int(amount))
        inventory += amount
        price = int(input("Please specify hom much it cost:\n>>>"))
        instance_price.push(int(price))
    if select == 2:
        amount_to_sell = int(input("Specify how many will be deleted:\n>>>"))
        if amount_to_sell > inventory:
            print("You specified too large amount.")
            break
        else:
            inventory -= amount_to_sell
            temporary = 0
            last_price = None
            x = instance_amount.display()[0]

            if x < amount_to_sell:
                selling_item = instance_amount.pop()
                last_price = instance_price.pop()
                temporary += selling_item
                current_profit = (0.1 * int(last_price)) * int(selling_item)
                profit += current_profit
                print(profit)
            if amount_to_sell < x:
                selling_item = instance_amount.pop()
                last_price = instance_price.pop()
                difference = selling_item - amount_to_sell
                instance_amount.push(difference)
                instance_price.push(last_price)
                break
            if x == amount_to_sell:
                selling_item = instance_amount.pop()
                last_price = instance_price.pop()
                profit += (last_price * 0.1) * selling_item
                break
    if select == 3:
        print("So far you have made:")
    if select == 0:
        break

