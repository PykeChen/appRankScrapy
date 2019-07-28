# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import json


class TestscrapytemplatePipeline(object):

    def __init__(self):
        self.key = 'AppRankItem'
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=1)

    def process_item(self, item, spider):
        dictItem = dict(item)
        json_data = json.dumps(dictItem, ensure_ascii=False)
        print('-------process_item' + json_data)
        self.r.hset(self.key, item['appRank'], json_data)
        return item
