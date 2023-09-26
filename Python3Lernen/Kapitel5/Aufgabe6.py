print("Kreditberechnung\n")

kreditSumme = int(input("Kreditsumme in Euro: "))
zinssatzJahr = int(input("Zinssatz (Prozent pro Jahr): "))
rückzahlungJahr = int(input("Jährliche Rückzahlung in Euro: "))
jahr = 2023   # besser: jahr = time.localtime()[0]  # aktuelles Jahr

print("\n")     # besser: print()

restSchulden = kreditSumme

while (restSchulden > rückzahlungJahr):
    zinsen = round(zinssatzJahr / 100 * restSchulden)
    tilgung = rückzahlungJahr - zinsen
    restSchulden -= tilgung
    print(str(jahr) + " Zinsen: " + str(zinsen) + " Tilgung " + str(tilgung) + " Restschulden: " + str(restSchulden))
    # besser: print(jahr, " Zinsen:", zinsen, "EUR", " Tilgung:", tilgung, "EUR", " Restschulden", restSchulden, "EUR")
    jahr += 1

print("Restforderung: " + str(restSchulden))

