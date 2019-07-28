# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestscrapytemplateItem(scrapy.Item):
    # define the fields for your item here like:
    appName = scrapy.Field()
    appType = scrapy.Field()
    appLink = scrapy.Field()
    appDownloadCount = scrapy.Field()
    appRank = scrapy.Field()

