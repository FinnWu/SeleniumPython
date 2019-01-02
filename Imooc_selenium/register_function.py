# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/10/30 18:04'

import sys

sys.path.append('G:/study/python3selenium3')
from selenium import webdriver
import time
import random
from PIL import Image
from util.rk import RClient
from Imooc_selenium.find_element import FindElement


class RegisterFunction(object):

    def __init__(self, url,i):
        self.driver = self.get_driver(url,i)

    # 获取driver并打开url
    def get_driver(self, url,i):
        if i == 0:
            driver = webdriver.Chrome()
        elif i == 1:
            driver = webdriver.Firefox()
        else:
            # driver = webdriver.Edge()
            pass
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
        return user_info

    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        # print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    # 获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        rc = RClient('meto001', 'agv10086', '115087', 'ac9b1b069fcc4f03a3108d16d5f67662')
        im = open(file_name, 'rb').read()
        key = rc.rk_create(im, 3050)['Result']
        return key

    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@163.com"
        file_name = "G:/study/python3selenium3/Image/test.png"
        # code_text = self.code_online(file_name)
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('password', '111111')
        # print(code_text)
        # self.send_user_info('code_text', code_text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('code_text_error')

        if code_error is None:
            print('注册成功')
        else:
            self.driver.save_screenshot('G:/study/python3selenium3/Image/code_error.png')
        time.sleep(10)
        self.driver.close()


if __name__ == '__main__':
    for i in range(3):
        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.main()
