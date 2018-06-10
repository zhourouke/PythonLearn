# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TutorialItem(Item):
    # define the fields for your item here like:
    title = Field()
    abstract = Field()
    nickname = Field()
    comments = Field()
    likes = Field()
    money = Field()
