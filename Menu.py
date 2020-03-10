from Stacks import SinglyLinkedList as linkedlist
instance = linkedlist()
prices = []
bank = 0
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
        price = int(input("Please specify hom much it cost:\n>>>"))
        instance.add_head(int(amount))
        prices.append(price)
    if select == 2:
        print("First item in a list will be deleted")
        selling_item = instance.del_head()
        sum_of_prices = sum(prices)
        average = (sum_of_prices / int(len(prices)))
        plus_profit = average + (average * 0.1)
        amount_of_total = plus_profit * selling_item
        bank += amount_of_total
        print("Was added to bank account:")
        print(amount_of_total)
    if select == 3:
        print("So far you have made:")
        print(bank)
    if select == 0:
        break

