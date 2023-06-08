import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression pattern to match an IPv4 address
    pattern = r'^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$'
    return bool(re.match(pattern, ip))



if __name__ == "__main__":
    main()