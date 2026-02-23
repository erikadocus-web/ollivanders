class Ollivanders():
    def __init__(self):
        self.inventory = {}

    class Item():
        def __init__(self):
            self.name = ""
            self.sellIn = 0
            self.quality = 0

        def updateQuality(self):
            pass

    class NormalItem(Item):
        def __init__(self, name, sellIn, quality):
            self.name = name
            self.sellIn = sellIn
            self.quality = quality

        def updateQuality(self):
            q = 1
            if self.sellIn >= 0:
                self.quality = self.quality - q * 1
            else:
                self.quality = self.quality - q *2
            
            print(f"Calidad nueva de {self.name} es {self.quality}")

if __name__ == "__main__": 
    Ollivanders = Ollivanders()
    normalItem = Ollivanders.NormalItem("item1", 10, 20)
    normalItem.updateQuality()

    