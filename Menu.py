from Stacks import Stacks as S
instance_amount = S()
profit = 0

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
        print(instance_amount.display())
        price = int(input("Please specify hom much it cost:\n>>>"))
        instance_price.push(int(price))
        print(instance_price.display())
    if select == 2:
        amount_to_sell = int(input("Specify how many will be deleted:\n>>>"))
        selling_item = instance_amount.pop()
        print("Was added to bank account:")
    if select == 3:
        print("So far you have made:")
    if select == 0:
        break

