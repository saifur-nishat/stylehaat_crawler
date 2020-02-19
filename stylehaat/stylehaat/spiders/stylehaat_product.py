# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import StylehaatItem


class StylehaatProductSpider(CrawlSpider):
    name = 'stylehaat_product'
    allowed_domains = ['www.stylehaat.com']
    start_urls = ['http://www.stylehaat.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//ul[contains(@class,"st_mega_menu")]/li/a[contains(@class,"is_parent")]'), follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[contains(@class,"product-name")]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//li[@id="pagination_next_bottom"]/a[@href]'), follow=True),
    )

    def parse_item(self, response):
        item = ItemLoader(item=StylehaatItem(), response=response)
        item.add_xpath('breadcrumb', '//section[@class="breadcrumb"]/ul/li[position()>1 and contains(@typeof,"v:Breadcrumb")]/a/text()')
        item.add_xpath('product_name', '//section[@class="breadcrumb"]/ul/li[last()]/span/text()')
        item.add_xpath('product_old_price', '//span[@id="old_price_display"]/text()')
        item.add_xpath('product_new_price', '//span[@id="our_price_display"]/text()')
        img_link = response.xpath('//div[@id="view_full_size"]//div[@class="item"]//img/@src').extract()
        item.add_value('image_urls', img_link)
        item.add_xpath('more_info', '//div[@id="more_info_block"]//div[@class="pa_content"]//p/text()')
        yield item.load_item()
