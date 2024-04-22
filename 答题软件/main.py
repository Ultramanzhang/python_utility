import json
import random
class Question:
    def __init__(self):
        # 记录已答题数目个数
        self.index = 0
        # 记录已答对题目个数
        self.success1 = 0

    # 打开文件函数，为了避免代码冗长，遂进行封装
    def openfile(self):
        try:
            with open('question.json', 'r', encoding='utf8') as f:
                a = json.load(f)
                return a
        except:
            print('文件打开失败')
            exit()

    # 核心函数，此函数打印题目
    def printque(self, i):
        a = self.openfile()
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
            self.success1 = self.success1 + 1
            self.index = self.index + 1
        elif qa.upper() == 'Q':
            print(f'本次共答{self.index}道题，正确率为{(self.success1 / self.index) * 100}%')
            self.choose()
        else:
            self.index = self.index + 1
            print(f"回答错误，正确答案 {a[i]['answer']}")

    # 顺序答题函数
    def shunxu(self):
        # 对文件中取出的数据求长度并遍历，实现顺序答题功能
        for i in range(len(self.openfile())):
            self.printque(i)
        print(f'本次共答{self.index}道题，正确率为{(self.success1 / self.index) * 100}%')
        self.choose()

    # 随机答题函数
    def suiji(self):
        # 定义列表，防止重复出题
        list = []
        # 求出文件数据长度，防止生成数据大于长度而导致崩溃
        len_a = len(self.openfile())
        # 此处定义死循环，让函数一直运行
        while True:
            i = random.randint(0, len_a)
            # 判断i是否在list之中，不在则取数第i个数据，在则继续循环
            if i not in list:
                list.append(i)
                self.printque(i)
                if len(list) == len(self.openfile()) and self.index != 0:
                    print(f'本次共答{self.index}道题，正确率为{(self.success1 / self.index) * 100}%')
                    self.choose()

    # 接收用户选择，无意义
    def choose(self):
        print("*" * 30)
        print('\n\n\n')
        q = input('请输入你想练习的方式：\n1：顺序练习\n2：随机练习\n（Q退出本程序）\n\n')
        if q == "1":
            self.shunxu()
        elif q == "2":
            self.suiji()
        elif q.upper() == 'Q':
            print('感谢使用，祝考试顺利')
            os.system('pause')
        else:
            print('选择有误请重新输入')
            self.choose()

    def main(self):
        self.choose()


# 主函数
if __name__ == '__main__':
    Question().main()
