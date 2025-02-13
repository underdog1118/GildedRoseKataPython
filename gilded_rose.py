# -*- coding: utf-8 -*-
from item_updater import AgedBrieUpdater
from item_updater import SulfurasUpdater
from item_updater import BackstagePassUpdater
from item_updater import ConjuredItemUpdater
from item_updater import NormalItemUpdater

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items


    def update_quality(self):
        for item in self.items:
            updater = self.get_updater(item)
            updater.update(item)

    def get_updater(self, item):
        if "Aged Brie" in item.name:
            return AgedBrieUpdater()
        elif "Sulfuras" in item.name:
            return SulfurasUpdater()
        elif "Backstage pass" in item.name:
            return BackstagePassUpdater()
        elif "Conjured" in item.name:
            return ConjuredItemUpdater()
        else:
            return NormalItemUpdater()