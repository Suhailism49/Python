class Student:

    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def begroet(self):
        print(f"Hallo, ik ben {self.naam}!")


studenten = [
    Student("Ali", 19),
    Student("Sara", 20),
    Student("Jan", 18),
]


for s in studenten:
    s.begroet()


aantal_18_plus = 0

for s in studenten:
    if s.leeftijd >= 18:
        aantal_18_plus += 1

print(f"Aantal studenten van 18 jaar of ouder: {aantal_18_plus}")


totaal_leeftijd = 0

for s in studenten:
    totaal_leeftijd += s.leeftijd

gemiddelde = totaal_leeftijd / len(studenten)

print(f"De gemiddelde leeftijd is: {gemiddelde}")