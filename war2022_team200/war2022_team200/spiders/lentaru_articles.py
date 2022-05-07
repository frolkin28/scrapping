import hashlib
import json

import scrapy
from scrapy.http import Request

from war2022_team200.items import War2022Team200Item


class LentaruArticlesSpider(scrapy.Spider):
    name = 'lentaru_articles'
    allowed_domains = ['lenta.ru']
    start_urls = ['http://lenta.ru/']

    def start_requests(self):
        with open('lentaru.json') as json_file:
            data = json.load(json_file)

        for link_url in data:
            print(link_url["article_url"])
            request = Request(
                link_url['article_url'],
                cookies={'store_language': 'ru'},
                callback=self.parse,
            )
            yield request

    def parse(self, response, **kwargs):
        item = War2022Team200Item()
        item['article_url'] = response.url
        item['article_uuid'] = hashlib.sha256(
            str(response.url).encode('utf-8')
        ).hexdigest()
        item['article_datetime'] = response.xpath(
            '//time[@class = "topic-header__item topic-header__time"]/text()'
        ).extract()
        item['article_title'] = response.xpath(
            '//span[@class = "topic-body__title"]/text()'
        ).extract()
        item['article_text'] = "\n".join(
            response.xpath(
                '//div[@class = "topic-body__content"]/p/text()'
            ).extract()
        )

        yield (item)
