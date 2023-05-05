import json


# 菜单函数
import random


def caidan():
        print(r'''
                                    ___.                  .__                         
______   ______  _  __ ___________  \_ |__ ___.__. _______|  |__   ____   ____  __ __ 
\____ \ /  _ \ \/ \/ // __ \_  __ \  | __ <   |  | \___   /  |  \_/ __ \ / ___\|  |  \
|  |_> >  <_> )     /\  ___/|  | \/  | \_\ \___  |  /    /|   Y  \  ___// /_/  >  |  /
|   __/ \____/ \/\_/  \___  >__|     |___  / ____| /_____ \___|  /\___  >___  /|____/ 
|__|                      \/             \/\/            \/    \/     \/_____/  

欢迎使用鹧鸪答题系统
------------------------------------------------------------------------------------------
''')

def shunxu():
    with open('question.json', 'r', encoding='utf8') as f:
        a = json.load(f)
        for i in range(len(a)):
            print('*' * 30)
            print(f'第{i}题')
            print(a[i]['questionn'])
            print(a[i]['A'])
            print(a[i]['B'])
            print(a[i]['C'])
            print(a[i]['D'])
            qa = input("请输入答案：\n")
            if qa.upper() == a[i]['answer']:
                print('答案正确')
            else:
                print(f"答案错误，正确答案 {a[i]['answer']}")
def suiji():
    with open('question.json', 'r', encoding='utf8') as f:
        a = json.load(f)
        list = []
        while True:
            i = random.randint(0,81)
            list.append()
            if i not in list:
                print('*' * 30)
                print(f'第{i}题')
                print(a[i]['questionn'])
                print(a[i]['A'])
                print(a[i]['B'])
                print(a[i]['C'])
                print(a[i]['D'])
                qa = input("请输入答案：\n")
                if qa.upper() == a[i]['answer']:
                    print('答案正确')
                else:
                    print(f"答案错误，正确答案 {a[i]['answer']}")
            else:
                pass
def choose():
    print("*" * 30)
    q = input('请输入你想练习的方式：\n1：顺序练习\n2：随即练习\n')
    if q == "1":
        shunxu()
    elif q == "2":
        suiji()
    else:
        print('选择有误请重新输入')
        choose()
if __name__ == '__main__':
    caidan()
    choose()