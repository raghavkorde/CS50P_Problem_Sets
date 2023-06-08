
greeting = input("Greeting: ").lower().strip()

letter = greeting[0]

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")