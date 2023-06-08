import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV File")
    else:
        format(sys.argv[1])

def format(file_name):
    table = []
    index = 0
    with open(file_name, 'r') as file:
        for row in file:
            col1, col2, col3 = row.rstrip().split(",")
            table.append([col1, col2, col3])
    print(tabulate(table[1:], table[0], tablefmt="grid"))


if __name__ == "__main__":
    main()
