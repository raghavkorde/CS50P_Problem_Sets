
def main():
    word = input("Input: ")
    output = shorten(word)
    print(f"Output: {output}")

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = ''
    for char in word:
        if char.lower() not in vowels:
            output += char
    return output


if __name__ == "__main__":
    main()

