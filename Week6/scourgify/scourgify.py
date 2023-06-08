import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False and sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a Python File")
    else:
        scourgify(sys.argv[1], sys.argv[2])

def scourgify(file_before, file_after):
    try:
        with open(file_before, "r") as input:
            reader = csv.DictReader(input)
            with open(file_after, "w") as output:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output, fieldnames = header)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == '__main__':
    main()

    