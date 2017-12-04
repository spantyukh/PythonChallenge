number = ""
while not number:
    try:
        print("Enter the number: ")
        number = float(input())
    except ValueError:
        print("!!!!!")
if (number % 3) == 0:
    print("True")
else: print("False")
input("Press any key")

