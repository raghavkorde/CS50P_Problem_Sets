
def main():
    answer = input("What time is it? ").strip()
    time = convert(answer) 
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print ("dinner time")


def convert(time):
    time = time.split(":")
    hours = time[0]
    minutes = time[1]

    convert = float(hours) + float(minutes)/60
    return convert

if __name__ == "__main__":
    main()