# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags


class MyItems(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tags = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field(
    	input_processor = MapCompose(str.strip),
    	output_processor = TakeFirst()
    	)
    birthdate = scrapy.Field()

    pass
