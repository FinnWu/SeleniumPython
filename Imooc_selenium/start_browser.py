# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/10/12 11:28'

from selenium import webdriver
import time
from PIL import Image
import random
from ShowapiRequest import ShowapiRequest
import requests
from hashlib import md5
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

#验证码类
class RClient(object):

    def __init__(self, username, password, soft_id, soft_key):
        self.username = username
        self.password = md5(password.encode('latin1')).hexdigest()
        self.soft_id = soft_id
        self.soft_key = soft_key
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': ('a.jpg', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        return r.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()


# rc = RClient('meto001', 'agv10086', '115087', 'ac9b1b069fcc4f03a3108d16d5f67662')
# im = open('2.png', 'rb').read()
# print(rc.rk_create(im, 3040)['Result'])





driver = webdriver.Chrome()
# driver = webdriver.Edge()
# driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
time.sleep(5)

#查看title中是否包含注册
print(EC.title_contains("注册")(driver))

# element = driver.find_element_by_class_name("controls")
#判断传入的元素是否可见
# EC.visibility_of_element_located(element)
locator = (By.CLASS_NAME,"controls")
# EC.visibility_of_element_located(element)
# print(WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator)))
email_element = driver.find_element_by_id("register_email")

#下面代码为保存验证码图片
driver.save_screenshot(r"G:\study\python3selenium3\1.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
print('left：',left)
top = code_element.location['y']
print('top:',top)
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open(r"G:\study\python3selenium3\1.png")
img = im.crop((left,top,right,height))
img.save(r"G:\study\python3selenium3\2.png")

rc = RClient('meto001', 'agv10086', '115087', 'ac9b1b069fcc4f03a3108d16d5f67662')
im = open('2.png', 'rb').read()
key = rc.rk_create(im, 3050)['Result']
print(key)

# time.sleep(5)

time.sleep(2)
driver.find_element_by_id('captcha_code').send_keys(key)


# for i in range(5):
#     user_email = ''.join(random.sample('1234567890abcdefg',5))+'@163.com'
#     print(user_email)


print(email_element.get_attribute("placeholder"))
# email_element.send_keys("mushishi_01@163.com")
# print(email_element.get_attribute("value"))


email_element = driver.find_element_by_id("register_email")
email_element.send_keys('7562469725@qq.com')
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# print(driver.find_elements_by_class_name("controls"))
user_element = user_name_element_node.find_element_by_class_name("form-control").send_keys("hel1lowang")
driver.find_element_by_name("password").send_keys("11121111")
# driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys("2vzx")

time.sleep(10)
driver.close()