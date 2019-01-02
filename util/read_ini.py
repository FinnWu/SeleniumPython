# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/10/30 18:14'

import configparser
import os


class ReadIni(object):

    def __init__(self, file_name=None, node=None):

        if file_name is None:
            file_name = "G:/study/python3selenium3/config/LocalElement.ini"
        if node is None:
            self.node = 'RegisterElement'

        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    #获取value值
    def get_value(self,key):
        data = self.cf.get(self.node, key)
        return data



if __name__ == '__main__':
    read = ReadIni()
    print(read.get_value('password'))
# #获取绝对路径
# path = os.path.dirname(__file__)
# print(path)
# with open('%s/config/LocalElement.ini'%path,'r') as f:
#     lines = f.readlines()
#     print(lines)
# cf = configparser.ConfigParser()
# cf.read("G:/study/python3selenium3/config/LocalElement.ini")
# print(cf.get('RegisterElement','user_email'))
# cf.get('RegisterElement','user_name')
# cf.get('RegisterElement','password')
# cf.get('RegisterElement','code_image')
