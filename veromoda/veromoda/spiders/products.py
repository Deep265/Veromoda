import scrapy
import time
from scrapy.utils.project import get_project_settings
from selenium.webdriver import Chrome,ChromeOptions
from ..items import VeromodaItem

class ProductsSpider(scrapy.Spider):
    name = 'products'

    def start_requests(self):
        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(executable_path=driver_path,options=options)
        # all the main page links
        l = ['https://www.veromoda.in/fashion-vm/fashion-accessories-vm/vm-belt',
             'https://www.veromoda.in/fashion-vm/fashion-accessories-vm/fashion-bags-belts-wallets-vm']
        # all the products links are extracted by selenium on the page
        links = []
        for i in l:
            driver.get(i)

            previous_height = driver.execute_script('return document.body.scrollHeight')
            while True:
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(3)
                new_height = driver.execute_script('return document.body.scrollHeight')
                if new_height == previous_height:
                    break
                previous_height = new_height
            a = '//*[@id="ajax-product-list"]/div/div/div[1]/a'
            link_elements = driver.find_elements_by_xpath(a)
            for i in link_elements:
                href = i.get_attribute('href')
                yield scrapy.Request(href)

        driver.quit()


    def parse(self, response):
        item = VeromodaItem()
        item['title'] = response.xpath('/html/body/div[5]/div[2]/div/div[1]/div[2]/h1/text()').get()
        item['price'] = response.xpath('/html/body/div[5]/div[2]/div/div[1]/div[2]/ul/li[1]/h2/text()').get()
        item['old_price'] = response.xpath('//*[@id="content"]/div[1]/div[2]/ul/li[2]/span/text()').get()
        item['Size'] = response.xpath('//div[@class="radio radio-type-button2 "]/label/text()').extract()
        item['Stock'] = response.xpath('//div[@class="stock_left_pdp"]/text()').get()
        item['product_description_text'] = response.xpath('//div[@class="table-responsive"]/text()').extract()
    #    item['product_table'] = response.xpath('/html/head/script[@type="application/ld+json"]/text()').get()
        size_table = response.xpath('//div[@class="table-responsive"]/div/table[@class="table"]')
        item['size_table'] = size_table.xpath('//tbody/tr/td/text()').extract()
        item['sub_catogery'] = response.xpath('/html/head/meta[@name="keywords"]/@content').extract()
        item['images'] =response.xpath('//*[@id="content"]/div[1]/div[1]/div/div[1]/div/a/@href').extract()
        item['size_table_labels'] = response.css('.pdp-sizeguide__table-head >tr > th::text').extract()
        # a = response.css('body table:nth-child(1)')[2]
        # item['product_detail'] = a.xpath('//td/text()').extract()
        yield item