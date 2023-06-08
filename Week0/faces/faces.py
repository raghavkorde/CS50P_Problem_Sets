
# Convert function implementation
# Use .replace() method to replace text in input
def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str


def main():
    text = input("Enter text: ")
    text = convert(text)
    print(text)

main()