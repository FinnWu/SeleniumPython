# _*_ coding:utf-8 _*_

__author__ = 'meto'
__date__ = '2018/11/20 15:18'

import unittest

import ddt


@ddt.ddt
class DataTest(unittest.TestCase):

    def setUp(self):
        pass
        # print('这是setup')

    def tearDown(self):
        pass
        # print('这是teardown')

    @ddt.data(
        (1, 2),
        [3, 4],
        [5, 6]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a + b)


if __name__ == '__main__':
    unittest.main()
