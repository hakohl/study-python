alkaliMetalle = ("Li", "Na", "K", "Rb", "Cs")

print("Bitte geben Sie die Formel eines chemischen Elementes an.")
element = input("Element: ")

if element in alkaliMetalle:
    print("Es handelt sich um ein Alkalimetall.")