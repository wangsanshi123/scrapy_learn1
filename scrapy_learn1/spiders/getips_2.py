# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.utils.response import get_base_url

from scrapy_learn1.items import Ips


class Getips2Spider(scrapy.Spider):
    name = "getips_2"
    allowed_domains = ["www.66ip.cn"]
    start_urls = ['http://www.66ip.cn/']
    page = 1
    maxPage = 3

    def parse(self, response):
        # print response.xpath(".//div")
        trs = response.xpath(".//div[@id='main']//table//tr")
        for tr in trs:
            tds = tr.xpath(".//td")
            # print tds.extract_first()
            ip = tds[0].xpath("string()").extract_first().strip()
            port = tds[1].xpath("string()").extract_first().strip()
            if re.match(r"^\d.*?", ip):
                print"ip:", ip
                print"port:", port
                ips = Ips(ip=ip, port=port)
                yield ips
        baseurl = get_base_url(response)
        self.page += self.page
        if self.page <= self.maxPage:
            url = baseurl + "{}.html".format(self.page)
            yield scrapy.Request(url=url)
