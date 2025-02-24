import pprint


class Prodotto():
    def __init__(self, nome: str, quantità: int, prezzo: float):
        self.nome = nome
        self.quantità = quantità
        self.prezzo = prezzo

    def __str__(self):

        output = f"""
            Nome: {self.nome}
            Quantità: {self.quantità}
            Prezzo: {self.prezzo}
        """

        return output


class Inventario():
    def __init__(self):
        self.prodotti = {}

    def aggiungi(self, prod: Prodotto):
        self.prodotti[prod.nome] = prod

    def rimuovi(self, nome_prod: str) -> Prodotto:
        return self.prodotti.pop(nome_prod)

    def aggiorna(self, nome_prod: str, quantità: float):
        self.prodotti[nome_prod].quantità = quantità

    def calcola_valore_totale(self) -> float:
        totale = 0
        for key, value in self.prodotti.items():
            print(value.prezzo)
            totale += value.prezzo * value.quantità

        return totale

    def stampa(self):
        print("Stampa inventario:")
        for key, value in self.prodotti.items():
            print(value)


def gestisci_scelta(invent: Inventario, scelta: str):
    scelta = scelta.strip()

    if scelta == "6":
        print("Arrivederci!")
        exit(0)
    elif scelta == "1":
        print("Di seguito dimmi quale prodotto vuoi aggiungere")
        nome = input("Nome Prodotto: ")
        quantità = int(input("Quantità: "))
        prezzo = float(input("Prezzo: "))

        invent.aggiungi(
            Prodotto(nome, quantità, prezzo)
        )
    elif scelta == "2":
        nome = input("Quale prodotto vuoi rimuovere?: ")
        invent.rimuovi(nome)
    elif scelta == "3":
        nome = input("Quale prodotto vuoi aggiornate?: ")
        quantità = int(input("Quantità: "))
        invent.aggiorna(nome, quantità)
    elif scelta == "4":
        invent.stampa()
    elif scelta == "5":
        print("Valore totale {}".format(invent.calcola_valore_totale()))
    else:
        print(f"Scelta non valida: {scelta}")


def main():
    inventario = Inventario()

    print("""
Benvenuto nel sistema di gestione dell'inventario!

1. Aggiungi un prodotto
2. Rimuovi un prodotto
3. Modifica la quantità di un prodotto
4. Visualizza inventario
5. Calcola valore totale
6. Esci
"""
)

    scelta = input("Fai la tua scelta: ")
    while scelta != "6":
        gestisci_scelta(inventario, scelta)
        scelta = input("Fai la tua scelta: ")


if __name__ == "__main__":
    main()

