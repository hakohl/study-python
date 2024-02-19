# Use a loop to display elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

index = 0

for i in my_list:
    if index % 2 != 0:
        print(i, end=" ")
    index += 1
