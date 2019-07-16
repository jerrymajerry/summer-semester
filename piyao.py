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
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
#print(soup.find_all(class_='rec-list'))
day=soup.find_all('div',{"class":"day_date"})
for m in day:
    print(m.get_text())
driver.close()