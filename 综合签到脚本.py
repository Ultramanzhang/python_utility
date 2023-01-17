import time
import requests
import os
from bs4 import BeautifulSoup
def xiaolonghui():
    a = int(time.time() * 1000)
    url = 'https://qualcomm.growthideadata.com/qualcomm-app/api/user/signIn?userId='
    headers = {'sessionkey': '',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 12; 2206122SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4375 MMWEBSDK/20221109 Mobile Safari/537.36 MMWEBID/4835 MicroMessenger/8.0.31.2281(0x28001F37) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
               'userid': '',
               'timestamp': str(a),
               }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        print(response.json()['message'])

    elif response.status_code == 1:
        print('\n【签到】 失败, 可能是:' + response.json()['message'])

    elif response.status_code == 40001:
        print('\n【签到】 失败, 可能是:' + response.json()['message'])

    else:
        print('\n【签到】 失败 ❌ 了呢, 可能是网络被外星人抓走了!\n')

def bugku():
    url = "https://ctf.bugku.com/user/checkin"
    headers = {
        "cookie": ""    
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    msg = soup.select('h3')
    for i in msg:
        print(i.text.replace('\n', '').replace(' ', ''))


if __name__ == '__main__':
    print('''
----------------------
骁龙会:
    ''')
    xiaolonghui()
    print('''
----------------------
bugku:
''')
    bugku()
    print('----------------------')
    os.system('pause')