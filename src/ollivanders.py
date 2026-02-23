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

if __name__ == "__main__": 
    Ollivanders = Ollivanders()
    normalItem = Ollivanders.NormalItem("item1", 10, 20)
    normalItem.updateQuality()

    