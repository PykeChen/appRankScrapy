# -*- coding: utf-8 -*-
import scrapy
import urllib.response
from TestScrapyTemplate.items import TestscrapytemplateItem
import urllib.request
import re


class GenspidertestSpider(scrapy.Spider):
    name = 'GenSpiderTest'
    allowed_domains = ['qq.com']
    start_urls = ['https://sj.qq.com/myapp/index.htm']

    # def start_rquests()
    def parse(self, response):
        nodesAll = response.xpath(
            '//*[@id = "J_RankTabBody"]/li[2]/ul/child::*').extract()
        rankNum = len(nodesAll)
        for i in range(rankNum):
            appName = response.xpath(
                '//*[@id="J_RankTabBody"]/li[2]/ul/li[' + str(i+1) + ']/div[1]/a/text()').extract()[0]
            appLink = response.xpath(
                '//*[@id="J_RankTabBody"]/li[2]/ul/li[' + str(i+1) + ']/a/@href').extract()[0]
            appRank = i
            appDownloadCount = response.xpath(
                '//*[@id="J_RankTabBody"]/li[2]/ul/li[' + str(i+1) + ']/div[1]/div[1]/span/text()').extract()[0]
            print('parse.....rank = ' + str(appRank) + ', link = ' + str(appLink) + ', downloadCount = ' + str(appDownloadCount) +
                  ' appName = ' + str(appName))
            detailLink = str(appLink).replace('..', 'https://sj.qq.com')
            print(detailLink)
            yield scrapy.Request(detailLink, self.parseAppDetail, meta={'rank': appRank}, flags=[appRank, 'sdfsdf'])

    def parseAppDetail(self, response):
        print('-------11111, meta ' + str(response.meta))
        appRank = response.meta['rank']
        print('-------2222, flag ' + str(appRank))
        appName = response.xpath(
            '//*[@id="J_DetDataContainer"]/div/div[1]/div[2]/div[1]/div[1]/text()').extract()[0]
        appDownload = response.xpath(
            '//*[@id="J_DetDataContainer"]/div/div[1]/div[2]/div[3]/div[1]/text()').extract()[0]
        appType = response.xpath(
            '//*[@id="J_DetCate"]/text()').extract()[0]
        item = TestscrapytemplateItem()
        item['appName'] = appName
        item['appDownloadCount'] = appDownload
        item['appType'] = appType
        item['appLink'] = response.url
        item['appRank'] = appRank
        print('-------222, appName ' + appName +
              ' type = ' + appType + ' download =- ' + appDownload)
        yield item
