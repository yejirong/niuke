'''
班级：大数据1801
姓名：叶际荣
学号：201806140014
'''
# 导入库
import requests


# 判断ip是否可用
def is_ip_valid(proxies):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    try:
        r = requests.get('http://www.163.com', headers=headers, proxies=proxies, timeout=5)
    except:
        print('NO')
    else:
        print('YES')

proxies = {"http": "http://61.135.217.7:80"}
# proxies = {"http": "http://116.196.85.150:3128"}
# proxies = {"http": "http://39.137.69.9:80"}
# proxies = {"http": "http://112.253.11.113:8000"}
# proxies = {"http": "http://114.105.183.142:4216"}
# proxies = {"http": "http://114.105.183.142:4216"}

# proxies = {"http": "http://	114.101.252.142:3000"}
is_ip_valid(proxies)