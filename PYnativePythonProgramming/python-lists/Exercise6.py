# Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

empty_item_count = list1.count("")

while empty_item_count > 0:
    list1.remove("")
    empty_item_count -= 1

print(list1)