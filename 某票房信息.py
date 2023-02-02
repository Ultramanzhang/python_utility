import json

import requests, binascii
from Crypto.Cipher import DES
print('''
power by zhegu,本代码仅供研究网页加密算法学习交流使用，不得将上述内容用于商业或者非法用途，否则，一切后果请用户自负。
''')

url = 'https://www.endata.com.cn/API/GetData.ashx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
year = input('请输入年份>>>')
data = {
    'year': year,
    'MethodName': 'BoxOffice_GetYearInfoData'
}
response = requests.get(url=url, headers=headers, data=data)
data = response.text


# 根据网站的加密算法逆向而来
def zhegu_fn(c_a, c_b, c_c):
    if (0 == c_b):
        return c_a[c_c:]
    zhegu_r = '' + c_a[0:c_b]
    zhegu_r += c_a[c_b + c_c:]
    return zhegu_r
zhegu_a = int(data[len(data) - 1], 16) + 9
zhegu_b = int(data[zhegu_a], 16)
data = zhegu_fn(data, zhegu_a, 1)
zhegu_a = data[zhegu_b:zhegu_b + 8]
data = zhegu_fn(data, zhegu_b, 8)
zhegu_b = zhegu_a.encode('utf8')
zhegu_a = zhegu_a.encode('utf8')
ds = binascii.a2b_hex(data)

des = DES.new(zhegu_b, mode=DES.MODE_ECB)
result = des.decrypt(ds)

# 解析数据
a_j = json.loads(result.decode('utf8')[:-23])
for i in a_j['Data']['Table']:
    print("*" * 30)
    print("电影名称: " + i['MovieName'])
    print("类型: " + i['Genre_Main'])
    print("总票房(亿)：" + str(i['BoxOffice'] / 10000))
    print("平均票价：" + str(i['AvgPrice']))
    print("场均人次：" + str(i['AvgPeoPle']))
    print("国家(地区)：", i['Area'])
    print("上映日期：", i['ReleaseTime'])
    print("*" * 30)
print('''
本代码仅供研究网页加密算法学习交流使用，不得将上述内容用于商业或者非法用途，否则，一切后果请用户自负。
''')
