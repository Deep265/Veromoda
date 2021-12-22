import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider as cw

# failed experiment :-(
class CrawlSpider(cw):
    name = 'crawl'
    start_urls = ['https://www.veromoda.in/']

    le_extractor = LinkExtractor(allow='dresses-jumpsuits-vm')
    ru = Rule(le_extractor,callback='parse_item',follow=False)
    rules = (
        ru,
    )
    def parse_item(self, response):
        yield {
            "link" : response.url
        }
