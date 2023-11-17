# Check if the first and last number of a list is the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

for i in [numbers_x, numbers_y]:
    print(i)

    if i[0] == i[-1]:
        print("result is True")
    else:
        print("result is False")
    

