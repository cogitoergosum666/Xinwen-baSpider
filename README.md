# Xinwen-baSpider

A tiny and easy-to-learn spider based on Python3

## 一个容易复用、小巧精悍的爬新闻吧美图的爬虫

即插即用版本，使用场景灵活多变，每行都有中文注释，便于爬虫入门学习者研究。

主要使用了：

* BeautifulSoup库
* Selenium库
* chromedriver

### QuickStart快速开始

git clone或下载zip解压后在根目录运行：

```python
python xinwenba.py [website url]
```

例如：

```python
python xinwenba.py https://www.xinwenba.net/plus/view-748261-1.html 
```

其中url建议为每一个图集的第一个网页。

若程序未能在根目录自动创建download请手动创建download文件夹。

爬虫会在download文件下自动创建以图集为名字的文件夹收纳图片。

### 版本日志

20220407 增加了driver.quit()使得爬完后浏览器可以自动关闭

20220407 针对复用之后可能没有download文件夹的情况增加了创建路径与错误判断的代码

20220407 针对抓取完毕后无法退出网页的问题增加了raise判断以退出网页的代码

20220406 完善了备注

### 备注

本爬虫为本人练手作品，目前仅设置了针对该网站webp文件的爬取（例如，“美女明星”栏目中的图片为href=x.jpg格式，不支持）。

Enjoy 美女图片beauty~
