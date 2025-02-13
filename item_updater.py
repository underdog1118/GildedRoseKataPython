class ItemUpdater:
    def update(self, item):
        raise NotImplementedError
    
class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1
        if item.quality < 0:
            item.quality = 0

class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
        if item.quality > 50:
            item.quality = 50

class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        # Sulfuras doesn't change in quality or sell_in
        pass

class BackstagePassUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality += 3
        elif item.sell_in < 10:
            item.quality += 2
        else:
            item.quality += 1
        if item.quality > 50:
            item.quality = 50

class ConjuredItemUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 2
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
        if item.quality < 0:
            item.quality = 0