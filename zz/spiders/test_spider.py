# -*- coding: utf-8 -*-
__author__ = 'zg'
from scrapy.spider import BaseSpider

class TestSpider(BaseSpider):
    name="zuojia"
    allowed_domains=["whpu.edu.cn"]
    start_urls=[
        "http://www.whpu.edu.cn"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
