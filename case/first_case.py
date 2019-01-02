# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/11/5 16:55'
import sys

sys.path.append('G:\study\python3selenium3')
import os
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import unittest
import time
import HTMLTestRunner


class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        print('所有case执行之前的前置')
        cls.file_name = 'G:/study/python3selenium3/Image/test001.png'

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')
        cls.log.close_handle()

    def setUp(self):
        print('driver前面')
        self.driver = webdriver.Chrome(
            'C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe ')
        print('调试')
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info("this is chrome")

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

    def test_login_email_error(self):
        print('开始email的case测试')
        # email_error = self.login.login_email_error('34@qq.com', 'user111', '111111', self.file_name)
        email_error = self.login.login_email_error('34@qq.com', 'user111', '111111', '1111')
        print(email_error)

        self.assertFalse(email_error, 'case执行了')
        # 通过assert 判断是否为error

    def test_login_username_error(self):
        print('开始username的case测试')
        username_error = self.login.login_name_error('111@qq.com', 'us', '111111', '1111')
        self.assertFalse(username_error)

    def test_login_code_error(self):
        print('开始code的case测试')
        code_error = self.login.login_code_error('111@qq.com', 'user001', '111111', '1111')
        self.assertFalse(code_error)

    def test_login_password_error(self):
        print('开始password的case测试')
        password_error = self.login.login_password_error('111@qq.com', 'user002', '1', '1111')
        self.assertFalse(password_error)

    def test_login_success(self):
        self.login.user_base('111112@qq.com', 'user0121', '111111', '1111')
        success = self.login.register_success()
        self.assertFalse(success)


#
# def main():
#     first = FirstCase()
#     first.test_login_email_error()
#     first.test_login_password_error()
#     first.test_login_username_error()
#     first.test_login_code_error()
#     first.test_login_success()


if __name__ == '__main__':
    # unittest.main()
    file_path = os.path.join(os.getcwd() + '/../report/first_case.html')
    with open(file_path, 'wb') as f:
        suite = unittest.TestSuite()
        # suite.addTests([FirstCase('test_login_email_error'), FirstCase('test_login_username_error'),
        #                 FirstCase('test_login_password_error'), FirstCase('test_login_code_error'),
        #                 FirstCase('test_login_success')])
        suite.addTests([FirstCase('test_login_email_error')])
        # unittest.TextTestRunner().run(suite)
        # 生成测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first report', description=u'这个是第一个测试报告',
                                               verbosity=2)
        runner.run(suite)
