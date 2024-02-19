# Count the total number of digits in a number

ori_number = 75869
number = ori_number
count = 0

while number != 0:
    count += 1
    number = number // 10

print("Die Zahl", ori_number, "hat", count ,"Stellen.")
