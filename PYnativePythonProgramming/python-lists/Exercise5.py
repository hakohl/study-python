# Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2.reverse()

for i in range(4):
    print(str(list1[i]) + " " + str(list2[i]))
