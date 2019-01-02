# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/10/31 17:34'

import sys
from util.read_ini import ReadIni


class FindElement(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)

        except Exception as e:
            # self.driver.save_screenshot('G:/study/python3selenium3/Image/%s.jpg'%value)
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
            return None
