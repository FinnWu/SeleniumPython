# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/11/20 10:20'
from PIL import Image
from util.rk import RClient
import time


class GetCode:
    def __init__(self,driver):
        self.driver = driver
    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        # print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

    # 获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        rc = RClient('meto001', 'agv10086', '115087', 'ac9b1b069fcc4f03a3108d16d5f67662')
        with open(file_name, 'rb') as f:
            im = f.read()
            key = rc.rk_create(im, 3050)['Result']
            time.sleep(2)
        return key