input = input('camelCase: ')

for char in input:
    if char.isupper():
        print('_'+ char.lower(), end='')
    else:
        print(char, end='')
print()