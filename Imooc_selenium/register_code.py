# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/10/30 10:48'
from selenium import webdriver
import time
import random
from hashlib import md5
import requests
from PIL import Image

from util.rk import RClient

driver = webdriver.Chrome()


# 浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(2)


# 获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element


# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
    return user_info


# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    # print(code_element.location)
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    img.save(file_name)


# 获取验证码
def code_online(file_name):
    rc = RClient('meto001', 'agv10086', '115087', 'ac9b1b069fcc4f03a3108d16d5f67662')
    im = open(file_name, 'rb').read()
    key = rc.rk_create(im, 3050)['Result']
    return key


# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info + "@163.com"
    file_name = "G:/study/python3selenium3/test.png"
    driver_init()
    print(type(get_element("register_email")))
    get_element("register_email").send_keys(user_email)
    get_element('register_nickname').send_keys(user_name_info)
    get_element("register_password").send_keys('111111')
    get_code_image(file_name)
    # text = code_online(file_name)
    # get_element('captcha_code').send_keys(text)
    get_element('register-btn').click()
    time.sleep(10)
    driver.close()
driver_init()
driver.find_element_by_id('register_email').send_keys('hello')
time.sleep(1)
driver.find_element_by_id('register_nickname').send_keys('1111111')
print('value:',driver.find_element_by_id('register_email').get_attribute('value'))
print('value:',driver.find_element_by_id('register_email-error').text)
# run_main()
