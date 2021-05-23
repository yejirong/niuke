# -*- coding: utf-8 -*-
'''
班级：大数据1801
姓名：叶际荣
学号：201806140014
'''
# 导入库
import scrapy
from niuke.items import NiukeItem
from scrapy.selector import Selector
from scrapy.http import Request
from fake_useragent import UserAgent  # 随机userUserAgent


class JobSpider(scrapy.Spider):
    name = 'job'  # 项目名字，唯一(必要)
    # allowed_domains = ['nowcoder.com']
    start_urls = ['https://www.nowcoder.com/job/center?page=1']  # 爬取的主页
    ua = UserAgent()  # 随机userUserAgent

    def parse(self, response):
        item = NiukeItem()  # 生成一个item对象
        selector = Selector(response)  # 定义选择器
        infos = selector.xpath('.//ul[@class="reco-job-list"]/li')  # 用xpath定位到ul标签下所有li标签
        for info in infos:  # 循环
            job_name = info.xpath('div/div[2]/a/text()').extract()[0]  # 工作名字
            job_are = info.xpath('div/div[3]/div[1]/span[1]/text()').extract()[0]  # 工作地点
            job_salary = info.xpath('div/div[3]/div[1]/span[2]/text()').extract()[0]  # 工作薪资
            company = info.xpath('div/div[2]/div/a/text()').extract()[0]  # 公司名字
            release_time = info.xpath('div/div[3]/div[2]/span[2]/text()').extract()[0]  # 发布时间
            rate = info.xpath('div/div[3]/div[2]/div/span[1]/text()').extract()[0]  # 简历处理率
            average = info.xpath('div/div[3]/div[2]/div/span[2]/text()').extract()[0]  # 简历平均处理时间
            link = info.xpath('div/div[2]/a/@href').extract()[0]  # 爬取a标签里的href用于拼接
            job_link = str('https://www.nowcoder.com' + link)   # 工作链接
            # 赋值对象成员变量
            item['job_name'] = job_name
            item['job_are'] = job_are
            item['job_salary'] = job_salary
            item['company'] = company
            item['release_time'] = release_time
            item['rate'] = rate
            item['average'] = average
            item['job_link'] = job_link

            yield item
        # 爬取第2页到92页
        urls = ['https://www.nowcoder.com/job/center?page={}'.format(str(i)) for i in range(2, 92)]
        for url in urls:
            yield Request(url, callback=self.parse, headers={'User-Agent': self.ua.random})


