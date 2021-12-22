# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VeromodaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    old_price= scrapy.Field()
    Size = scrapy.Field()
    Stock = scrapy.Field()
    product_description_text = scrapy.Field()
    product_table = scrapy.Field()
    size_table_labels = scrapy.Field()
    size_table = scrapy.Field()
    sub_catogery = scrapy.Field()
    images = scrapy.Field()