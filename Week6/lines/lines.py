import sys
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python File")
    else:
        print(count_lines(sys.argv[1]))

def count_lines(file_name):
    count = 0
    try:
        with open(file_name, "r") as code:
            for line in code:
                if len(line.strip()) != 0 and line.strip().startswith("#") == False:
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()