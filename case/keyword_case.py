# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/12/4 10:54'
import sys
sys.path.append('G:/study/python3selenium3')
from util.excel_util import ExcelUtil
from keywords.actionMethod import ActionMethod


class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()

        handle_excel = ExcelUtil('G:/study/python3selenium3/config/keyword.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_value(i,3)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handle_value = handle_excel.get_col_value(i, 6)
                    except_result_method = handle_excel.get_col_value(i, 7)
                    except_result = handle_excel.get_col_value(i, 8)
                    # 可能为 ''而不是None
                    # if send_value:
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                print('excepot_value:',except_value[1],';i:',i)
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':

                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                print('excepot_value:', except_value[1], ';i:', i)
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print('没有else')
                    else:
                        print('预期结果为空')
    # 获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value='',handle_value=''):

        method_value = getattr(self.action_method, method)
        if send_value:
            if handle_value:
                result = method_value(send_value,handle_value)
            else:
                result = method_value(send_value)
        # elif send_value == '' and handle_value != '':
        elif handle_value:

            result = method_value(handle_value)
        else:
            result = method_value()
        return result

if __name__ == '__main__':
    keywords = KeywordCase()
    keywords.run_main()