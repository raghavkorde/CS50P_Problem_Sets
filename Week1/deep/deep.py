
# Getting user input
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.lower().strip()

# Checking condition
if answer == "forty two" or answer == "forty-two" or answer == "42":
    print("Yes")
else:
    print("No")