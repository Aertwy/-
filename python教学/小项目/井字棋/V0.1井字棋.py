import re
import tkinter as tk
import os
class Window:
    def __init__(self):
        # ====================屏幕初始化==============================
        self.root = tk.Tk()
        self.root.title("井字棋(～￣▽￣)～")
        self.root.geometry("300x300")
        # 设定是否能够改变窗口的宽和高尺寸
        self.root.resizable(False, False)

        self.root.config(bg="#1F8C85")
        for i in range(4):
            self.root.columnconfigure(i, weight=1, uniform="key")
        self.root.mainloop()
class Main:
    def __init__(self):
        self.first="先手"#状态
        self.fi = []#先手坐标
        self.se = []#后手坐标
        self.mistake = ""
        # 坐标
        self.coordinate={"1":[0, 0], "2":[0, 1], "3":[0, 2],
                         "4":[1, 0], "5":[1, 1], "6":[1, 2],
                         "7":[2, 0], "8":[2, 1], "9":[2, 2]}
    #地图
    def map(self):
        print("#\t" * 5)
        # 生成边框1
        for x in range(0, 3):
            print("#", end="\t")
            for y in range(0, 3):
                #这里是如果遍历到输入的值就可以创建一个
                if [x, y] in self.fi:
                    print("X", end="\t")
                elif [x, y] in self.se:
                    print("o", end="\t")
                else:
                    print(".", end="\t")
            print("#", end="")
            print()
        print("#\t" * 5)
    def start(self):
#=================下面是输入值错误===================================
        try:
            coord = input(f"{self.first}输入坐标1-9:")
        except KeyError:
            self.mistake = "KeyError"
            return False
        try:
            if self.first == "先手":
                self.fi.append(self.coordinate[coord])
                self.coordinate.pop(coord)
            else:
                self.se.append(self.coordinate[coord])
                self.coordinate.pop(coord)
        except KeyError:
            self.mistake = "RepeatedInputError"
            return False
        return True

#================================================================
    #胜利条件
    def victory(self):
        #当棋子先手棋子数量大于=3才判断
        if len(self.fi) < 3:
            return False
        for i in range(2):
            if i ==1:
                first = self.se
            else:
                first = self.fi
            # 棋子胜利条件，穷举8种连续的数字
            if (all([0, y] in first for y in range(3))
                    or
                    all([1, y] in first for y in range(3))
                    or
                    all([2, y] in first for y in range(3))
                    # =============================竖排
                    or
                    all([x, 0] in first for x in range(3))
                    or
                    all([x, 1] in first for x in range(3))
                    or
                    all([x, 2] in first for x in range(3))
                    # =============================对角↓
                    or
                    # 即打印正序坐标012也打印倒叙坐标210
                    all([x, y] in first for x, y in enumerate(range(2, -1, -1)))
                    or
                    all([x, x] in first for x in range(3))):
                return True
        # 平局
        if len(self.coordinate) == 0:
            return -1
        return False
    #错误
    def error(self):
        if self.mistake == "KeyError":
            return "输入错误"
        elif self.mistake == "RepeatedInputError":
            return "重复输入错误"
        return False
    #运行模式

    def run(self):
        #判断平局和胜利
        while True:
            err = self.error()
            vic = self.victory()
            #没有胜利所以继续执行
            os.system("cls")
            if bool(isinstance(err,str)):
                print(err)
                self.mistake = ""
                continue
            elif  vic == False and err == False:
                self.map()
                if self.start():
                    if self.first == "先手":
                        self.first = "后手"
                    else:
                        self.first = "先手"
            elif vic == -1:#这是平局
                print("平局")
                break
            elif vic == True:
                if self.first=="先手":
                    print("后手赢")
                    break
                else:
                    print("先手赢")
                    break
        uqd = input("输入任意键退出按出，Q继续")
        if uqd == "Q":
            self.reset()
            uqd = 0
            return
    #复位
    def reset(self):
        self.first="先手"#状态
        self.fi = []#先手坐标
        self.se = []#后手坐标1
        self.mistake = ""
        # 坐标
        self.coordinate={"1":[0, 0], "2":[0, 1], "3":[0, 2],
                         "4":[1, 0], "5":[1, 1], "6":[1, 2],
                         "7":[2, 0], "8":[2, 1], "9":[2, 2]}
        self.run()
if __name__ == "__main__":
    main = Main()
    main.run()






































































