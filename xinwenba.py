import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import time
import sys
import os
import string

driver = webdriver.Chrome()


index = 1
index2 = 1


def getImage(target):

    # driver.get('https://www.xinwenba.net/plus/view-756374-1.html')
    driver.get(target)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #找到<title标签并拉取字符串
    title = str(soup.find_all("title"))

    #标题太长也创建不了文件夹，于是缩减一点标题长度，会一直裁剪到find到的坐标前一位
    title = title[8:title.find("_美女")]
    print("the web title is %s"%title)
    #将工作目录转入download
    os.chdir("download")
    #创建放置爬来的图片的目录
    os.mkdir(title)
    #将两个计数变量调成全局变量（不受local frame影响）
    global index, index2
    while True:
        html = BeautifulSoup(driver.page_source, 'html.parser')
        #使用正则表达式的残骸
        img_regexp = re.compile(r'src="(.+?\.webp)" pic_ext')
        #不清楚哪次尝试的残骸
        # html = html.decode('utf-8')
        #找到<img 标签，寻找其中的src=项，使用正则匹配带有webp的项目
        links = html.find_all("img", src=re.compile('webp'))
        # links = re.findall(img_regexp,html)
        time.sleep(2)#等加载
        for link in links:
            # 此处使用’wb‘操作数覆盖写入文件，写入xx.jpg文件
            with open('{}/{}.jpg'.format(title,index), 'wb') as jpg:
                # 此处使用write函数，get(get(webp文件地址))
                jpg.write(requests.get(link.get('src')).content)
                index += 1
                print("正在爬取第%s张图片" % index)

        time.sleep(1)
        index2 += 1
        try:
            driver.get(target[:target.find(".html")-1] +
                       str(index2)+'.html')
                       #针对新闻吧的网页结果进行换页操作
        except:
            print("一共抓取%d张图片，快来看看吧！" % index)
        # 模拟点击，注意要下拉！！！
        # 拖动视窗下拉操作
        # driver.execute_script("window.scrollTo(0,4000);")
        # 寻找下一页按钮并点击
        # driver.find_element(by=By.LINK_TEXT,value=u'下一页')
        # 此处用不上翻页按钮了，分析网站命名规律后直接用新的url更新翻页
        # 以下一行是旧的find element函数形式
        # driver.find_element_by_link_text(u'下一页').click()


def main():
    link_texts = [u'下一页']#使用多变量翻页的残骸
    #接收命令行参数
    target = sys.argv
    print("Input argument is %s" % target)
    #传递网址
    getImage(target[1])


main()
