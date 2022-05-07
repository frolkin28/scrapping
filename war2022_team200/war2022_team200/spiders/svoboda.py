import scrapy
from scrapy.http import Request
from war2022_team200.items import War2022Team200Item


class SvobodaSpider(scrapy.Spider):
    name = 'svoboda'
    allowed_domains = ['svoboda.org']
    start_urls = ['https://www.svoboda.org/z/16871']

    def start_requests(self):
        for link_url in self.start_urls:
            print(link_url)
            request = Request(link_url, cookies={'store_language': 'ru'},
                              callback=self.parse)
            yield request

    def parse(self, response):
        item = War2022Team200Item()
        content = response.xpath('//*[@id="ordinaryItems"]')

        for article_link in content.xpath('/li[1]/div/a'):
            item['article_url'] = (
                article_link
                .xpath('.//@href')
                .extract_first()
            )
            if item['article_url'].startswith("http"):
                continue
            item['article_url'] = "https://svoboda.org"+item['article_url']
            print(item['article_url'])
            yield (item)
