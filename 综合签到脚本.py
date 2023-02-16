import time
import requests, json
import os
import re
from bs4 import BeautifulSoup
from threading import Thread

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
def xiaolonghui():
    a = int(time.time() * 1000)
    url = 'https://qualcomm.growthideadata.com/qualcomm-app/api/user/signIn?userId='
    headers = {'sessionkey': '',
               'User-Agent': useragent,
               'userid': '',
               'timestamp': str(a),
               }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        print("骁龙会：" + response.json()['message'])

    elif response.status_code == 1:
        print("骁龙会：" + '【签到】 失败, 可能是:' + response.json()['message'])

    elif response.status_code == 40001:
        print("骁龙会：" + '【签到】 失败, 可能是:' + response.json()['message'])

    else:
        print("骁龙会：" + '【签到】 失败 ❌ 了呢, 可能是网络被外星人抓走了!')


def bugku():
    url = "https://ctf.bugku.com/user/checkin"
    headers = {
        "cookie": "",
        "user-agent": useragent,

    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    msg = soup.select('h3')
    for i in msg:
        print("BUGku：" + i.text.replace('\n', '').replace(' ', ''))

def ctfhub():
    url = 'https://api.ctfhub.com/User_API/User/checkIn'
    headers={
        "user-agent": useragent,
        "Authorization": "",
    }
    response=requests.post(url=url,headers=headers,data={})
    print('ctfhub'+response.json()['msg'])

def shuyi():
    url = 'https://scrm-prod.shuyi.org.cn//saas-gateway/api/agg-trade/v1/signIn/insertSignInV2?memberId='
    headers={
        'Host': 'scrm-prod.shuyi.org.cn',
        'auth': '',
        "ReleaseVersion":"2023211",
		"hostName":"scrm-prod.shuyi.org.cn",
		"Terminal-Code":"member_wechat_micro",
		"channel":"wechat_micro",
		"referer":"https://servicewechat.com/wxa778c3d895442625/267/page-frame.html",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6500"

    }
    response = requests.get(url=url,headers=headers)
    if(response.json()['resultCode']=='0'):
        print("书亦烧仙草："+"签到成功，获得:"+response.json()['data']['pointRewardNum']+"积分:"+response.json()['data']['days'])
    else:
        print("书亦烧仙草："+response.json()['resultMsg'])

if __name__ == '__main__':
    Thread(target=xiaolonghui).start()#启动多进程
    Thread(target=bugku).start()
    Thread(target=ctfhub).start()
    Thread(target=shuyi).start()

    # 扩展空间，方便以后增加新的签到函数
    time.sleep(1)
    os.system('pause')

