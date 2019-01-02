# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/12/12 15:24'

import os
i = 0
for root, dirs, files in os.walk('/d-disk/data/source/source/bjz'):
    for file in files:
        # if i % 1000 == 0:
        print(i)
        i += 1
        # print(file)
        # 通过‘_’判断已处理的文件，用于该场景，其他场景酌情选择

    # print(list1)