jahr = int(input("Jahr: "))
           
if ((not jahr%400) or ((not jahr%4) and (jahr//100))):
    print("Das Jahr", jahr, "ist ein Schaltjahr.")
else:
    print("Das Jahr", jahr, "ist kein Schaltjahr.")
