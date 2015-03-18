# -*- coding: utf-8 -*-
__author__ = 'zg'
from scrapy.spider import BaseSpider

class TestSpider(BaseSpider):
    name="zuojia"
    allowed_domains=["whpu.edu.cn"]
    start_urls=[
        "http://www.whpu.edu.cn"
        "http://www.whpu.edu.cn/showmore.aspx?type=%D0%C5%CF%A2&Ctype=%D0%A3%D4%B0%B9%AB%B8%E6"
        "http://www.whpu.edu.cn/showmore.aspx?type=%D0%C5%CF%A2&Ctype=%D1%A7%D0%A3%D0%C2%CE%C5"
        "http://www.whpu.edu.cn/showmore.aspx?type=%D0%C5%CF%A2&Ctype=%D1%A7%CA%F5%B6%AF%CC%AC"
    ]
    def parse(self, response):
        filename = "a.txt"
        open(filename, 'wb').write(response.body)
