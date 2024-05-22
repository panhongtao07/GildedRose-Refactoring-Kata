# -*- coding: utf-8 -*-

class GildedRose:
    MAX_QUALITY = 50

    def __init__(self, items: list['Item']):
        self.items = items

    @staticmethod
    def is_item_immutable(item: 'Item') -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"

    def _update_quality(self, item: 'Item', value: int = 1):
        if self.is_item_immutable(item):
            return
        item.quality += value
        item.quality = max(0, min(self.MAX_QUALITY, item.quality))

    def _increase_quality(self, item: 'Item', value: int = 1):
        self._update_quality(item, value)

    def _decrease_quality(self, item: 'Item', value: int = 1):
        self._update_quality(item, -value)

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                self._decrease_quality(item)
            else:
                self._increase_quality(item)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        self._increase_quality(item)
                    if item.sell_in < 6:
                        self._increase_quality(item)
            if not self.is_item_immutable(item):
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        self._decrease_quality(item)
                    else:
                        item.quality = 0
                else:
                    self._increase_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
