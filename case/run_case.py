# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/11/16 11:08'
import os
import unittest

class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd())
        print(case_path)
        suite = unittest.defaultTestLoader.discover(case_path,'unittest*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
    # RunCase().test_case01()