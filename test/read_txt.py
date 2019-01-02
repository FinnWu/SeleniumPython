# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/11/28 16:26'
import io
class ReadTxt:
    def get_list(self):
        i = 0
        all_list = []
        name_list = []
        addr_list = []
        bh_list = []
        with io.open('20180716.txt','r',encoding='gb18030') as f:
            f.readline()
            for line in f:
                bh = line.replace('"', '').split(',')[0]
                bh_list.append(bh)
                name = line.replace('"', '').split(',')[1]
                name_list.append(name)
                addr = line.replace('"', '').split(',')[7]
                addr_list.append(addr)

            all_list.append(name_list)
            all_list.append(addr_list)
            all_list.append(bh_list)
            # print(all_list)
        return all_list

if __name__ == '__main__':
    biglist = ReadTxt().get_list()
    bhlist = biglist[2]
    print(bhlist)