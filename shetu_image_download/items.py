# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class ShetuImageDownloadItem(scrapy.Item):
    title = scrapy.Field() #标题
    author_name = scrapy.Field() #作者
    publish_time = scrapy.Field() #提交时间
    pc_url = scrapy.Field() #帖子URL
    image_urls = scrapy.Field() #图片URL地址

