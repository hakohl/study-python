# Definition von Funktionen

def konkat(*str):
    string = ''

    for s in str:
        string += s
    
    return string

# Hauptprogramm

print(konkat('aA', 'bB', 'cC'))