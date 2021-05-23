# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# from openpyxl import Workbook
#
#
# class NiukePipeline(object):
#
#     wb = Workbook()
#     ws = wb.active
#     # 设置表头
#     ws.append(['工作名字', '工作地点', '工作薪资', '公司名字', '发布时间', '简历处理率', '简历平均处理时间', '工作链接'])
#
#     def process_item(self, item, spider):
#         # 添加数据
#         line = [item['job_name'], item['job_are'], item['job_salary'], item['company'], item['release_time'],
#                 item['rate'], item['average'], item['job_link']]
#         self.ws.append(line)  # 按行添加
#         self.wb.save('job2.xlsx')
#         return item
'''
班级：大数据1801
姓名：叶际荣
学号：201806140014
'''
# 导入库
import pandas as pd


class NiukePipeline(object):

    def process_item(self, item, spider):
        data = pd.DataFrame(dict(item), index=[0])  # item数据转换为字典格式
        # 将数据保存到本地job.csv文件中
        data.to_csv("./job.csv", mode='a+', index=None, header=None)
        return item


