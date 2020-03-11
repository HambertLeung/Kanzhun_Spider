#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
from utils.utils import get_header
from urllib.parse import urlencode
import re
import os
from Kanzhun_Config import *

os.chdir(FILEPATH)

def get_cookies(): # 解析cookies为字典
    f=open(r'Kanzhun_cookies.txt', 'r')
    cookies={}
    for line in f.read().split(';'):        
        name,value=line.strip().split('=',1)
        cookies[name]=value 
    return cookies


def get_one_page(query, n):
    data = { 
        'query' : query,
        'cityCode' : 0,
        'pageNum' : n,
    }
    url = 'https://www.kanzhun.com/search/interview.json?' + urlencode(data)
    try:
        response = requests.get(url ,headers=get_header(), cookies = get_cookies(), timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('请求网页出错')
        return None


def parse_one_page(html):
    pattern = re.compile('.*?companyName":"(.*?)".*?cityName":"(.*?)".*?content":"(.*?)".*?result":"(.*?)".*?diffcult":"(.*?)".*?fell":"(.*?)"', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
        '公司' : item[0].replace(r'\u', ''),
        '城市' : item[1].replace(r'\u', ''),
        '简评' : item[2].replace(r'\u', ''),
        '结果' : item[3].replace(r'\u', ''),
        '自评' : item[4].replace(r'\u', ''),
        '难度' : item[5].replace(r'\u', '')
        }
        
        
def main(page): 
    html = get_one_page(KEYWORD, page) 
    df = pd.DataFrame(parse_one_page(html))  
    print(df)
    try:        
        df.to_csv(FILENAME, mode='a', header=False, encoding='gbk')
    except: pass


if __name__ == '__main__':    
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    head_df = pd.DataFrame(columns=( '公司', '城市' , '简评', '结果', '自评', '难度'))        
    head_df.to_csv(FILENAME, encoding='gbk')
    for i in range(GROUP_START, GROUP_END):
        main(i)
    print('\n爬取完成！请查看：' + str(FILEPATH) + '\\' + str(FILENAME))
        
        