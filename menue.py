
import os

def main():
    if(not os.path.exists("download")):
        try:
            os.mkdir("download")
        except:
            raise("创建目录失败！请手动创建download目录！")

    args = list(input("请输入待爬取新闻吧网址（多个网址之间以空格隔开）：").split())
    print(args)
    for argv in args:
        os.system('python xinwenbaV2.py '+argv)

main()