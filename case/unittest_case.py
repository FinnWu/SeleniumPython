# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/11/13 17:48'

import unittest


class FirstCase01(unittest.TestCase):

    def setUp(self):
        print('这个是case的前置条件')

    def tearDown(self):
        print('这个是case的后置条件 ')

    @unittest.skip('不执行第一条')
    def testfirst01(self):
        print('this is 一 case')

    def testfirst02(self):
        print('this is 二 case')

    def testfirst03(self):
        print('this is 三 case')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests([FirstCase01('testfirst02'),FirstCase01('testfirst01'),FirstCase01('testfirst03')])
    # suite.addTest(FirstCase01('testfirst02'))
    # suite.addTest(FirstCase01('testfirst01'))
    # suite.addTest(FirstCase01('testfirst03'))
    unittest.TextTestRunner().run(suite)
