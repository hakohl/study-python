# Calculate the multiplication and sum of two numbers

def printResult(num1, num2):
    product = num1 * num2

    if product > 1000:
        print(num1 + num2)
    else:
        print(product)
    


# main program

number1 = int(input ("number1: "))
number2 = int(input ("number2: "))

printResult (number1, number2)