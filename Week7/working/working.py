import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Define regular expressions for each format
    regex1 = r"(\d{1,2}):(\d{2})\s(AM|PM)\s{0,}to\s{0,}(\d{1,2}):(\d{2})\s(AM|PM)"
    regex2 = r"(\d{1,2})\s(AM|PM)\s{0,}to\s{0,}(\d{1,2})\s(AM|PM)"
    
    # Check if the input string matches either of the formats
    match1 = re.match(regex1, s)
    match2 = re.match(regex2, s)
    if not match1 and not match2:
        raise ValueError("Invalid format")
    
    # Extract hours, minutes and meridian from the matched groups
    if match1:
        h1, m1, mer1, h2, m2, mer2 = match1.groups()
        h1, h2 = int(h1), int(h2)
        m1, m2 = int(m1), int(m2)
    else:
        h1, mer1, h2, mer2 = match2.groups()
        h1, h2 = int(h1), int(h2)
        m1, m2 = 0, 0
    
    # Convert to 24-hour format
    if mer1 == "PM" and h1 != 12:
        h1 += 12
    if mer2 == "PM" and h2 != 12:
        h2 += 12
    if mer1 == "AM" and h1 == 12:
        h1 = 0
    if mer2 == "AM" and h2 == 12:
        h2 = 0
    
    # Check for invalid times
    if h1 > 23 or h2 > 23 or m1 > 59 or m2 > 59:
        raise ValueError("Invalid time")
    
    # Return the 24-hour formatted string
    return f"{h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}"


if __name__ == "__main__":
    main()