import scrapy


class War2022Team200Item(scrapy.Item):
    article_url = scrapy.Field()
    article_uuid = scrapy.Field()
    article_id = scrapy.Field()
    article_link = scrapy.Field()
    article_datetime = scrapy.Field()
    article_title = scrapy.Field()
    article_text = scrapy.Field()
