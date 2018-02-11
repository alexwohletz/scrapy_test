# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from test_scraper.items import MyItems

class ItemSpiderSpider(CrawlSpider):
    name = 'item_spider'
    start_urls = [
        'http://quotes.toscrape.com/page/1']

    rules = [
        Rule(LinkExtractor(restrict_css='li.next a'), callback='parse_items', follow=True),
    	Rule(LinkExtractor(restrict_css ="div.quote span a"), callback='parse_author', follow=True)
    	]

    def parse_items(self, response):
    	l = ItemLoader(item=MyItems(),response = response)
    	l.add_css('tags',"meta.keywords::attr(content)")
    	return l.load_item()
    	
    def parse_author(self,response):
    	l = ItemLoader(item=MyItems(),response = response)
    	l.add_css('author',"h3.author-title::text")
    	l.add_css('birthdate',"span.author-born-date::text")
    	l.add_css('description',"div.author-description::text")
    	return l.load_item()
