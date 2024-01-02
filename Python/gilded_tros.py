# -*- coding: utf-8 -*-

class GildedTros:
    _legendary_item_name = "B-DAWG Keychain"

    def __init__(self, items: list["Item"]) -> None:
        self.items = items

    def update_items(self) -> None:
        for item in self.items:
            if item.name == self._legendary_item_name:
                continue
            self._update_quality(item=item)

    @staticmethod
    def _update_quality(item: "Item") -> None:
        if item.name != "Good Wine" and item.name != "Backstage passes for Re:Factor" and item.name != "Backstage passes for HAXX":
            if item.quality > 0:
                item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes for Re:Factor" or item.name == "Backstage passes for HAXX":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Good Wine":
                if item.name != "Backstage passes for Re:Factor" and item.name != "Backstage passes for HAXX":
                    if item.quality > 0:
                        item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1


class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
