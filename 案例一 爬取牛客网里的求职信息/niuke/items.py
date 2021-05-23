# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
'''
班级：大数据1801
姓名：叶际荣
学号：201806140014
'''
# 导入库
import scrapy


class NiukeItem(scrapy.Item):  # 创建爬取内容
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()  # 工作名字
    job_are = scrapy.Field()  # 工作地点
    job_salary = scrapy.Field()  # 工作薪资
    company = scrapy.Field()  # 公司名字
    release_time = scrapy.Field()  # 发布时间
    rate = scrapy.Field()  # 简历处理率
    average = scrapy.Field()  # 简历平均处理时间
    job_link = scrapy.Field()  # 工作链接
