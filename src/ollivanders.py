class Ollivanders():

    def __init__(self, items):
        self.items = items
    def updateQuality(self):
        for item in self.items:
            item.updateQuality()

class Interfaz():
    def __init__(self):
        pass

class Item:
    def __init__(self,name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality
        
    @property
    def quality(self):
        return self._quality
        
    @quality.setter
    def quality(self,quality):
        self._quality = max(0, min(50, quality))


class NormalItem(Item, Interfaz):
    def setSellIn(self):
        self.sellIn = self.sellIn - 1
            
    def updateQuality(self):
        self.setSellIn()
        if self.sellIn > 0:
            self.quality = self.quality - 1
        else:
            self.quality = self.quality - 2

class AgedBrie(NormalItem):
    pass

class Conjured(NormalItem):
    pass

class Backstage(NormalItem):
    pass

class Sulfuras(NormalItem):
    pass

if __name__ == "__main__": 
    elixir = NormalItem("elixir", 50, 15)
    print(elixir.quality)

    