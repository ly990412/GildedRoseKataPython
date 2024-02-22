# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
   

        
    # my test1
    def test1(self):
        items = [
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items[0].quality, 80)
        self.assertEqual(gr.items[1].sell_in, -1)
        self.assertEqual(gr.items[1].quality, 80)



    # my test2 
    def test2(self):
        items = [
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Aged Brie", sell_in=0, quality=50),
             Item(name="Aged Brie", sell_in=0, quality=48),
             Item(name="Aged Brie", sell_in=0, quality=49),
             Item(name="Aged Brie", sell_in=0, quality=40)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items[0].sell_in, 1)
        self.assertEqual(gr.items[0].quality, 1)
        self.assertEqual(gr.items[1].sell_in,-1)
        self.assertEqual(gr.items[1].quality, 50)
        self.assertEqual(gr.items[2].quality, 50)
        self.assertEqual(gr.items[3].quality, 50)
        self.assertEqual(gr.items[4].quality, 42)


    # my test3
    def test3(self):
        items = [
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=0),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=0),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=0),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
             ]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items[0].sell_in, 1)
        self.assertEqual(gr.items[0].quality, 3)
        self.assertEqual(gr.items[1].quality, 2)
        self.assertEqual(gr.items[2].quality, 1)
        self.assertEqual(gr.items[3].quality, 0)




if __name__ == '__main__':
    unittest.main()
