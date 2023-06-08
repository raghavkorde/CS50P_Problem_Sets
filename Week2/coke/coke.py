price = 50
paidAmount = 0
dueAmount = 50
coins = [25, 10, 5]

while(dueAmount > 0):
    print("Amount Due:", dueAmount)
    insert = int(input("Insert Coin: "))
    if insert in coins:
        dueAmount = dueAmount - insert
        paidAmount = paidAmount + insert
    
if(paidAmount >= price):
    print("Change Owed:", int(paidAmount - price))
