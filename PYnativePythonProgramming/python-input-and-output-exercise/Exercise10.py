# Read line number 4 from the following file

with open('test.txt', 'r') as f:
    line_number = 0

    for line in f:
        line_number+=1
        
        if line_number == 4:
            print(line)
