
input = input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u']
print("Output: ", end='')
for char in input:
    if char.lower() not in vowels:
        print(char, end='')
print()