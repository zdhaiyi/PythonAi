#https://www.themoviedb.org
#https://www.themoviedb.org/movie/top-rated


import requests
import csv
from lxml import html
import re

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
TMDB_TOP_PAGE = "https://www.themoviedb.org/discover/movie/items"

#修正年份格式
def get_movie_years(movie_years):
    year = movie_years[0].strip() if movie_years else ''
    return year.replace("(","").replace(")","")

#修正上映时间格式
def get_movie_data(movie_data):
    time = movie_data[0].strip() if movie_data else ''
    match = re.search(r'\d{4}-\d{2}-\d{2}', time)
    return match.group() if match else ''

#修正时长格式
def get_movie_duration(movie_duration):
    duration = movie_duration[0].strip() if movie_duration else ''
    #使用正则方式
    h = re.search(r'(\d+)h', duration)
    m = re.search(r'(\d+)m', duration)
    h_has = int(h.group(1)) if h else 0
    m_has = int(m.group(1)) if m else 0
    return f"{h_has * 60 + m_has}分钟"

def get_movie_info(url):
    response = requests.get(url,timeout=60)
    docment_info = html.fromstring(response.text)
    movie_name = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()") # 电影名称
    movie_years = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()") # 年份
    movie_data = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()") # 上映时间
    movie_type = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()") # 类型
    movie_duration = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()") # 时长
    movie_rating = docment_info.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent") # 评分
    has_class = docment_info.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[@class]")
    movie_language = docment_info.xpath(f"//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[{3 if has_class else 2}]/text()") # 语言
    movie_director = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()") # 导演
    movie_writer = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")    # 作者
    movie_cast = docment_info.xpath("//*[@id='cast_scroller']/ol/li[1]/p[1]/a/text()")  # 主演
    movie_slogan = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[@class='tagline']/text()")   # Slogan
    movie_description = docment_info.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()") # 简介

    #保存为字典类型并返回
    movie_info = {
        "电影名称": movie_name[0].strip() if movie_name else '',
        "年份": get_movie_years(movie_years),
        "上映时间": get_movie_data(movie_data),
        "类型": ",".join(movie_type) if movie_type else '',
        "时长": get_movie_duration(movie_duration),
        "评分": movie_rating[0].strip() if movie_rating else '',
        "语言": movie_language[0].strip() if movie_language else '',
        "导演": movie_director[0].strip() if movie_director else '',
        "作者": movie_writer[0].strip() if movie_writer else '',
        "主演": movie_cast[0].strip() if movie_cast else '',
        "Slogan": movie_slogan[0].strip() if movie_slogan else '',
        "简介": movie_description[0].strip() if movie_description else ''
    }
    return movie_info




#保存数据为csv文件
def save_all_moveies(all_movies):
    with open("./csv_data/movies.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名称", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演", "作者", "主演", "Slogan", "简介"])
        writer.writeheader()
        writer.writerows(all_movies)

def main():
    all_movies = []
    for page_num in range(1,6):
        # 发送请求，获取页面数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL, timeout=60)
        else:
            response = requests.post(TMDB_TOP_PAGE, f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-01-01&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400", timeout=60)
        response.raise_for_status()
        docment = html.fromstring(response.text)
        movie_links = docment.xpath("//a[contains(@href, '/movie/')]/@href")
        movie_links = list(dict.fromkeys(movie_links))

        print(f"找到 {len(movie_links)} 部电影链接")

        for link in movie_links:
            if not re.match(r'/movie/\d+', link):
                continue
            movie_info_url = TMDB_BASE_URL + link
            try:
                movie_info = get_movie_info(movie_info_url)
                if movie_info["电影名称"]:
                    all_movies.append(movie_info)
            except Exception as e:
                print(f"  获取失败: {movie_info_url}, 错误: {e}")
                continue

        print(f"  当前已获取 {len(all_movies)} 部电影数据")

    print(f"\n总共获取 {len(all_movies)} 部电影数据")
    save_all_moveies(all_movies)
    print("数据已保存到 ./csv_data/movies.csv")
if __name__ == '__main__':
    main()