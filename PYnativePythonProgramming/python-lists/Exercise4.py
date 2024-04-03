# Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res_list = []

for i in list1:
    for j in list2:
        res_list.append(i + j)

print(res_list)