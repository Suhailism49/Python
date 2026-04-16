class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self.voorraad = voorraad

    def verlaag_voorraad(self, aantal):
        # Ongeldig aantal
        if aantal <= 0:
            return False

        # Niet genoeg voorraad
        if aantal > self.voorraad:
            return False

        # Geldig → verlaag voorraad
        self.voorraad -= aantal
        return True


class Winkelmandje:
    def __init__(self):
        self.items = []  # lijst van (Product, aantal)

    def voeg_toe(self, product, aantal):
        # Ongeldig aantal
        if aantal <= 0:
            return False

        # Probeer voorraad te verlagen
        if not product.verlaag_voorraad(aantal):
            return False

        # Voeg toe aan mandje
        self.items.append((product, aantal))
        return True

    def totaal_prijs(self):
        totaal = 0

        for product, aantal in self.items:
            totaal += product.prijs * aantal

        return totaal