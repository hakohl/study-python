# Format variables using a string.format() method.

totalMoney = int(input("Total money: "))
quantity = int(input("Quantity: "))
price = float(input("Price: "))

print("I have {0} dollars So I can buy {1} football for {2:.2f} dollars.".format(totalMoney, quantity, price))
