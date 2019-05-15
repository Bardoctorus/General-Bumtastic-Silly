# -*- coding: utf-8 -*-
import scrapy

# ! taken from this tut https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/


class BigSpiderSpider(scrapy.Spider):
    name = 'big_spider'
    allowed_domains = ['https://www.makeuseof.com/service/buying-guides/']
    start_urls = ['https://www.makeuseof.com/service/buying-guides/']

    def parse(self, response):
        urls = response.css('.article-card-title').extract()
        ims =  response.css('.article-card-image-overlay').extract()
        pass

        for item in zip(urls, ims):
            scrape_dict = {
                'URL' : item[0],
                'Image': item[1]
            }
            yield scrape_dict