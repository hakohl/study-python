# Check user input is a positive number or negative

num = input("Enter a number: ")

try:
    val = int(num)
    if val >= 0:
        print("Num", num, "is a positive number.")
    else:
        print("Num", num, "is a negative number.")
except ValueError:
    print("It's not a number, it's a string!")
