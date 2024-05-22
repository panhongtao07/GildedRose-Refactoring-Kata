# -*- coding: utf-8 -*-

class GildedRose:
    MAX_QUALITY = 50

    def __init__(self, items: list['Item']):
        self.items = items

    @staticmethod
    def is_item_immutable(item: 'Item') -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"

    @staticmethod
    def is_time_sensitive(item: 'Item') -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

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
            if self.is_item_immutable(item):
                continue
            item.sell_in -= 1
            if item.name == "Aged Brie":
                self._increase_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._increase_quality(item)
                if item.sell_in < 10:
                    self._increase_quality(item)
                if item.sell_in < 5:
                    self._increase_quality(item)
            else:
                self._decrease_quality(item)
            if item.sell_in < 0:
                if self.is_time_sensitive(item):
                    item.quality = 0
                elif item.name == "Aged Brie":
                    self._increase_quality(item)
                else:
                    self._decrease_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
