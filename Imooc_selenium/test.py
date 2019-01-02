# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/11/2 15:13'

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
element = driver.find_element_by_id("kw")
element.send_keys('test')  # 这里报错
time.sleep(4)
driver.close()