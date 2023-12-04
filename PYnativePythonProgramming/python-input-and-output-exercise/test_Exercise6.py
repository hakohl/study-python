# Write all content of a given file into a new file by skipping line number 5

with open('new_file.txt', 'w') as new_file, open('test.txt', 'r') as base_file:
    line_number = 0

    for line in base_file:
        line_number+=1
        
        if line_number != 5:
            new_file.write(line)

new_file = open('new_file.txt', 'r')
print(new_file.read())

def test_answer():
    lines = []

    with open('new_file.txt') as f:
        lines = f.readlines()
        print(lines)
        assert "line4" not in lines
        