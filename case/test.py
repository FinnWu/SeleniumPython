#!/usr/bin/python3
import requests
import json
import re
import os
list1 = []
def PostcapFrequencyDetail():
    url = "http://192.168.0.154:8000/facecenter/faceCapture/capFrequencyDetail"
    payload = "{\"f\":{\"startTime\":\"2018-12-21 17:49:01\",\"endTime\":\"2018-12-29 17:49:01\",\"childList\":\";\",\"archivesId\"\r\n:\"bc33ab63-2c2f-4550-bddb-f9527da0c9ed\"},\"pageNo\":1,\"pageRows\":500,\"pageFlag\":\"pageFlag\"}"
    headers = {
        'content-type': "application/json;charset=UTF-8",
        'token': "YWRtaW47YWRtaW47MTsxNTQ1MTIyODc1MTI4OzE7MTsxO251bGw7bnVsbDtudWxsO251bGw=",
        'cache-control': "no-cache",
        'postman-token': "13a4d6ec-3462-ab97-5018-89471b341830"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    returnvalue = response.text
    returnvalue = re.sub('\'','\"',returnvalue)
    returnvalue = json.loads(returnvalue)
    return_map = returnvalue['map']['pager']['resultList']
    print(return_map)
    print(len(return_map))
    for i in return_map:
        # print(i['fcapImgUrl'])
        imgeurl = i['fcapImgUrl']
        # print(type(imgeurl))
        # print(imgeurl)
        list1.append(imgeurl)
        # requests.get()
        # print(list.index(imgeurl))
        # j = list.index(i) + 1
        # print(j)
        # PostImge(i['fcapImgUrl'],list.index(imgeurl))
    return list1

def PostImge(ImageUrl,j):
    url = ImageUrl
    querystring = {"t": "1545990896569", "uuid": "admin", "md5": "bdacae204b77a2f4666ca468a30fed3b"}
    headers = {
        'from': "comp",
        'cache-control': "no-cache",
        'postman-token': "f08405f9-e0d1-0639-7a32-9017e2a9a486"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    img = response.content
    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    file_name = 'img/'+j
    with open(file_name, 'wb') as f:
        f.write(img)

img_list = PostcapFrequencyDetail()
print(img_list)
int1 = 0

#创建目录
if os.path.exists('img') == 0:
    os.mkdir('img')

for i in img_list:
    name = i.split('/')[-1]
    print(name)
    PostImge(i,name)
    # int1+=1