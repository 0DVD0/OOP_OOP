import random
from abc import ABC, abstractmethod


# Abstract Base Class for all entities in the ecosystem
class EntitateEcosistem(ABC):
    def __init__(self, nume, energie, x, y, rataSupravietuire):
        self.nume = nume
        self.energie = energie
        self.x = x
        self.y = y
        self.rataSupravietuire = rataSupravietuire

    @abstractmethod
    def actioneaza(self):
        pass

    @abstractmethod
    def reproduce(self):
        pass


# Plant class
class Planta(EntitateEcosistem):
    def __init__(self, nume, energie, x, y, rataSupravietuire, rataCrestere):
        super().__init__(nume, energie, x, y, rataSupravietuire)
        self.rataCrestere = rataCrestere

    def actioneaza(self):
        self.energie += self.rataCrestere
        print(f"{self.nume} crește, energie: {self.energie}")

    def reproduce(self):
        if self.energie > 10:
            self.energie -= 5
            print(f"{self.nume} s-a reprodus!")
            return Planta(self.nume, 5, random.randint(0, 9), random.randint(0, 9), self.rataSupravietuire,
                          self.rataCrestere)
        return None


# Abstract Animal class
class Animal(EntitateEcosistem, ABC):
    def __init__(self, nume, energie, x, y, rataSupravietuire, viteza, tipHrana):
        super().__init__(nume, energie, x, y, rataSupravietuire)
        self.viteza = viteza
        self.tipHrana = tipHrana

    @abstractmethod
    def mananca(self, hrana):
        pass

    def deplaseaza(self):
        self.x += random.randint(-self.viteza, self.viteza)
        self.y += random.randint(-self.viteza, self.viteza)
        print(f"{self.nume} s-a deplasat la ({self.x}, {self.y})")


# Herbivore class
class Erbivor(Animal):
    def __init__(self, nume, energie, x, y, rataSupravietuire, viteza):
        super().__init__(nume, energie, x, y, rataSupravietuire, viteza, "planta")

    def mananca(self, planta):
        if isinstance(planta, Planta):
            self.energie += planta.energie
            planta.energie = 0
            print(f"{self.nume} a mâncat o plantă, energie: {self.energie}")

    def actioneaza(self):
        self.deplaseaza()

    def reproduce(self):
        if self.energie > 20:
            self.energie -= 10
            print(f"{self.nume} s-a reprodus!")
            return Erbivor(self.nume, 10, random.randint(0, 9), random.randint(0, 9), self.rataSupravietuire,
                           self.viteza)
        return None


# Carnivore class
class Carnivor(Animal):
    def __init__(self, nume, energie, x, y, rataSupravietuire, viteza):
        super().__init__(nume, energie, x, y, rataSupravietuire, viteza, "animal")

    def mananca(self, prada):
        if isinstance(prada, Animal):
            self.energie += prada.energie
            prada.energie = 0
            print(f"{self.nume} a vânat {prada.nume}, energie: {self.energie}")

    def actioneaza(self):
        self.deplaseaza()

    def reproduce(self):
        if self.energie > 30:
            self.energie -= 15
            print(f"{self.nume} s-a reprodus!")
            return Carnivor(self.nume, 15, random.randint(0, 9), random.randint(0, 9), self.rataSupravietuire,
                            self.viteza)
        return None


# Ecosystem class
class Ecosistem:
    def __init__(self, dimensiune):
        self.dimensiune = dimensiune
        self.entitati = []

    def adauga_entitate(self, entitate):
        self.entitati.append(entitate)

    def elimina_entitate(self, entitate):
        self.entitati.remove(entitate)

    def simuleaza_pasi(self, pasi):
        for _ in range(pasi):
            print("-- Pas Simulare --")
            for entitate in self.entitati:
                entitate.actioneaza()
                if isinstance(entitate, Animal):
                    if entitate.energie <= 0:
                        print(f"{entitate.nume} a murit.")
                        self.elimina_entitate(entitate)
                reproducere = entitate.reproduce()
                if reproducere:
                    self.adauga_entitate(reproducere)

    def afisare_stare(self):
        print("-- Starea Ecosistemului --")
        for entitate in self.entitati:
            print(f"{entitate.nume} la ({entitate.x}, {entitate.y}) cu energie {entitate.energie}")


# Testing the Ecosystem
if __name__ == "__main__":
    ecosistem = Ecosistem(dimensiune=10)

    planta1 = Planta("Feriga", 5, 2, 2, 0.8, 2)
    erbivor1 = Erbivor("Iepure", 10, 3, 3, 0.9, 1)
    carnivor1 = Carnivor("Lup", 15, 5, 5, 0.95, 2)

    ecosistem.adauga_entitate(planta1)
    ecosistem.adauga_entitate(erbivor1)
    ecosistem.adauga_entitate(carnivor1)

    ecosistem.afisare_stare()
    ecosistem.simuleaza_pasi(5)
    ecosistem.afisare_stare()
