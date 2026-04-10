import json
from pathlib import Path


class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def to_dict(self):
        return {
            "naam": self.naam,
            "prijs": self.prijs,
            "voorraad": self._voorraad
        }

    @staticmethod
    def from_dict(data):
        return Product(
            data["naam"],
            data["prijs"],
            data["voorraad"]
        )


def save_producten(producten, filename):
    data = [p.to_dict() for p in producten]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_producten(filename):
    if not Path(filename).exists():
        return []

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Product.from_dict(d) for d in data]


def vraag_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer, voer een heel getal in.")


def vraag_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ongeldige invoer, voer een geldig getal in.")


def toon_producten(producten):
    if not producten:
        print("Geen producten gevonden.")
        return

    print("\n--- PRODUCTEN ---")
    for i, product in enumerate(producten, start=1):
        print(f"{i}. {product.naam} | €{product.prijs:.2f} | voorraad: {product._voorraad}")


def main():
    filename = "producten.json"
    producten = load_producten(filename)

    if not producten:
        producten = [
            Product("Muis", 25.0, 10),
            Product("Toetsenbord", 45.0, 5),
            Product("Monitor", 199.99, 3)
        ]

    while True:
        print("\n--- MENU ---")
        print("1. Toon producten")
        print("2. Product toevoegen")
        print("3. Opslaan")
        print("0. Stoppen")

        keuze = vraag_int("Kies: ")

        if keuze == 1:
            toon_producten(producten)

        elif keuze == 2:
            naam = input("Naam van product: ")
            prijs = vraag_float("Prijs: ")
            voorraad = vraag_int("Voorraad: ")

            nieuw_product = Product(naam, prijs, voorraad)
            producten.append(nieuw_product)
            print(f"Product '{naam}' toegevoegd.")

        elif keuze == 3:
            save_producten(producten, filename)
            print("Producten opgeslagen.")

        elif keuze == 0:
            save_producten(producten, filename)
            print("Producten opgeslagen. Programma gestopt.")
            break

        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    main()