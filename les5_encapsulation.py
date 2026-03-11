class Student:

    def __init__(self, naam, leeftijd):
        self.naam = naam
        self._leeftijd = leeftijd

    def get_leeftijd(self):
        return self._leeftijd

    def set_leeftijd(self, nieuwe_leeftijd):
        if nieuwe_leeftijd < 0:
            print("Leeftijd mag niet negatief zijn!")
            return
        if nieuwe_leeftijd > 130:
            print("Leeftijd mag niet hoger dan 130 zijn!")
            return
        self._leeftijd = nieuwe_leeftijd

    def verjaar(self):
        leeftijd_nu = self.get_leeftijd()
        leeftijd_nu = leeftijd_nu + 1
        self.set_leeftijd(leeftijd_nu)


s1 = Student("Ali", 19)

print(s1.get_leeftijd())

s1.set_leeftijd(20)
print(s1.get_leeftijd())

s1.set_leeftijd(-5)

s1.set_leeftijd(150)

s1.verjaar()
print(s1.get_leeftijd())