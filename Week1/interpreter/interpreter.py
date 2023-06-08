
def text(output):
    print(f"{output:.1f}")


def main():
    exp = input("Expression: ")
    exp = exp.split(" ")
    if exp[1] == "+":
        result = float(exp[0]) + float(exp[2])
        text(result)
    elif exp[1] == "-":
        result = float(exp[0]) - float(exp[2])
        text(result)
    elif exp[1] == "*":
        result = float(exp[0]) * float(exp[2])
        text(result)
    elif exp[1] == "/" and exp[2] != "0":
        result = float(exp[0]) / float(exp[2])
        text(result)
    else:
        print("Invalid operation")

main()