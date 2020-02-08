# -*- coding: utf-8 -*-

import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import os

def spider(page):
    url = "https://movie.douban.com/top250?start={}&filter=".format(page * 25)
    text = requests.get(url, headers = headers).content.decode()
    html = etree.HTML(text)
    data_title[page] = html.xpath("//span[@class='title'][1]/text()")
    data_score[page] = html.xpath("//span[@class='rating_num']/text()")
    data_address[page] = html.xpath("//div[@class='hd']/a/@href")
    data_image = html.xpath("//a/img/@src")
    #保存图片与img文件下
    for i in range(25):
        with open("img/{}.png".format(data_title[page][i]),"wb") as f:
            f.write(requests.get(data_image[i]).content)

def save():
    """保存信息为xls文件"""
    with open("data.xls", "w", encoding="utf-8") as f:
        f.write("排行\t名称\t评分\t网址\n")
        for i in range(250):
            f.write("{}\t{}\t{}\t{}\n".format(i+1, data_title[i//25][i%25], data_score[i//25][i%25], data_address[i//25][i%25]))

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
#保存爬取的信息
data_title = [[] for _ in range(10)]
data_score = [[] for _ in range(10)]
data_address = [[] for _ in range(10)]
#目录下没有img文件则创建此文件
if not os.path.exists("img"):
    os.makedirs("img")
#开启10个进程分别爬取10个页面
pool = ThreadPool(10)
print("爬取开始...")
pool.map(spider, range(10))
pool.close()
pool.join()
save()
print("爬取完成...")          


