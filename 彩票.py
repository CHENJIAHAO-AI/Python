# -*- coding:utf-8 -*-

'''导入爬虫模块'''
from bs4 import BeautifulSoup
from urllib import request


'''分析'''
url = 'http://8.lemicp.com/trade/jclq/index?playid=10001'
soup = request.urlopen(url).read().decode('utf-8')
load = BeautifulSoup(soup)

'''过滤'''
load_arr = load.select('#vsTable table tbody tr td i')
load_arr1 = load.select('#vsTable table tbody tr td #stopdatetext')
load_arr2 = load.select('#vsTable table tbody tr td em span')
load_arr3 = load.select('#vsTable table tbody tr td .emfr')
load_arr4 = load.select('#vsTable table tbody tr td .emfls')
load_arr5 = load.select('#vsTable table tbody tr td .emfrs span')


load_arr00 = load.select('#vsTable table tbody .trmain td i')
load_arr01 = load.select('#vsTable table tbody .trmain .backred')
load_arr02 = load.select('#vsTable table tbody .trmain #stopdatetext')
load_arr03 = load.select('#vsTable table tbody .trmain td:nth-of-type(4) em')
load_arr04 = load.select('#vsTable table tbody .trmain td:nth-of-type(4) td')
load_arr05 = load.select('#vsTable table tbody .trmain td:nth-of-type(5) em')
load_arr06 = load.select('#vsTable table tbody .trmain td:nth-of-type(6) em span')
load_arr07 = load.select('#vsTable table tbody .trmain td:nth-of-type(6) em')
load_arr08 = load.select('#vsTable table tbody .trmain td:nth-of-type(7) strong')
load_arr09 = load.select('#vsTable table tbody .trmain td:nth-of-type(8) em')
load_arr10 = load.select('#vsTable table tbody .trmain td:nth-of-type(8) span')


'''结果'''
load_arr000 = load.select('.tShared table tbody .trmain td:nth-of-type(10)')


f = open('博彩.txt','w+',encoding='utf-8')
def f1():
    x = 0
    save = ''
    for i in load_arr:
        v1 = i.string.replace('3','星期三-',1)
        v2 = load_arr1[x].string
        v3 = load_arr2[x].string
        v4 = load_arr3[x].string
        v5 = load_arr4[x].string
        v6 = load_arr5[x].string
        vv = v1+v2+v3+v4+v5+v6
        x+=1
        save+=vv
    ff = save
    print(ff,file=f)

f1()

print(load_arr05)