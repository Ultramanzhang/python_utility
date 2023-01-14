from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from os.path import exists
from time import localtime
from time import time
from os import getcwd
from json import loads
from json import dumps


class Xiaoyuan(object):

    def __init__(self):
        self.url = 'http://10.10.10.3'
        self.options = webdriver.EdgeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.flag = False
        self.s = Service('msedgedriver.exe')
        # self.driver = webdriver.Chrome(service=self.s,options=self.options)
        self.username = None
        self.password = None
        self.time_tuple = localtime(time())
        self.dic = {}

    def run(self):
        self.driver = webdriver.Edge(service=self.s, options=self.options)
        try:
            self.driver.get(self.url)
        except:
            print('检测到当前网页无法访问，请联系网络管理员检查')
        self.boolen_login()
        # 进行逻辑判断，判断是否登录
        print('正在检测登录状态')
        if self.flag == False:
            print('检测到校园网未登录，正在帮你登录')
            # 关闭浏览器,减少资源占用
            self.login_in()
        else:
            self.driver.close()
            self.login_out()

    # 解析网页数据，并进行账号密码的输入，点击登录按钮
    def login_in(self):
        if exists('账号密码.json'):
            self.red_user()
        else:
            self.write_file()
        sleep(1)
        print("当前账号为：{}密码为：{},如需修改请用记事本打开".format(self.username, self.password) + getcwd() + r"\账号密码.json")
        self.driver.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys(self.username)
        self.driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value='//*[@id="login-account"]').click()
        print('正在检测是否登录成功')
        self.boolen_login()
        if self.flag == False:
            print("登录失败,请自行打开浏览器进行尝试登录")

    # 进行登录判断
    def boolen_login(self):
        # 等待页面加载，实测校园网检测登录需要时间
        sleep(4)
        try:
            self.driver.find_element(by=By.XPATH, value='//*[@id="login-account"]')
        except:
            self.flag = True
            if self.flag == True:
                if self.time_tuple[3] + 4 >= 24:
                    print('检测到您已登录，请勿关闭本程序，下次释放重登时间为明日{}点{}分'.format(self.time_tuple[3] + 4 - 24, self.time_tuple[4]))
                    self.driver.close()
                    self.login_out()
                else:
                    print('检测到您已登录，请勿关闭本程序，下次释放重登时间为{}点{}分'.format(self.time_tuple[3] + 4, self.time_tuple[4]))
                # 关闭浏览器,减少资源占用
                self.driver.close()
                self.login_out()
            else:
                self.flag = False

    # 注销函数
    def login_out(self):
        sleep(4*60*60)
        self.time_tuple = localtime(time())
        print("正在为您释放登录,当前时间为：{}点{}分".format(self.time_tuple[3], self.time_tuple[4]))
        self.driver = webdriver.Edge(service=self.s, options=self.options)
        self.driver.get(url=self.url)
        sleep(1.5)
        # 点击注销按钮
        self.driver.find_element(by=By.XPATH, value='//*[@id="logout"]').click()
        # 点击确认按钮
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[2]/div[3]/button[1]').click()
        self.login_in()

    def red_user(self):
        with open('账号密码.json', 'r', encoding='utf8') as f:
            a = f.read()
            if a == "":
                self.write_file()
            else:
                js = loads(a)
                self.username = js["username"]
                self.password = js["password"]
            f.close()

    def write_file(self):
        print("配置文件有误，或不存在，请按提示操作")
        with open('账号密码.json', 'w', encoding='utf8') as f:
            self.username = input("请输入账号：")
            self.password = input("请输入密码：")
            self.dic.update({"username": self.username, "password": self.password})
            f.write(dumps(self.dic))
            f.close()
            self.login_in()

    def caidan(self):
        print(r'''
                                    ___.                  .__                         
______   ______  _  __ ___________  \_ |__ ___.__. _______|  |__   ____   ____  __ __ 
\____ \ /  _ \ \/ \/ // __ \_  __ \  | __ <   |  | \___   /  |  \_/ __ \ / ___\|  |  \
|  |_> >  <_> )     /\  ___/|  | \/  | \_\ \___  |  /    /|   Y  \  ___// /_/  >  |  /
|   __/ \____/ \/\_/  \___  >__|     |___  / ____| /_____ \___|  /\___  >___  /|____/ 
|__|                      \/             \/\/            \/    \/     \/_____/  


欢迎使用鹧鸪校园网登录程序，当前系统时间为   {}年{}月{}日{}时{}分 ，正在拉起程序进行登录中
                '''.format(self.time_tuple[0], self.time_tuple[1], self.time_tuple[2], self.time_tuple[3],
                           self.time_tuple[4]))


if __name__ == '__main__':
    xiaoyuan = Xiaoyuan()
    xiaoyuan.caidan()
    xiaoyuan.run()
