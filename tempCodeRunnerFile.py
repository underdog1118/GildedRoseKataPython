        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 11, "Aged Brie quality should increase by 1"