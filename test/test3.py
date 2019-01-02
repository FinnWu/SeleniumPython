import time
from selenium import webdriver
# def xh():
#     t = True
#     time.sleep(1)
#     for i in range(1,100):
#         str1 =str(i*926)
#         print(str1)
#         js = "var q=document.getElementById('mainView').scrollTop =%s"%str1
#         driver.execute_script(js)
#         time.sleep(1)
#         # target = driver.find_element_by_id("系统")
#         # target = driver.find_element_by_class_name('for-roast')
#         # driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get('https://ac.qq.com/ComicView/index/id/635294/cid/1')
#     driver.maximize_window()
#     xh()
#

def xh():
    t = True
    time.sleep(1)
    while t:
        driver.execute_script("window.scrollTo(100,500)")
        try:
            driver.find_element('link_text', '没有更多推荐了，返回首页').click()
            time.sleep(1)
            t = False
        except:
            xh()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://blog.csdn.net/sily_z/article/details/80733267")
    xh()