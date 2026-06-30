#https://www.themoviedb.org
#https://www.themoviedb.org/movie/top-rated


import requests
import csv
from lxml import html

"""
需求：爬取https://www.themoviedb.org/movie/top-rated页面的电影信息，并保存到csv文件中
    1. 明确网站https://www.themoviedb.org的robots.txt中的抓取规则
    2. 查看页面的结构，拆解具体的操作步骤，按步骤开发
        a.获取高分电影列表
        b.遍历电影列表，获取每一部电影的详情信息（数据包括：电影名称、年份、上映时间、类型、时长、评分、语言、导演、作者、主演、Slogan、简介），
          并提取电影数据信息
        c. 保存数据到csv文件中

"""

#常量
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"


def main():
    #发送请求，获取页面数据
    response = requests.get(TMDB_TOP_URL,timeout=60)
    docment = html.fromstring(response.text)
    print(docment)

if __name__ == '__main__':
    main()