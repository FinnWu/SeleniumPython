# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/10/24 17:54'

import pytesseract
from PIL import Image
import time
from ShowapiRequest import ShowapiRequest


r = ShowapiRequest("http://route.showapi.com/184-4","78386","b5dc4da7de6f45138bfa2d4b27154d1da" )

# r = ShowapiRequest("http://route.showapi.com/184-4","my_appId","my_appSecret" )
r.addBodyPara("typeId", "35")

# r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")

r.addFilePara("image", r"G:\study\python3selenium3\2.png") #文件上传时设置

res = r.post()

print(res.text)
# time.sleep(5)
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
# res = {"showapi_res_error":"","showapi_res_id":"5dfc847fc3544d519000f1bb7e9ba0e2","showapi_res_code":0,"showapi_res_body":{"Id":"6f2b7df2-5390-4929-ae69-d5400be278da","Result":"W2FQX","ret_code":0}}
# print(res['showapi_res_body']['Result'])
# image = Image.open("3.png")
# # pytesseract.image_to_string(image)
# text = pytesseract.image_to_string(image,lang='chi_sim')
# print(text)