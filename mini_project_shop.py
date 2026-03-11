class Product:

    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def toon_info(self):
        print(self.naam + " - €" + str(self.prijs) + " (voorraad: " + str(self._voorraad) + ")")

    def is_op_voorraad(self):
        if self._voorraad > 0:
            return True
        else:
            return False

    def verlaag_voorraad(self, aantal):
        if aantal <= 0:
            print("Aantal moet groter dan 0 zijn")
            return False

        if aantal > self._voorraad:
            print("Niet genoeg voorraad")
            return False

        self._voorraad = self._voorraad - aantal
        return True


class Winkelmandje:

    def __init__(self):
        self.items = []

    def voeg_toe(self, product, aantal):
        self.items.append((product, aantal))
        print("Toegevoegd:", product.naam, "x", aantal)

    def toon_mandje(self):
        if len(self.items) == 0:
            print("Mandje is leeg")
            return

        totaal = 0
        for product, aantal in self.items:
            prijs = product.prijs * aantal
            totaal = totaal + prijs
            print(product.naam, "x", aantal, "- €", prijs)

        print("Totaal: €", totaal)

    def totaal_prijs(self):
        totaal = 0
        for product, aantal in self.items:
            totaal = totaal + (product.prijs * aantal)
        return totaal


producten = [
    Product("Laptop", 899, 3),
    Product("Muis", 25, 10),
    Product("Toetsenbord", 59, 5)
]

mandje = Winkelmandje()


while True:

    print("\n--- MENU ---")
    print("1 - Producten bekijken")
    print("2 - Product toevoegen")
    print("3 - Mandje bekijken")
    print("4 - Afrekenen")
    print("0 - Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        print("\nProducten:")
        i = 0
        for p in producten:
            print(i, end=" - ")
            p.toon_info()
            i = i + 1

    elif keuze == "2":
        try:
            nummer = int(input("Welk productnummer? "))
            aantal = int(input("Aantal: "))

            if nummer < 0 or nummer >= len(producten):
                print("Product bestaat niet")
                continue

            if aantal <= 0:
                print("Aantal moet groter dan 0 zijn")
                continue

            product = producten[nummer]

            if aantal > product._voorraad:
                print("Niet genoeg voorraad")
                continue

            mandje.voeg_toe(product, aantal)

        except:
            print("Foute invoer")

    elif keuze == "3":
        mandje.toon_mandje()

    elif keuze == "4":

        if len(mandje.items) == 0:
            print("Mandje is leeg")
            continue

        totaal = mandje.totaal_prijs()

        korting = 0
        if totaal > 500:
            korting = totaal * 0.10
            print("10% korting toegepast!")

        eind_totaal = totaal - korting

        for product, aantal in mandje.items:
            gelukt = product.verlaag_voorraad(aantal)
            if not gelukt:
                print("Probleem met voorraad bij", product.naam)

        print("\n--- Bonnetje ---")

        for product, aantal in mandje.items:
            subtotaal = product.prijs * aantal
            print(product.naam, "x", aantal, "- €", subtotaal)

        print("Totaal: €", totaal)

        if korting > 0:
            print("Korting: €", korting)

        print("Te betalen: €", eind_totaal)

        with open("bonnetje.txt", "a") as f:
            f.write("Nieuwe bestelling\n")
            for product, aantal in mandje.items:
                subtotaal = product.prijs * aantal
                f.write(product.naam + " x " + str(aantal) + " - €" + str(subtotaal) + "\n")
            f.write("Totaal: €" + str(totaal) + "\n")
            if korting > 0:
                f.write("Korting: €" + str(korting) + "\n")
            f.write("Te betalen: €" + str(eind_totaal) + "\n")
            f.write("----------------------\n")

        print("Bedankt voor je aankoop!")

        mandje.items = []

    elif keuze == "0":
        print("Programma gestopt")
        break

    else:
        print("Ongeldige keuze")