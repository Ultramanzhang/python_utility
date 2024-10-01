'''
目标网址：https://movie.douban.com/top250?format=text
请求：requests 方式发送请求
    解析：re 方式解析
数据字段：电影标题、导演、编剧、主演、类型、制片国家/地区、上映时间、别名、评分、评价人数,描述,宣传图片
'<em class="">(\d+)</em>.*?<span class="title">(.*?)</span>.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>'
'''
import requests
import re


class DoubanTop250(object):
    # 定义初始化变量，防止代码冗余
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?format=text'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        }
        # 标题
        self.titles = []
        self.directors = []
        self.actors = []
        self.genres = []
        self.countries = []
        self.years = []
        self.english_names = []
        self.ratings = []
        self.votes = []
        self.quotes = []
        self.images = []
        self.result = []

    # 请求函数，用于向目标网站发起请求
    def request(self, url):
        response = requests.get(url, headers=self.headers)
        return response

    # 解析每个连接函数
    def parse_link(self, response):
        # 电影名
        titles = re.findall(r'<span class="title">(.*?)</span>', response.text)
        # 过滤掉杂项
        self.titles = [title for title in titles if r'&nbsp;/&nbsp;' not in title]
        # 导演
        self.directors = re.findall(r'导演: (.*?)&nbsp;&nbsp;', response.text)
        # 主演
        self.actors = re.findall(r'主演: (.*?)<br>', response.text)
        # 类型
        self.genres = re.findall(r'\d{4}&nbsp;/&nbsp;.*?&nbsp;/&nbsp;(.*?)\n', response.text)
        # 制片国家/地区
        self.countries = re.findall(r'.\d{4}&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;.*?\n', response.text)
        # 上映时间
        years = re.findall(r'(.*?)&nbsp;/&nbsp;.*?&nbsp;/&nbsp;.*?\n', response.text)
        self.years = [year.strip() for year in years]
        # 外文名
        self.english_names = re.findall(r'<span class="title">&nbsp;/&nbsp;(.*?)</span>', response.text)
        # 评分
        self.ratings = re.findall(r'property="v:average">(.*?)</span>', response.text)
        # 评价人数
        self.votes = re.findall(r'<span>(.*?)人评价</span>', response.text)
        # 描述
        self.quotes = re.findall(r'<span class="inq">(.*?)</span>', response.text)
        # 宣传图片
        self.images = re.findall(r'src="(.*?)" class="">', response.text)

    # 将以上列表按相同的索引进行压缩
    def merge(self):
        '''
        # 第二种合并方式 不带电影标题这种东西
        for i in zip(self.titles, self.directors, self.actors, self.genres,self.countries, self.years,self.english_names,self.ratings, self.votes,self.quotes, self.images):
            self.result.append(list(i))
        '''
        # 合并信息
        for title, director, actor, genre, country, year, english_name, rating, vote, quote, image in zip(self.titles,
                                                                                                          self.directors,
                                                                                                          self.actors,
                                                                                                          self.genres,
                                                                                                          self.countries,
                                                                                                          self.years,
                                                                                                          self.english_names,
                                                                                                          self.ratings,
                                                                                                          self.votes,
                                                                                                          self.quotes,
                                                                                                          self.images):
            movie_info = {
                "电影标题": title,
                "导演": director,
                "主演": actor,
                "类型": genre,
                "制片国家/地区": country,
                "上映时间": year,
                "外文名": english_name,
                "评分": rating,
                "评价人数": vote,
                "描述": quote,
                "宣传图片": image
            }
            self.result.append(movie_info)

   # 定义入口函数，方便组织内部函数运行
    def main(self):
       self.parse_link(self.request(self.url))
       self.merge()
       for i in self.result:
           print(i)


if __name__ == '__main__':
   douban = DoubanTop250()
   douban.main()
