# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags


def remove_newline(value):
    return value.replace('\n', '')


def remove_char(value):
    return value.replace('৳', '').replace(',', '')


class StylehaatItem(scrapy.Item):
    breadcrumb = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_tags, remove_newline)
    )
    product_name = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_tags, remove_newline),
        output_processor=TakeFirst()
    )
    product_old_price = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_tags, remove_newline, remove_char)
    )
    product_new_price = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_tags, remove_newline, remove_char),
    )
    images = scrapy.Field()
    image_urls = scrapy.Field()
    more_info = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_tags, remove_newline),
        output_processor=Join('')
    )
