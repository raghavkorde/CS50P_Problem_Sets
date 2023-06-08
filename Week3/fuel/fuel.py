def main():
    out = getFraction("Fraction: ")
    print(out)

def getFraction(prompt):
    while True:
        try:
            p, q = input(prompt).split('/')
            fraction = int(p)/int(q)
            if 0 <= fraction <= 0.1:
                return("E")
            elif 0.9 <= fraction <= 1:
                return("F")
            elif 0.1 < fraction < 0.9:
                return(f"{round(fraction * 100)}%")
        except(ValueError, ZeroDivisionError):
            pass

main()
        