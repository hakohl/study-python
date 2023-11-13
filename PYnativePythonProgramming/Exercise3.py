# Print characters from a string that are present at an even index number

str = input("String: ")

print("Original String is", str)
print("Printing only even index chars")

size = len(str)

for c in range(0, size - 1, 2):
    print(str[c])