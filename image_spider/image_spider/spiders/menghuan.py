# -*- coding: utf-8 -*-
import os
import scrapy
import json
from logging import getLogger
from scrapy import Request
from urllib.parse import quote
from image_spider.items import ImageSpiderItem


logger = getLogger()


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.baidu.com']
    start_urls = ['http://image.baidu.com/']

    def __init__(self, keyword='国旗', total_page=100, *args, **kwargs):
        super(ImageSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword
        self.total_page = int(total_page)

    def start_requests(self):
        data = {'queryWord': self.keyword, 'word': self.keyword}
        base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='
        for page in range(1, self.total_page + 1):
            data['pn'] = page * 30
            url = base_url + quote(data['queryWord']) + '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=' + \
                quote(data['word']) + '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&pn=' + \
                quote(str(data['pn'])) + '&rn=30&gsm=' + str(hex(data['pn']))
            yield Request(url, self.parse)

    def parse(self, response):
        images = json.loads(response.body)['data']
        for image in images:
            item = ImageSpiderItem()
            try:
                item['url'] = image.get('thumbURL')
                item['keyword'] = self.keyword
                yield item
            except Exception as e:
                print(e)
        pass
        # # 存放老师信息的集合
        # items = []
        #
        # # for each in response.xpath("//div[@class='li_txt']"):
        # for each in response.xpath("//*[@id='imgid']"):
        #     print(each)
        #     # 将我们得到的数据封装到一个 `ItcastItem` 对象
        #     item = ImageSpiderItem()
        #     # extract()方法返回的都是unicode字符串
        #     name = each.xpath("h3/text()").extract()
        #     title = each.xpath("h4/text()").extract()
        #     info = each.xpath("p/text()").extract()
        #
        #     # xpath返回的是包含一个元素的列表
        #     item['name'] = name[0]
        #     item['title'] = title[0]
        #     item['info'] = info[0]
        #
        #     items.append(item)
        #
        # # 直接返回最后数据
        # print('[items]', items)
        # return items
        # pass

