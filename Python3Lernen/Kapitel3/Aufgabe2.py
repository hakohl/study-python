print("Kostenplan für eine Reise")
print("---------------------------")

kostenReisebus = float(input("Kosten für den Reisebus: "))
kostenPersonHotel = float(input("Hotelkosten pro Person: "))
kostenEvents = float(input("Gesamtkosten für touristische Events: "))
anzahlPersonen = float(input("Anzahl der Teilnehmer: "))

kostenPerson = kostenReisebus / anzahlPersonen + kostenPersonHotel + kostenEvents /anzahlPersonen
gesamtKosten = kostenPerson * anzahlPersonen

print("Kosten pro Person: ", kostenPerson)
print("Gesamtkosten: ", gesamtKosten)
