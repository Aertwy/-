import tkinter as tk


class Window:
    def __init__(self):
        # ====================屏幕初始化==============================
        self.expression = ""
        self.root = tk.Tk()
        self.root.title("简单的小计算器(～￣▽￣)～")
        self.root.geometry("400x500")
        # 设定是否能够改变窗口的宽和高尺寸
        self.root.resizable(False, False)
        # 窗口图标
        self.root.iconbitmap('pigm.ico')
        # 颜色
        self.root.config(bg="#123F3C")
        #====================下面是数字按钮初始化==============================
        #颜色
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
        buttons = ["0", "1", "2", "3", "4",
                "5", "6", "7", "8", "9"]
        self.button = []
        for index,i in enumerate(buttons):
            button= tk.Button(
                self.root,
                text=i, #字
                font=("微软雅黑", 30,"bold"),#字体
                bg=color["num_bg"],#按钮背景色
                fg=color["num_fg"],#按钮字体色
            activebackground = color["num_active"],
            command=lambda x = i:self.input_num(x)
            )
            button.grid(row=index//3 + 1, column=index%3)
            self.button.append(button)

        #=================显示！启动！=======================
        # 变量！创建！
        self.display = None
        # 字符串！创建！
        self.display = tk.StringVar(self.root)
        #文本框！创建！
        self.input_box=tk.Entry(self.root,textvariable=self.display)
        self.input_box.grid(row=0, column=0, columnspan=4)
        # =================加减乘除=======================
        buttons = ["+", "-", "×", "÷",]
        self.operation = []
        for index,i in enumerate(buttons):
            operation= tk.Button(
                self.root,
                text=i, #字
                font=("微软雅黑", 30,"bold"),#字体
                bg=color["num_bg"],#按钮背景色
                fg=color["num_fg"],#按钮字体色
            activebackground = color["num_active"],
            command=lambda x = i:self.input_num(x)
            )

            operation.grid(row=index, column=3)
            self.operation.append(operation)
        # =================清空=======================
        self.clear = tk.Button(self.root,text="C", #字
                font=("微软雅黑", 30,"bold"),#字体
                bg=color["num_bg"],#按钮背景色
                fg=color["num_fg"],
                activebackground=color["num_active"],
                command=self.clear1)
        self.clear.grid(row=4, column=4)
        # =================删除=======================
        self.dele = tk.Button(self.root,text="X", #字
                font=("微软雅黑", 30,"bold"),#字体
                bg=color["num_bg"],#按钮背景色
                fg=color["num_fg"],
                activebackground=color["num_active"],
                command=self.dele1)
        self.dele.grid(row=4, column=3)
        # =================等于=======================
        self.equals = tk.Button(self.root,text="=", #字
                font=("微软雅黑", 30,"bold"),#字体
                bg=color["num_bg"],#按钮背景色
                fg=color["num_fg"],
                activebackground=color["num_active"],
                command=self.equals1)
        self.equals.grid(row=4, column=2)
        # =================小数点=======================
        self.decimal = tk.Button(self.root,text=".", #字
                font=("微软雅黑", 30,"bold"),#字体
                bg=color["num_bg"],#按钮背景色
                fg=color["num_fg"],
                activebackground=color["num_active"],
                command=lambda x = ".":self.input_num(x))
        self.decimal.grid(row=4, column=5)

    def equals1(self):
        pass

    #删除
    def dele1(self):
        original_str = self.expression
        self.expression = original_str[:-1]
        self.display.set(self.expression)
    #清空
    def clear1(self):
        self.expression = ""
        self.display.set(self.expression)
    def input_num(self,x):
        #数字按钮！更新！
        self.expression += x
        # 文本框！更新！
        self.display.set(self.expression)
    def run(self):
        self.root.mainloop()
w = Window()

w.run()



