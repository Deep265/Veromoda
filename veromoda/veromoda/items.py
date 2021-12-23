# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

Source = "Veromoda"
class VeromodaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
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
    """
    source = scrapy.Field()
    Native_product_id = scrapy.Field()
    product_id = scrapy.Field()
    Category = scrapy.Field()
    Subcategory1 = scrapy.Field()
    Subcategory2 = scrapy.Field()
    Subcategory3 = scrapy.Field()
    Title = scrapy.Field()
    Brand = scrapy.Field()
    Item_url = scrapy.Field()
    currentPrice = scrapy.Field()
    originalPrice = scrapy.Field()
    discount = scrapy.Field()
    currencyIso = scrapy.Field()
    product_detail = scrapy.Field()
    PrimaryColor = scrapy.Field()
    available_colors = scrapy.Field()
    ManufacturedBy = scrapy.Field()
    CountryOfOrigin = scrapy.Field()
    image_urls = scrapy.Field()
    sizeTag = scrapy.Field()
    Description = scrapy.Field()
  # Ratings = scrapy.Field()
  #  Review_counts = scrapy.Field()
    fabric = scrapy.Field()
    pattern = scrapy.Field()
    length = scrapy.Field()
    sleeve_styling = scrapy.Field()
    neck = scrapy.Field()
    occasion = scrapy.Field()
    fit = scrapy.Field()
    # commented type
    SeasonYear = scrapy.Field()
    Season = scrapy.Field()
    fashionType = scrapy.Field()
    Design_Styling = scrapy.Field()
    productType = scrapy.Field()
    productGroups = scrapy.Field()
    modelImage = scrapy.Field()