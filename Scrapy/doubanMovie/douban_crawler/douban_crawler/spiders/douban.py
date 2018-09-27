# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        items = response.css('.item')
        for item in items:
            yield {
                'cover_pic': item.css('.pic a img::attr(src)').extract_first(),
                'link': item.css('.info .hd a::attr(href)').extract_first(),
                'title': item.css('.info .hd a .title::text').extract_first(),
                'rating': item.css('.info .bd .star .rating_num::text').extract_first(),
                'quote': item.css('.info .bd .quote span.inq::text').extract_first()
            }
        next_page = response.css('.paginator .next a::attr(href)').extract_first()
        if next_page:
            next_page_real = response.urljoin(next_page)
            yield scrapy.Request(next_page_real, callback=self.parse, dont_filter=True)

