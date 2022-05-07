import scrapy
from scrapy.http import Request

from war2022_team200.items import War2022Team200Item


ARTICLES_PATH = '//a[contains(@class,"card-full-news")]'


class LentaruSpider(scrapy.Spider):
    name = 'lentaru'
    allowed_domains = ['lenta.ru']
    start_urls = ['https://lenta.ru/rubrics/economics/economy/']

    def start_requests(self):
        for link_url in self.start_urls:
            print(link_url)
            request = Request(
                link_url,
                cookies={'store_language': 'ru'},
                callback=self.parse,
            )
            yield request

    def parse(self, response, **kwargs):
        item = War2022Team200Item()
        article_links = response.xpath(ARTICLES_PATH)

        for link in article_links:
            item['article_url'] = ( 
                "https://lenta.ru" + link.xpath('.//@href').extract_first()
            )
            print(item['article_url'])

            yield (item)
