# Remove all occurrences of a specific item from a list

list1 = [5, 20, 15, 20, 25, 50, 20]

count = list1.count(20)

while count > 0:
    list1.remove(20)
    count -= 1

print(list1)