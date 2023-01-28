import os
import time
import requests
from lxml import etree
from urllib.parse import urljoin
import asyncio
import aiohttp
import aiofiles


class Qushu():
    def __init__(self):
        self.dir = ''
        self.base_url = ''

    def get_every_chapter_url(self, base_url):
        response = requests.get(base_url)
        response.encoding = 'gbk'
        # print(response.text)
        tree = etree.HTML(response.text)
        href_list = tree.xpath('//*[@id="list"]/dl/dd/a/@href')
        self.dir = tree.xpath('//*[@id="info"]/h1/text()')[0]
        if os.path.exists(self.dir):
            pass
        else:
            os.mkdir(self.dir)
        return href_list

    # 开始下载文章内容
    async def download_one(self, url):
        while 1:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        page_source = await response.text()

                        tree = etree.HTML(page_source)
                        title = "".join(tree.xpath('///div[@class="bookname"]/h1/text()'))
                        if '正文 ' in title:
                            title = title.replace('正文 ', '')
                        content = "".join(tree.xpath('//*[@id="content"]/text()')).replace('\xa0', '').replace("\n", '')
                        async  with aiofiles.open(f"./{self.dir}/{title}.txt", mode='w', encoding='utf8') as f:
                            await f.write(content.replace("\n", ''))
                        break
            except:
                print("遇到错误，重试中", url)
                time.sleep(0.5)

    # 下载函数
    async def download(self, href_list):
        tasks = []
        for href in href_list:
            href = urljoin('https://www.xiaoqudushu.com/17_17413/', href)
            t = asyncio.create_task(self.download_one(href))
            tasks.append(t)
        await asyncio.wait(tasks)

    # 菜单函数
    def caidan(self,time_tuple):
        print(r'''
                                    ___.                  .__                         
______   ______  _  __ ___________  \_ |__ ___.__. _______|  |__   ____   ____  __ __ 
\____ \ /  _ \ \/ \/ // __ \_  __ \  | __ <   |  | \___   /  |  \_/ __ \ / ___\|  |  \
|  |_> >  <_> )     /\  ___/|  | \/  | \_\ \___  |  /    /|   Y  \  ___// /_/  >  |  /
|   __/ \____/ \/\_/  \___  >__|     |___  / ____| /_____ \___|  /\___  >___  /|____/ 
|__|                      \/             \/\/            \/    \/     \/_____/  

欢迎使用鹧鸪图书下载系统，当前系统时间为   {}年{}月{}日{}时{}分
------------------------------------------------------------------------------------------
仅用于学习交流使用，请下载后24小时内删除本软件，当前采集站点为：https://www.xiaoqudushu.com/，请输入图书
详情页下载例如：https://www.xiaoqudushu.com/17_17413/
                        '''.format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3],
                                   time_tuple[4]))
        self.base_url = input("请输入图书详情页>>>")

    # 主函数
    def main(self):
        # 1. 拿到页面中每一个章节的url
        href_list = self.get_every_chapter_url(self.base_url)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.download(href_list))
        print("下载完毕")


if __name__ == '__main__':
    time_tuple = time.localtime(time.time())
    qushu = Qushu()
    qushu.caidan(time_tuple)
    qushu.main()
