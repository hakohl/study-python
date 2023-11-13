# Print the sum of the current number and the previous number

previous_num = 0

for current_num in range(10):
    print("Current Number ",  current_num, " Previous Number ",  previous_num,  "Sum:  ", current_num + previous_num)
    previous_num = current_num