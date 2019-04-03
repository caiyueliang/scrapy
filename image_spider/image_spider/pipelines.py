# -*- coding: utf-8 -*-
import os
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class FlagSpiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
class FlagSpiderPipeline(ImagesPipeline):
    keyword = None

    # 返回保存的文件名
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        if self.keyword is not None:
            file_name = os.path.join(self.keyword, file_name)
        return file_name

    # 单个Item完成下载时的处理方法
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    # 发起图片下载的请求
    def get_media_requests(self, item, info):
        if item['url'] is not None:
            self.keyword = item['keyword']
            yield Request(item['url'])              # 加入调度队列，等待被调度，执行下载
