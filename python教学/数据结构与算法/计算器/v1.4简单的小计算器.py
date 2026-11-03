import re
import tkinter as tk
class Window:
    def __init__(self):
        # ====================屏幕初始化==============================
        self.expression = ""
        self.root = tk.Tk()
        self.root.title("简单的小计算器(～￣▽￣)～")
        self.root.geometry("410x570")
        # 设定是否能够改变窗口的宽和高尺寸
        self.root.resizable(False, False)
        # 窗口图标
        self.root.iconbitmap('pigm.ico')
        # 颜色
        self.root.config(bg="#123F3C")
        for i in range(4):
            self.root.columnconfigure(i, weight=1, uniform="key")
        # ====================下面是数字按钮初始化==============================
        # 颜色
        color = {
            # 基础
            "bg": "#39C5BB",  #
            "text_dark": "#0F4C49",  # 深青文字（标题、小字用，浅底上最清晰）

            # 显示屏（做"屏幕感"用深色）
            "display_bg": "#123F3C",  # 深青屏幕底
            "display_fg": "#BFF5EF",  # 薄荷白数字

            # 数字键（占面积最大，白色最清爽）
            "num_bg": "#FFFFFF",  # 白底
            "num_fg": "#0F4C49",  # 深青字
            "num_active": "#D9F3EE",  # 按下/悬停：薄荷白

            # 运算符 + - × ÷（比底色深一档，一眼区分）
            "op_bg": "#1F8C85",  # 中深青
            "op_fg": "#FFFFFF",  # 白字
            "op_active": "#176F6A",  # 按下更深

            # 等号（全场唯一的暖色，焦点就是它）
            "eq_bg": "#FF7043",  # 珊瑚橙（青的互补色，跳得出来）
            "eq_fg": "#FFFFFF",
            "eq_active": "#E85D3A",

            # 清除 C（喵系柔粉）
            "clear_bg": "#F8BBD0",
            "clear_fg": "#7A2E4B",
            "clear_active": "#F48FB1",
        }
        positions = {
            "7": (1, 0),
            "8": (1, 1),
            "9": (1, 2),

            "4": (2, 0),
            "5": (2, 1),
            "6": (2, 2),

            "1": (3, 0),
            "2": (3, 1),
            "3": (3, 2),

            "0": (4, 1)
        }
        self.button = []
        for index, i in enumerate(positions):
            row, column = positions[i]
            button = tk.Button(
                self.root,
                text=i,  # 字
                font=("微软雅黑", 30, "bold"),  # 字体
                bg=color["num_bg"],  # 按钮背景色
                fg=color["num_fg"],  # 按钮字体色
                activebackground=color["num_active"],
                command=lambda x=i: self.input_num(x)
            )

            button.grid(row=row,column=column,sticky="nsew",padx=4,pady=4)
            self.button.append(button)

        # =================显示！启动！=======================
        # 变量！创建！
        self.display = None
        # 字符串！创建！
        self.display = tk.StringVar(self.root)
        # 文本框！创建！
        self.input_box = tk.Entry(self.root, textvariable=self.display)
        self.input_box.config(
            font=("微软雅黑", 25),
            justify="right",
            bg="#123F3C",
            fg="#BFF5EF",
            insertbackground="white"
        )
        self.input_box.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="ew",
            padx=8,
            pady=12
        )
        # =================加减乘除=======================
        buttons = ["÷", "×", "-", "+", ]
        self.operation = []
        for index, i in enumerate(buttons):
            operation = tk.Button(
                self.root,
                text=i,  # 字
                font=("微软雅黑", 30, "bold"),  # 字体
                bg=color["op_bg"],  # 按钮背景色
                fg=color["op_fg"],  # 按钮字体色
                activebackground=color["op_active"],
                command=lambda x=i: self.input_num(x)
            )
            operation.grid(row=index+1, column=3, sticky="nsew", padx=4, pady=4)
            self.operation.append(operation)
        # =================清空=======================
        self.clear = tk.Button(self.root, text="C",  # 字
                               font=("微软雅黑", 30, "bold"),  # 字体
                               bg=color["clear_bg"],  # 按钮背景色
                               fg=color["clear_fg"],
                               activebackground=color["clear_active"],
                               command=self.clear1)
        self.clear.grid(row=4, column=0, sticky="nsew", padx=4, pady=4)
        # =================删除=======================
        self.dele = tk.Button(self.root, text="X",  # 字
                              font=("微软雅黑", 30, "bold"),  # 字体
                              bg=color["op_bg"],  # 按钮背景色
                              fg=color["op_fg"],  # 按钮字体色
                              activebackground=color["op_active"],
                              command=self.dele1)
        self.dele.grid(row=5,column=0,sticky="ew",padx=4,pady=4)
        # =================等于=======================
        self.equals = tk.Button(self.root, text="=",  # 字
                                font=("微软雅黑", 30, "bold"),  # 字体
                                bg=color["eq_bg"],  # 按钮背景色
                                fg=color["eq_fg"],
                                activebackground=color["eq_active"],
                                command=self.equals1)
        self.equals.grid(row=5,column=1,columnspan=3,sticky="ew",padx=4,pady=4)

        # =================小数点=======================
        self.decimal = tk.Button(self.root, text=".",  # 字
                                 font=("微软雅黑", 30, "bold"),  # 字体
                                 bg=color["num_bg"],  # 按钮背景色
                                 fg=color["num_fg"],
                                 activebackground=color["num_active"],
                                 command=lambda x=".": self.input_num(x))

        self.decimal.grid(row=4, column=2, sticky="nsew", padx=4, pady=4)
        #实例化下面的计算机喵
        self.calculator = Calculator()
        #错误提示
        self.warning = ""
        self.root.mainloop()#循环


#==============================================================================================================================
    def run(self):
        if  self.calculator.parse(self.expression):
            if self.calculator.calculate():
                return self.calculator.result
            else:
                message = self.calculator.error()
                return message#要是返回else就说明已经报错了
        else:
            message = self.calculator.error()
            return message



    # 等于
    def equals1(self):
        self.display.set(self.expression)
        return1 = self.run()
        #return1是整数和浮点数
        if isinstance(return1, (int, float)):
            #格式化，可以去0
            self.expression = f"{return1:g}"

        else:
            #如果是字符串就转字符串
            self.expression = str(return1)
            self.display.set(self.expression)
        self.display.set(self.expression)

    # 删除
    def dele1(self):
        original_str = self.expression
        self.expression = original_str[:-1]
        self.display.set(self.expression)

    # 清空
    def clear1(self):
        self.expression = ""
        self.display.set(self.expression)



    def input_num(self, x):
        # 数字按钮！更新！
        self.expression += x
        # 文本框！更新！
        self.display.set(self.expression)
class Calculator:
    def __init__(self):
        self.result=0
        self.expression=None
        self.numbers = []
        self.operators = []
        self.warning = ""
    # 先判断是否是包含特殊字符
    def jud(self):
        #正则表达式：# 全字母匹配喵
        pattern = r'[a-zA-Z]'
        result = bool(re.search(pattern, self.expression))
        if result:
            self.warning = "IllegalInputErrors"#包含

            return False
        #下面是有没有连续两个计算符==============================上面是判断有没有英文字符
        for i in range(len(self.expression)-1):
            if ( self.expression[i] in ("+", "-", "×", "÷")
                and
                    self.expression[i+1] in ("+", "-", "×", "÷")
            ):
                self.warning ="ExpressionError"
                return False
        return True
    #报错
    def error(self):

        if self.warning == "ZeroDivisionError":
            return "除数为0"
        elif self.warning == "IllegalInputErrors":
            return "输入非法"
        elif self.warning == "ExpressionError":
            return "表达式错误"
        elif self.warning=="EmptyExpressionError":
            return "表达式为空"
        return True

    # 拆分字符串
    def parse(self,expression):
        self.numbers = []
        self.operators = []
        current = ""
        self.expression = expression
        #========================================
        if self.expression =="":                 #
            self.warning="EmptyExpressionError"                       #
            return False                        #
        if not self.jud():                      #
            return False                        #
        #========================================
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
                if i in ("+", "-", "×", "÷"):
                    self.warning = "ExpressionError"
                    return False
                self.numbers.append(float(current))
                current = ""
        return True

    #计算
    def calculate(self):
        #初始化
        opera1 = 0#下标
        result = 0#计算结果
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
                                self.warning = "ZeroDivisionError"
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
if __name__=="__main__":
    w = Window()














