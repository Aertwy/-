import re
import tkinter as tk
class Window:
    def __init__(self):
        root = tk.Tk()
        root.title("简单的小计算器(～￣▽￣)～")
        root.geometry("400x500")
        # 设定是否能够改变窗口的宽和高尺寸
        root.resizable(False, False)
        # 窗口图标
        root.iconbitmap('pigm.ico')
        # 颜色
        root.config(bg="#39c5bb")
class Calculator:
    def __init__(self):
        self.result=0
        self.expression=None
        self.numbers = []
        self.operators = []


    # 先判断是否是包含特殊字符
    def jud(self):
        #正则表达式：# 全字母匹配喵
        pattern = r'[a-zA-Z]'
        result = bool(re.search(pattern, self.expression))
        if result:
            print("错误:有英文字母")
            return False
        else:
            return True
    # 拆分字符串
    def parse(self):
        self.numbers = []
        self.operators = []
        current = ""
        self.expression = input()
        if not self.jud():
            return False
        else:
            for i in self.expression:
                # 判断i是否在里如果是则为Ture
                if i in ("+", "-", "×", "÷"):
                    # 乘法加进去
                    self.operators.append(i)
                    self.numbers.append(float(current))
                    current = ""
                else:
                    current += i
            else:
                self.numbers.append(float(current))
                current = ""
        return True

    #计算
    def calculate(self):
        #初始化
        opera1 = 0   #下标
        result = 0   #计算结果
        state = False#是否有乘除
        self.result = 0
        while len(self.operators) != 0:
            # 状态判断
            for i in self.operators:
                if i in ("×", "÷"):
                    state = True
                    break
                else:
                    state = False
            for opera, a in enumerate(self.operators):
                if state:
                    if a in ("×", "÷"):
                        opera1 = opera
                        if self.operators[opera1] == "×":
                            result = self.numbers[opera1] * self.numbers[opera1 + 1]
                        elif self.operators[opera1] == "÷":
                            try:
                                result = self.numbers[opera1] / self.numbers[opera1 + 1]
                            except ZeroDivisionError:
                                self.numbers.clear()
                                print("除数不能为零")
                                return False
                        break
            if not state:
                for opera, a in enumerate(self.operators):
                    if a in ("+", "-"):
                        opera1 = opera
                        if self.operators[opera1] == "+":
                            result = self.numbers[opera1] + self.numbers[opera1 + 1]
                        elif self.operators[opera1] == "-":
                            result = self.numbers[opera1] - self.numbers[opera1 + 1]
                        break
            self.numbers[opera1] = result
            self.numbers.pop(opera1 + 1)
            self.operators.pop(opera1)
        self.result = self.numbers[0]

        return True
    def run(self):
        if self.parse():
            if self.calculate():
                print(self.result)


if __name__=="__main__":
    print("输入+,-,×,÷不用等于")
    r = Calculator()
    r.run()
    r.run()














