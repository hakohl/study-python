# Accept a list of 5 float numbers as an input from the user

float_list = []

for i in range(5):
    float_num = float(input("Enter float number: "))
    float_list.append(float_num)

print(float_list)
