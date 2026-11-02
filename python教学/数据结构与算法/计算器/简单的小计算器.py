
#正则表达式
import re
#窗口控键
"""
import tkinter as tk
root = tk.Tk()
root.title("简单的小计算器(～￣▽￣)～")
root.geometry("400x500")
#设定是否能够改变窗口的宽和高尺寸
root.resizable(False, False)
#窗口图标
root.iconbitmap('pigm.ico')
#颜色
root.config(bg="#39c5bb")

lab = tk.Label(root, text=f"{j.result}",font=("黑体", 20))
lab.pack()
root.mainloop()
#一个加号按钮plus_sign= tk.Button()

"""



class Calculator:
    def __init__(self):
        self.result=0
        #这是输入
        self.expression=None

    #先判断是否是包含特殊字符
    def jud(self):
        #初始化
        self.expression = None
        pattern = r'[a-zA-Z]'#全字母
        #输入
        self.expression = input()
        result = bool(re.search(pattern, self.expression))
        if result:
            print("错误:有英文字母")
            return False
        else:
            return True

    #加
    def add(self):
        total = 0
        try:#执行函数调用
            if self.jud() :
                # 在整个字符串里搜索self.pattern，如果为NONE则为没有英文字母，但是我加上了bool就不用写两个判断了
                num1, *num2 = map(float, self.expression.split("+"))
                for i in num2:
                    total += i
                total+=num1
                self.result= total
                #将列表用+号连接成一个单独的字符串
                nu = "+".join(map(str,num2))
                print(f"{num1}+{nu}={total}")
        except ValueError:
            print("错误:表达式错误")

    #减
    def sub(self):
        try:#执行函数调用
            if self.jud() :
                # 在整个字符串里搜索self.pattern，如果为NONE则为没有英文字母，但是我加上了bool就不用写两个判断了
                num1, *num2 = map(float, self.expression.split("-"))
                total = num1
                for i in num2:
                    total -=i
                self.result = total
                nu = "-".join(map(str, num2))
                print(f"{num1}-{nu}={total}")
        except ValueError:
            print("错误:表达式错误")

    #乘
    def ride(self):
        try:  # 执行函数调用
            if self.jud():
                # 在整个字符串里搜索self.pattern，如果为NONE则为没有英文字母，但是我加上了bool就不用写两个判断了
                num1, *num2 = map(float, self.expression.split("×"))
                total=num1
                for i in num2:
                    total *= i
                self.result = total
                nu = "×".join(map(str, num2))
                print(f"{num1}×{nu}={total}")
        except ValueError:
            print("错误:表达式错误")

    #除
    def exclu(self):
        try:  # 执行函数调用
            if self.jud():
                # 在整个字符串里搜索self.pattern，如果为NONE则为没有英文字母，但是我加上了bool就不用写两个判断了
                num1, *num2 = map(float, self.expression.split("÷"))
                total=num1
                for i in num2:
                    total /=i
                self.result = total
                nu = "÷".join(map(str, num2))
                print(f"{num1}÷{nu}={total}")
        except ValueError:
            print("错误:表达式错误")
        except ZeroDivisionError:
            print("错误:除数不能为0")

if __name__ is "__main__":
    print("我去不早曰，还能这样用")
    j = Calculator()
    j.exclu()


