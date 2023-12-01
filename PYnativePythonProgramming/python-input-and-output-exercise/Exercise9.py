# Check file is empty or not

import os

file_name = input("Enter filename: ")

file_size = os.path.getsize(file_name)
print(f"Size of file {file_name} is {file_size} bytes.")
