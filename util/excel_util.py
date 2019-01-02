# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/11/22 10:22'

import xlrd
from xlutils.copy import copy
class ExcelUtil:
    def __init__(self,excel_path=None, index=None):
        self.excel_path = excel_path
        if excel_path is None:
            excel_path = "G:/study/python3selenium3/config/keyword.xls"
        if index is None:
            index =0

        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        # 行数
        # self.rows = self.table.nrows

    # 获取excel数据， 按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        # print(self.rows)
        rows = self.get_lines()
        if rows !=None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >=1:
            return rows
        return None

    # 获取单元格的数据
    def get_col_value(self,row,col):
        # print(row)
        if self.get_lines()>row:
            data = self.table.cell(row,col).value
            return data
        return None

    #写入数据
    def write_value(self,row,value):
        # 重新打开excel，免得被替换掉
        self.data = xlrd.open_workbook(self.excel_path)
        read_value  = self.data
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save("G:/study/python3selenium3/config/keyword.xls")


if __name__ == '__main__':
    ex = ExcelUtil()
    ex.get_col_value(6,5)
    # print(ex.write_value(7,"test"))