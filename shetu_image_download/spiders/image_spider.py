#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from shetu_image_download.items import ShetuImageDownloadItem#导入Item
from configparser import ConfigParser
import json
import time
import os
import pandas as pd
class ImageDownloadSpider(Spider):
    #定义爬虫名称
    name = 'image'
    cfg = ConfigParser()
    r = cfg.read(r'C:\Users\19248\Desktop\汽车之家\shetu_image_download\spiders\Car.txt',encoding='UTF-8')
    print(cfg.sections)
    pageno = cfg.get('TuGuan','pagenum')#需要爬取的页数
    #获取初始Request
    def start_requests(self):
        for i in range(int(self.pageno)):
            time.sleep(3)
            url = f"https://club.autohome.com.cn/frontapi/data/page/club_get_topics_list?page_num={i}&page_size=50&club_bbs_type=c&club_bbs_id=4274&club_order_type=1"
            #生成请求对象
            yield Request(url,callback=self.parse)

    #解析函数-解析详细页，获取图片URL
    def parse(self,response):
        response = json.loads(response.text)['result']['items']
        #去重
        df = pd.read_excel(r'C:\Users\19248\Desktop\汽车之家\途观.xlsx',usecols='D',names = None).values.tolist()
        #创建ShetuImageDownloadItem对象
        for listcar in response:
            item = ShetuImageDownloadItem()
            item["title"] = listcar['title']#标题
            item["author_name"] = listcar['author_name']#作者
            item["publish_time"] = listcar['publish_time']#提交时间
            item["pc_url"] = listcar['pc_url']#详情页URL
            if item["pc_url"] in df:
                print(f'{pc_url}地址已经爬取')
                break
            item["image_urls"] = listcar['imgList'].split(",") #获取所有照片的url地址
            yield item





