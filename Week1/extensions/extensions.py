
def text(select, type):
    if select == 1 and (type == "jpg" or type == "jpeg"):
        print("image/jpeg") 
    elif select == 1 and type == "txt":
        print("text/plain")
    elif select == 1:
        print(f"image/{type}")
    
    else:
        print(f"application/{type}")

def main():
    name = input("Name: ").strip().lower()
    format = name.split('.')
    type = format[-1]

    if type == "gif" or type == "jpg" or type == "jpeg" or type == "png" or type == "txt":
        text(1, type)
    elif type == "pdf" or type == "zip":
        text(2, type)
    else:
        print("application/octet-stream")

main()        