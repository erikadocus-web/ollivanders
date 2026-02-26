from src.ollivanders import Ollivanders, NormalItem, AgedBrie, Backstage, Conjured, Sulfuras

def main():
    print("Bienvenido a la tienda de Ollivanders")

if __name__ == "__main__":
    items = [
        NormalItem("Varita de roble", 10, 20),
        AgedBrie("Reliquia encantada antigua", 2, 0),
        Backstage("Entrada al Torneo de los Tres Magos", 15, 20),
        Conjured("Poción conjurada", 3, 6),
        Sulfuras("Sulfuras, la varita eterna", 0, 80)
    ]

    tienda = Ollivanders(items)

    for day in range(31):
        print(f"\nDia {day}")
        for item in items:
            print(f"{item.name}, SellIn: {item.sellIn}, Quality: {item.quality}")

        tienda.updateQuality()