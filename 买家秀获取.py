from time import localtime, time

from requests import get
from os import mkdir, system
from os.path import exists
from concurrent.futures import ThreadPoolExecutor


def get_img(i):
    url = 'https://api.uomg.com/api/rand.img3?format=images'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    r = get(url=url, headers=headers)
    with open(path + "/" + str(i) + '.jpg', "wb") as f:
        f.write(r.content)
def caidan(time_tuple):
    print(r'''
                                    ___.                  .__                         
______   ______  _  __ ___________  \_ |__ ___.__. _______|  |__   ____   ____  __ __ 
\____ \ /  _ \ \/ \/ // __ \_  __ \  | __ <   |  | \___   /  |  \_/ __ \ / ___\|  |  \
|  |_> >  <_> )     /\  ___/|  | \/  | \_\ \___  |  /    /|   Y  \  ___// /_/  >  |  /
|   __/ \____/ \/\_/  \___  >__|     |___  / ____| /_____ \___|  /\___  >___  /|____/ 
|__|                      \/             \/\/            \/    \/     \/_____/  

欢迎使用鹧鸪买家秀获取系统，当前系统时间为   {}年{}月{}日{}时{}分
------------------------------------------------------------------------------------------
仅用于学习交流使用，请下载后24小时内删除本软件
                '''.format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3],
                           time_tuple[4]))

if __name__ == '__main__':
    time_tuple = localtime(time())
    caidan(time_tuple)
    global path
    path = input("请输入存放路径(默认为E:/test)>>")
    if path == "":
        path = r"E:/test"
    if exists(path):
        pass
    else:
        mkdir(path)
    a = int(input("请输入获取图片数量："))
    print("正在保存。。。(时间取决于你的网速和图片数量)")
    with ThreadPoolExecutor(20) as t:
        for i in range(a):
            t.submit(get_img, i)
    print("保存成功，路径为：{}".format(path))

    system('pause')
