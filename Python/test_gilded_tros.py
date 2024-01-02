# -*- coding: utf-8 -*-
import unittest

from gilded_tros import Item, GildedTros


class GildedTrosTest(unittest.TestCase):
    def test_foo(self) -> None:
        sell_in = 5
        quality = 9
        items = [Item(name="foo", sell_in=sell_in, quality=quality)]
        gilded_tros = GildedTros(items=items)
        for x in range(0, 6):
            sell_in -= 1
            quality -= 1 if items[0].sell_in > 0 else 2
            gilded_tros.update_items()
            self.assertEqual(first="foo", second=items[0].name)
            self.assertEqual(first=sell_in, second=items[0].sell_in)
            self.assertEqual(first=quality, second=items[0].quality)

    def test_quality_degrading_after_sell_by_date_passed(self) -> None:
        items = [
            Item(name="Item sell date passed", sell_in=1, quality=3)
        ]
        gilded_tros = GildedTros(items=items)

        gilded_tros.update_items()
        self.assertEqual(first=0, second=items[0].sell_in)
        self.assertEqual(first=2, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=-1, second=items[0].sell_in)
        self.assertEqual(first=0, second=items[0].quality)

    def test_quality_never_negative(self) -> None:
        items = [
            Item(name="Quality not negative", sell_in=0, quality=0)
        ]
        gilded_tros = GildedTros(items=items)

        gilded_tros.update_items()
        self.assertEqual(first=-1, second=items[0].sell_in)
        self.assertEqual(first=0, second=items[0].quality)

    def test_good_wine_quality_increase(self) -> None:
        items = [
            Item(name="Good Wine", sell_in=1, quality=0)
        ]
        gilded_tros = GildedTros(items=items)

        gilded_tros.update_items()
        self.assertEqual(first=0, second=items[0].sell_in)
        self.assertEqual(first=1, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=-1, second=items[0].sell_in)
        self.assertEqual(first=3, second=items[0].quality)

    def test_quality_not_over_50(self) -> None:
        items = [
            Item(name="Good Wine", sell_in=0, quality=49)
        ]
        gilded_tros = GildedTros(items=items)

        gilded_tros.update_items()
        self.assertEqual(first=-1, second=items[0].sell_in)
        self.assertEqual(first=50, second=items[0].quality)

    def test_legendary_item(self) -> None:
        items = [
            Item(name="B-DAWG Keychain", sell_in=1, quality=80)
        ]
        gilded_tros = GildedTros(items=items)

        gilded_tros.update_items()
        self.assertEqual(first=1, second=items[0].sell_in)
        self.assertEqual(first=80, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=1, second=items[0].sell_in)
        self.assertEqual(first=80, second=items[0].quality)

    def test_backstage_passes(self) -> None:
        items = [
            Item(name="Backstage passes for Re:Factor", sell_in=6, quality=20)
        ]
        gilded_tros = GildedTros(items=items)

        gilded_tros.update_items()
        self.assertEqual(first=5, second=items[0].sell_in)
        self.assertEqual(first=22, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=4, second=items[0].sell_in)
        self.assertEqual(first=25, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=3, second=items[0].sell_in)
        self.assertEqual(first=28, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=2, second=items[0].sell_in)
        self.assertEqual(first=31, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=1, second=items[0].sell_in)
        self.assertEqual(first=34, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=0, second=items[0].sell_in)
        self.assertEqual(first=37, second=items[0].quality)

        gilded_tros.update_items()
        self.assertEqual(first=-1, second=items[0].sell_in)
        self.assertEqual(first=0, second=items[0].quality)

    def test_smelly_items(self) -> None:
        items = [
            Item(name="Duplicate Code", sell_in=1, quality=8),
            Item(name="Long Methods", sell_in=1, quality=8),
            Item(name="Ugly Variable Names", sell_in=1, quality=8)
        ]
        gilded_tros = GildedTros(items=items)

        gilded_tros.update_items()
        for item in items:
            self.assertEqual(first=0, second=item.sell_in)
            self.assertEqual(first=6, second=item.quality)

        gilded_tros.update_items()
        for item in items:
            self.assertEqual(first=-1, second=item.sell_in)
            self.assertEqual(first=2, second=item.quality)


if __name__ == '__main__':
    unittest.main()
