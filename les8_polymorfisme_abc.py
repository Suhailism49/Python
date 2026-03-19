from abc import ABC, abstractmethod

# Stap 3 — Abstracte class
class Betaalmethode(ABC):
    def __init__(self, naam):
        self.naam = naam

    @abstractmethod
    def betaal(self, bedrag):
        pass


# Stap 4 — Subclasses

class PinBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Pin")

    def betaal(self, bedrag):
        return f"{self.naam}: Betaling van €{bedrag} gepind."


class ContantBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Contant")

    def betaal(self, bedrag):
        return f"{self.naam}: €{bedrag} contant ontvangen."


class OnlineBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Online")

    def betaal(self, bedrag):
        return f"{self.naam}: Betaling van €{bedrag} online verwerkt."


# Stap 6 — Test met een lijst

methodes = [PinBetaling(), ContantBetaling(), OnlineBetaling()]

for methode in methodes:
    print(methode.betaal(49.95))