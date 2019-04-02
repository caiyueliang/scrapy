# -*- coding: utf-8 -*-
import scrapy


class FlagSpider(scrapy.Spider):
    name = 'flag'
    allowed_domains = ['image.baidu.com']
    start_urls = ['http://image.baidu.com/']

    def parse(self, response):
        pass
