from .product import Product


class Winkelmandje:
    def __init__(self):
        self.items = []

    def voeg_toe(self, product, aantal):
        if not isinstance(product, Product):
            print("Ongeldig product.")
            return

        if product.is_op_voorraad(aantal):
            product.verlaag_voorraad(aantal)
            self.items.append((product, aantal))
            print(f"{aantal} x {product.naam} toegevoegd aan mandje.")
        else:
            print(f"Niet genoeg voorraad van {product.naam}.")

    def totaal_prijs(self):
        totaal = 0
        for product, aantal in self.items:
            totaal += product.prijs * aantal
        return totaal

    def toon(self):
        if not self.items:
            print("Je winkelmandje is leeg.")
            return

        print("\n--- WINKELMANDJE ---")
        for product, aantal in self.items:
            subtotaal = product.prijs * aantal
            print(f"{product.naam} x {aantal} = €{subtotaal:.2f}")

        print(f"Totaal: €{self.totaal_prijs():.2f}")