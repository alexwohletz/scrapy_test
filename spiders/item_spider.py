# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from test_scraper.items import MyItems
from birdseye import eye


class ItemSpiderSpider(CrawlSpider):
    name = 'item_spider'
    start_urls = [
        'http://quotes.toscrape.com/']

    rules = [
        Rule(LinkExtractor(restrict_xpaths="//a[contains(.,'Next')]"), callback='parse_items', follow=True)
    	]

    def parse_items(self, response):
    	print(response.url)
    	
    	#Get the tags
    	tags = response.css("meta.keywords::attr(content)").extract()
    	#Get the links for each about page for iteration below
    	next_links = response.css("div.quote span a::attr(href)").extract()

    	#Always instantiate itemloader inside of the for loop or you'll get duplicates.
    	for result in zip(next_links,tags):
            url = response.urljoin(result[0])
            print(url)
            #print(result[1])
            l = ItemLoader(item=MyItems(),response = response)
            l.item['tags'] = result[1] #add items either way
            yield scrapy.Request(url= url, callback = self.parse_author, meta={'item':l.load_item()})

    def parse_author(self,response):
    	l = ItemLoader(item=response.meta['item'],response = response)
    	#print(response.css("h3.author-title::text").extract())
    	#print(l.item['tags'])
    	l.add_css('author',"h3.author-title::text")
    	l.add_css('birthdate',"span.author-born-date::text")
    	l.add_css('description',"div.author-description::text")

    	print(l.item)
    	yield l.load_item()
