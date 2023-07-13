print("Bitte geben Sie die ersten Titel der Charts ein!")

titelList = []
titel = input("Titel: ")
titelList.append(titel)
titel = input("Titel: ")
titelList.append(titel)
titel = input("Titel: ")
titelList.append(titel)

print()
print("Hier sind die ersten drei Titel der Charts:")

for i in (1, 2, 3):
    print("Platz", i, ":", titelList[i-1])