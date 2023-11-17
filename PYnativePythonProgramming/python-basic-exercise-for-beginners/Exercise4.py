# Remove first n characters from a string 

def remove_chars(str, n):
    string = str[n:]
    return string



# main

string = input("String: ")
cut = int(input("Cut?: "))

print("Stripped string: ", remove_chars(string, cut))


