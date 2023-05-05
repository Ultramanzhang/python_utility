import json

# 菜单函数
import os
import random

index = 0
success1 = 0


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


def openfile():
    with open('question.json', 'r', encoding='utf8') as f:
        a = json.load(f)
        return a


def printque(i):
    global success1
    global index
    a = openfile()
    print('*' * 30)
    print(f'第{i + 1}题')
    print(a[i]['questionn'])
    print(a[i]['A'])
    print(a[i]['B'])
    print(a[i]['C'])
    print(a[i]['D'])
    qa = input("请输入你的答案（输入q退出）：\n")
    if qa.upper() == a[i]['answer']:
        print('回答正确')
        success1 = success1 + 1
        index = index + 1
    elif qa.upper() == 'Q':
        print(f'本次共答{index}道题，正确率为{(success1 / index) * 100}%')
        choose()
    else:
        index = index + 1
        print(f"回答错误，正确答案 {a[i]['answer']}")


def shunxu():
    global success1
    global index
    for i in range(len(openfile())):
        printque(i)
    print(f'本次共答{index}道题，正确率为{(success1 / index) * 100}%')
    choose()


def suiji():
    global success1
    global index
    list = []
    while True:
        i = random.randint(0, 80)
        if i not in list:
            list.append(i)
            printque(i)
            if len(list)==81:
                print(f'本次共答{index}道题，正确率为{(success1 / index) * 100}%')
                choose()



def choose():
    print("*" * 30)
    print('\n\n\n')
    q = input('请输入你想练习的方式：\n1：顺序练习\n2：随机练习\n（Q退出本程序）\n\n')
    if q == "1":
        shunxu()
    elif q == "2":
        suiji()
    elif q.upper()=='Q':
        print('感谢使用，祝考试顺利')
        os.system('pause')
    else:
        print('选择有误请重新输入')
        choose()


if __name__ == '__main__':
    caidan()
    choose()
