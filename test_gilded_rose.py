# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # # example of test that checks for logical errors
    # def test_sulfuras_should_not_decrease_quality(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     sulfuras_item = items[0]
    #     self.assertEqual(80, sulfuras_item.quality)
    #     self.assertEqual(4, sulfuras_item.sell_in)
    #     self.assertEqual("Sulfuras", sulfuras_item.name)

    # # example of test that checks for syntax errors
    # def test_gilded_rose_list_all_items(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     all_items = gilded_rose.get_item()
    #     self.assertEqual(["Sulfuras"], all_items)




    # test 1 that checks for logical errors
    def test_quality_never_exceed_50(self):
        items = [Item(name="Aged Brie", sell_in=10, quality=49.2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertLess(items[0].quality, 50, "FAIL: The quality of an item should never be more than 50.")

    # test 2 that checks for logical errors
    def test_quality_never_negative(self):
        items = [Item("Normal Item", 10, 0.8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0, "FAIL: The quality should be non-negative but found negative.")


    # test 3 that checks for logical errors
    def test_conjured_quality_degrade_twice(self):
        items = [Item("Conjured", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8, "FAIL:Conjured items degrade in Quality twice as fast as normal items.")        


    # test 4 that checks for syntax errors
    def test_invalid_item_initialization(self):
        items = [Item("Invalid Item", 5)]  # missing 1 required positional argument



if __name__ == '__main__':
    unittest.main()
