#https://www.themoviedb.org
#https://www.themoviedb.org/movie/top-rated


import requests
import csv
import time
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
TMDB_TOP_PAGE = "https://www.themoviedb.org/discover/movie/items"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

def get_safe_text(result):
    """安全提取xpath结果中的文本"""
    if result and len(result) > 0:
        return result[0].strip() if isinstance(result[0], str) else result[0].text_content().strip()
    return ''


def get_movie_info(url):
    time.sleep(1)
    response = requests.get(url, headers=HEADERS, timeout=60)
    response.raise_for_status()
    docment_info = html.fromstring(response.text)

    movie_name = docment_info.xpath("//*[@id='original_header']//h2/a/text()")
    movie_years = docment_info.xpath("//*[@id='original_header']//h2/span/text()")
    movie_data = docment_info.xpath("//*[@id='original_header']//div[contains(@class,'release_date')]//span[@class='release']/text()")
    movie_type = docment_info.xpath("//*[@id='original_header']//span[contains(@class,'genres')]//a/text()")
    movie_duration = docment_info.xpath("//*[@id='original_header']//span[contains(@class,'runtime')]//text()")
    movie_language = docment_info.xpath("//section[contains(@id,'facts')]//p[contains(text(),'语言') or contains(text(),'Original Language')]/following-sibling::p/text() | //section[@id='facts']//li[contains(@class,'language')]//text()")
    movie_director = docment_info.xpath("//section[@id='cast']/ol/li[1]//p[@class='character']/preceding-sibling::p[@class='name']/a/text() | //ol[@class='people']/li[1]//a/text()")
    movie_slogan = docment_info.xpath("//p[contains(@class,'tagline')]/text()")
    movie_description = docment_info.xpath("//div[contains(@class,'overview')]//p/text() | //section[@id='overview']//p/text()")

    movie_info = {
        "电影名称": get_safe_text(movie_name),
        "年份": get_safe_text(movie_years),
        "上映时间": get_safe_text(movie_data),
        "类型": ",".join([t.strip() for t in movie_type]) if movie_type else '',
        "时长": get_safe_text(movie_duration),
        "语言": get_safe_text(movie_language),
        "导演": get_safe_text(movie_director),
        "Slogan": get_safe_text(movie_slogan),
        "简介": get_safe_text(movie_description)
    }
    print(f"已获取: {movie_info['电影名称']}")
    return movie_info


#保存数据为csv文件
def save_all_moveies(all_movies):
    with open("./csv_data/movies.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名称", "年份", "上映时间", "类型", "时长", "语言", "导演", "Slogan", "简介"])
        writer.writeheader()
        writer.writerows(all_movies)

def main():
    all_movies = []
    session = requests.Session()
    session.headers.update(HEADERS)

    for page_num in range(1, 6):
        print(f"正在获取第 {page_num} 页电影列表...")
        time.sleep(1)

        if page_num == 1:
            response = session.get(TMDB_TOP_URL, timeout=60)
        else:
            payload = f"page={page_num}&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&include_adult=false&with_runtime.gte=0&with_runtime.lte=400"
            response = session.post(TMDB_TOP_PAGE, data=payload, timeout=60)

        response.raise_for_status()
        docment = html.fromstring(response.text)

        movie_links = docment.xpath("//a[contains(@href, '/movie/')]/@href")
        movie_links = list(dict.fromkeys(movie_links))

        print(f"  找到 {len(movie_links)} 部电影链接")

        for link in movie_links:
            if '/movie/' not in link:
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
