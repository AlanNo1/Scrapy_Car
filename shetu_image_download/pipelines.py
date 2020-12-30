# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import numpy as np 
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline#导入图片管道类
from scrapy import Request
#Excel处理管道
class ShetuExcelPipeline(object):
    def open_spider(self,spider):
        self.df_list = []

    def process_item(self, item, spider):
        self.df_list.append(dict(item))
        return item

    def close_spider(self,spider):
        df_new = pd.concat([pd.DataFrame(self.df_list),pd.read_excel(r'C:\Users\19248\Desktop\汽车之家\途观.xlsx')],ignore_index=True).\
        drop_duplicates(subset=['pc_url'],keep='last',inplace=False).to_excel(r'C:\Users\19248\Desktop\汽车之家\途观.xlsx',index=False)

#图片管道，继承于ImagesPipeline
class SaveImagePipeline(ImagesPipeline):
    #构造图像下载的请求，url从item["image_urls"]中获取
    def get_media_requests(self, item, info):
        #将图片类型作为参数传递出去（用于设置存储图片存储路径）
        return [Request(x,meta={"title":item["title"]}) for x in item.get(self.images_urls_field, [])]

    #设置图片存储路径及名称
    def file_path(self, request, response=None, info=None):
        #从Request中meta中获取图片类型
        title = request.meta["title"]
        #图片名称
        image_name = request.url.split("/")[-1]
        #图片存储形式：图片类型/图片名称
        return "%s/%s"%(title,image_name)

