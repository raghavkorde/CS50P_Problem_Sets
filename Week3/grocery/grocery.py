
items = {}
while True:
    try:
        item = input().strip().upper()
        if item not in items: 
            items.update({item: 1})
        else:
            items[item] += 1
    except EOFError:
        break
items = dict(sorted(items.items()))
for item in items:
    print(f"{items[item]} {item}")
