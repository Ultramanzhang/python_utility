from requests import get
from urllib import parse
from bs4 import BeautifulSoup
from time import localtime
from time import time
from os import system


class DY():
    def __init__(self):
        self.name = None
        self.downUrl = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        self.time_tuple = localtime(time())
        self.urls = []

    # 获取网页并返回一个response
    def get(self, url):
        response = get(url=url, headers=self.headers)
        return response

    # 解析网页title
    def get_title_urls(self, response):
        response.encoding = 'gb2312'
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.select('.co_content8 a')
        i = 1
        for ti in title[0:len(title) - 2]:
            print(str(i) + '. ' + '电影名称：' + ti.text)
            self.urls.append('https://m.ygdy8.com' + ti['href'])
            i = i + 1
        print("--" * 20)

    # 判读用户输入
    def choose(self):
        a = input('>>>请输入您的选择：>>')
        if a.isdigit():
            if int(a) <= len(self.urls):
                url = self.urls[int(a) - 1]
                return url
            else:
                print('输入有误，请重新输入')
                return self.choose()
        else:
            print('请输入数字')
            return self.choose()

    # 加工url
    def url_work(self):
        self.url = 'http://s.ygdy8.com/plus/so.php?typeid=&keyword={}'

        name = input(">>>请输入需要搜索的名称>>")
        self.url = self.url.format(parse.quote(name, encoding='gb2312'))

    # 判断搜索结果
    def bool_url(self, response):
        response.encoding = 'gb2312'
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.select('.co_content8 a')
        if len(title) == 2:
            return 0
        else:
            return 1

    # 退出程序
    def exit(self):
        system('pause')

    # 解析下载地址
    def parse_down(self, response):
        print('--' * 20)
        print('下载链接如下（复制到迅雷）：')
        response.encoding = 'gb2312'
        soup = BeautifulSoup(response.text, 'lxml')
        link = soup.select('.co_content8 ul a')
        self.downUrl = link
        i = 1
        for li in self.downUrl[0:len(self.downUrl) - 2]:
            print(str(i) + "." + li['href'])
            i = i + 1
        print('--' * 20)

    # 写入文件
    def wite(self):
        if input('>>是否保存？(1:保存，0：不保存)>>>') == '1':
            with open('下载链接.txt', 'w', encoding='utf8') as f:
                for li in self.downUrl[0:len(self.downUrl) - 2]:
                    f.write(str(li['href']) + '\n')
                f.write('\n')
                f.write(r'''
-------------------------------------------------------------------------------------------
                                    ___.                  .__                         
______   ______  _  __ ___________  \_ |__ ___.__. _______|  |__   ____   ____  __ __ 
\____ \ /  _ \ \/ \/ // __ \_  __ \  | __ <   |  | \___   /  |  \_/ __ \ / ___\|  |  \
|  |_> >  <_> )     /\  ___/|  | \/  | \_\ \___  |  /    /|   Y  \  ___// /_/  >  |  /
|   __/ \____/ \/\_/  \___  >__|     |___  / ____| /_____ \___|  /\___  >___  /|____/ 
|__|                      \/             \/\/            \/    \/     \/_____/  
------------------------------------------------------------------------------------------
仅用于学习交流使用，请下载后24小时内删除本软件
                ''')
            print('保存成功，请查看 下载链接.txt 文件')
            if input('>>>是否继续使用？(1:继续，0：不继续)>>') == '1':
                self.main1()
            else:
                print('''
--------------------
|     感谢使用       |
--------------------
                            ''')
                self.exit()
        else:
            if input('>>>是否继续使用？(1:继续，0：不继续)>>') == '1':
                dianying = DY()
                try:
                    dianying.main1()
                except:
                    print('''
                --------------------
                |     程序出错了     |
                --------------------
                        ''')
                    dianying.exit()
            else:
                print('''
--------------------
|     感谢使用       |
--------------------
                ''')
                self.exit()

    def caidan(self):
        print(r'''
                                    ___.                  .__                         
______   ______  _  __ ___________  \_ |__ ___.__. _______|  |__   ____   ____  __ __ 
\____ \ /  _ \ \/ \/ // __ \_  __ \  | __ <   |  | \___   /  |  \_/ __ \ / ___\|  |  \
|  |_> >  <_> )     /\  ___/|  | \/  | \_\ \___  |  /    /|   Y  \  ___// /_/  >  |  /
|   __/ \____/ \/\_/  \___  >__|     |___  / ____| /_____ \___|  /\___  >___  /|____/ 
|__|                      \/             \/\/            \/    \/     \/_____/  

欢迎使用鹧鸪影视搜索系统，当前系统时间为   {}年{}月{}日{}时{}分
------------------------------------------------------------------------------------------
仅用于学习交流使用，请下载后24小时内删除本软件
                '''.format(self.time_tuple[0], self.time_tuple[1], self.time_tuple[2], self.time_tuple[3],
                           self.time_tuple[4]))

    def main1(self):
        # 整理url
        self.url_work()
        response = self.get(self.url)
        if self.bool_url(response) == 1:
            self.get_title_urls(response)
            self.parse_down(self.get(url=self.choose()))
            self.wite()
        else:
            print('''
--------------------
|     没有检索到     |
--------------------          
            ''')
            self.main1()


if __name__ == '__main__':
    dianying = DY()
    try:
        dianying.caidan()
        dianying.main1()
    except:
        print('''
--------------------
|     程序出错了     |
--------------------
        ''')
        dianying.exit()
