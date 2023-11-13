# Verstecke Buchstaben

import random

def verstecke(str, anz):
    string = ''
    n = anz

    for s in str:
        string += s
    
        # bestimme zufällige Großbuchstaben und hänge sie an

        for i in range (n):
            indexGB = random.randint (0, 25) + 65
            GB = chr (indexGB)
            string += GB

    return string


# Hauptprogramm

str = 'uuAiiiFJKpojmj'
anz = 3

str = str.upper()

print (verstecke (str, anz))