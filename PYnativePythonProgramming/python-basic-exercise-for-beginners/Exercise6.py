# Display numbers divisible by 5 from a list

list = [10, 20, 33, 46, 55]

print("Given list is ", list)
print("Divisible by 5")

for i in list:
    if i % 5 == 0:
        print(i)
