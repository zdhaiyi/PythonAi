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

#获取详细页面数据
def get_movie_info(url):
    response = requests.get(url,timeout=60)
    docment_info = html.fromstring(response.text)
    movie_name = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()") # 电影名称
    movie_years = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()") # 年份
    movie_data = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()") # 上映时间
    movie_type = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()") # 类型
    movie_duration = docment_info.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent") # 时长
    movie_language = docment_info.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()") # 语言
    movie_director = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()") # 导演
    movie_writer = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")    # 作者
    movie_cast = docment_info.xpath("//*[@id='cast_scroller']/ol/li[1]/p[1]/a/text()")  # 主演
    movie_slogan = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[@class='tagline']/text()")   # Slogan
    movie_description = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()") # 简介

    #保存为字典类型并返回
    movie_info = {
        "电影名称": movie_name[0].strip() if movie_name else '',
        "年份": movie_years[0].strip() if movie_name else '',
        "上映时间": movie_data[0].strip() if movie_name else '',
        "类型": ",".join(movie_type) if movie_type else '',
        "时长": movie_duration[0].strip() if movie_duration else '',
        "语言": movie_language[0].strip() if movie_language else '',
        "导演": movie_director[0].strip() if movie_director else '',
        "作者": movie_writer[0].strip() if movie_writer else '',
        "主演": movie_cast[0].strip() if movie_cast else '',
        "Slogan": movie_slogan[0].strip() if movie_slogan else '',
        "简介": movie_description[0].strip() if movie_description else ''
    }
    print(movie_info)
    return movie_info




#保存数据为csv文件
def save_all_moveies(all_movies):
    with open("./csv_data/movies.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名称", "年份", "上映时间", "类型", "时长", "语言", "导演", "作者", "主演", "Slogan", "简介"])
        writer.writeheader()
        writer.writerows(all_movies)

def main():
    #发送请求，获取页面数据
    response = requests.get(TMDB_TOP_URL,timeout=60)
    docment = html.fromstring(response.text)
    #解析数据
    movie_list = docment.xpath("/html/body/div[1]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div")
    #遍历电影列表，获取每一部电影的详情信息
    all_movies = []
    for movie in movie_list:
        movie_urls = movie.xpath("./div/div/a/@href")
        if movie_urls:
            movie_info_url = TMDB_BASE_URL + movie_urls[0]
            #发送请求，获取电影详情页面数据，
            movie_info = get_movie_info(movie_info_url)
            all_movies.append(movie_info)
    #保存数据，保存为csv文件
    save_all_moveies(all_movies)
if __name__ == '__main__':
    main()