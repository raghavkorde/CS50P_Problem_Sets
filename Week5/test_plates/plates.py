import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    for char in s:
        if char.isalnum() == False:
            return False
    if s[0].isalpha() == False and s[1].isalpha() == False: 
        return False
    for i in range(0, len(s)):
        for k in range(i, len(s)):
            if s[i].isdigit() and s[k].isalpha():
                return False
    digits = []
    for char in s:
        if char.isdigit():
            digits.append(int(char))
    if digits != [] and digits[0] == 0:
        return False
    return True 

if __name__ == "__main__":
    main()