# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import get_base_url


class GsmarenaSpider(scrapy.Spider):
    name = "gsmarena"
    allowed_domains = ["gsmarena.com"]
    start_urls = ['http://www.gsmarena.com/makers.php3']
    time1 = 0
    time2 = 0

    def parse(self, response):
        baseurl = get_base_url(response)
        trs = response.xpath(".//div[@class='st-text']/table//tr")

        for tr in trs:
            tds = tr.xpath(".//td")
            if self.time1 > 0:
                break
            for td in tds:
                if self.time2 > 0:
                    break
                url = baseurl + td.xpath(".//a/@href").extract_first()
                self.time2 += 1
                yield scrapy.Request(url=url, callback=self.parseBrand)
            self.time1 += 1
        pass

    def parseBrand(self, response):
        print "parseBrand"
        urls = response.xpath(".//div[@class='makers']//li")
        print urls
        for url in urls:
            print "url", url.xpath(".//a/@href").extract_first()

        pass
