# Xinwen-baSpider



## 一个小巧的为了爬新闻吧美图的爬虫

即插即用版本，使用场景灵活多变，每行都有注释，便于爬虫入门学习者研究。

主要使用了：

* BeautifulSoup库
* Selenium库

#### QuickStart

​	git clone或下载zip解压后在根目录运行：

```python
python xinwenba.py [website url]
```

例如：

```python
python xinwenba.py https://www.xinwenba.net/plus/view-748261-1.html 
```

其中url建议为每一个图集的第一个网页。

爬虫会在download文件下自动创建以图集为名字的文件夹收纳图片。

#### 版本日志

20220407 针对抓取完毕后无法退出网页的问题增加了raise判断以退出网页

20220406 完善了备注

#### 备注

本爬虫为本人练手作品，目前仅设置了针对该网站webp文件的爬取。

Enjoy 美女图片beauty~