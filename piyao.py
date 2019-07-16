#/usr/local/bin/python3 
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
driver = webdriver.Chrome()
driver.get("http://piyao.sina.cn/")
time.sleep(3)
#控制滚动条到页面底部
for i in range(26):#range（10）爬到了6-24，增大数值为30，爬到3-31，26刚好到4-16
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)#解决了一个下午，原来是因为需要这个等待时间，不然网页没法加载
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
#print(soup.find_all(class_='rec-list'))
day=soup.find_all('div',{"class":"day_date"})
like=soup.find_all('div',{"class":"like_text"})
title=soup.find_all('div',{"class":"left_title"})
for m in like:
    x=m.get_text()
    print(x)
driver.close()