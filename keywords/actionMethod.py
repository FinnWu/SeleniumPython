# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/12/3 17:56'
from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod:

    def __init__(self):
        pass

    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()

    # 输入地址
    def get_url(self,url):
        self.driver.get(url)

    # 定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_element(self,key):
        self.get_element(key).click()

    # 等待
    def sleep_time(self,*args):
        time.sleep(3)

    # 关闭浏览器
    def close_browser(self, *args):
        print('我要关闭了！')
        self.driver.close()

    # 获取title
    def get_title(self):
        print('get_title')
        return self.driver.title

    # 获取element