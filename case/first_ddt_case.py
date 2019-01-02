# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/11/20 16:36'

import ddt
import sys
import os
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
from util.excel_util import ExcelUtil

sys.path.append('G:\study\python3selenium3')

ex = ExcelUtil()
data = ex.get_data()


@ddt.ddt
class FirstDdtCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')
        cls.file_name = 'G:/study/python3selenium3/Image/test002.png'

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        # python2处理方法
        # if sys.exc_info()[0]:
            # self.driver.save_screenshot()
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                img_path = os.path.join(os.getcwd() + '/../Image/%s.jpg' % case_name)
                self.driver.save_screenshot(img_path)
        self.driver.close()
    '''
    @ddt.data(
        # ['12', 'mushishi1', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
        # ['@qq.com', 'mushishi1', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
        ['121@qq.com', 'mus2hishi1', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
        # ['12@qq.com', 'mu1', '111111', 'code', 'user_name_error', '字符长度必须大于等于4，一个中文字算2个字符'],
        # ['121@qq.com', 'mushishi2', '11', 'code', 'user_password_error', '最少需要输入 5 个字符'],
        # ['122@qq.com', 'mushishi3', '111111', 'code', 'code_text_error', '验证码错误'],
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email, username, password, self.file_name, assertCode, assertText)
        print(email_error)
        self.assertFalse(email_error, '测试失败')
        # 通过assert 判断是否为error


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + '/../report/first_case1.html')
    with open(file_path, 'wb') as f:
        suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first report1', description=u'这个是第一个测试报告1',
                                               verbosity=2)
        runner.run(suite)