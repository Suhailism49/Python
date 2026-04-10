from shop.product import Product
from shop.mandje import Winkelmandje


def vraag_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer, voer een heel getal in.")


def toon_producten(producten):
    print("\n--- PRODUCTEN ---")
    for i, product in enumerate(producten, start=1):
        print(f"{i}. ", end="")
        product.toon_info()


def main():
    producten = [
        Product("Laptop", 899, 3),
        Product("Muis", 25, 10),
        Product("Toetsenbord", 59, 5)
    ]

    mandje = Winkelmandje()

    while True:
        print("\n--- MENU ---")
        print("1. Toon producten")
        print("2. Voeg toe aan mandje")
        print("3. Toon mandje")
        print("0. Stoppen")

        keuze = vraag_int("Kies: ")

        if keuze == 1:
            toon_producten(producten)

        elif keuze == 2:
            toon_producten(producten)

            product_nummer = vraag_int("Kies productnummer: ")
            aantal = vraag_int("Aantal: ")

            if 1 <= product_nummer <= len(producten):
                product = producten[product_nummer - 1]
                mandje.voeg_toe(product, aantal)
            else:
                print("Ongeldig productnummer.")

        elif keuze == 3:
            mandje.toon()

        elif keuze == 0:
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    main()