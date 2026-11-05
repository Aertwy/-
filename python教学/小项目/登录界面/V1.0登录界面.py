
import tkinter as tk
import tkinter.font as tkfont          # 字体模块（第 09 章）
from tkinter import ttk                # ttk 控件（更现代外观的一部分控件）
from tkinter import messagebox         # 弹窗：提示/警告/错误/确认
from tkinter import simpledialog       # 弹窗：输入框
from tkinter import filedialog         # 弹窗：打开/保存文件
from tkinter import colorchooser       # 弹窗：取色器
import re
import os

class Window:
    def __init__(self):
        # ====================屏幕初始化==============================
        self.expression = ""
        self.root = tk.Tk()
        self.root.title("登录界面(～￣▽￣)～")
        self.root.geometry("700x500")
        # 设定是否能够改变窗口的宽和高尺寸
        self.root.resizable(False, False)
        # 窗口图标
        #self.root.iconbitmap('pigm.ico')
        # 颜色
        self.root.config(bg="#39C5BB")
        for i in range(4):
            self.root.columnconfigure(i, weight=1, uniform="key")
        #=============================中间
        self.root.update_idletasks()  # 先让 Tk 算出窗口真实大小
        w, h = self.root.winfo_width(), self.root.winfo_height()
        x = (self.root.winfo_screenwidth() - w) // 2  # 屏幕宽 - 窗口宽 再对半分
        y = (self.root.winfo_screenheight() - h) // 2
        self.root.geometry(f"+{x}+{y}")
        #=======色卡======================
        miku={
            "bg": "#39C5BB", "surface": "#EAFBF7",
            "primary": "#1F8C85","primary_active": "#176F6A",
            "text": "#0F4C49", "accent": "#FF7043",
            "success": "#2E9E96","danger": "#E8505B"}
        #====标题===========================
        lab = tk.Label(self.root,
                       text="登录系统V1.0",
                       font=("微软雅黑", 25),
                       bg = miku["bg"],
                       fg=miku["text"])
        lab.pack()
        #账号
        self.account = tk.StringVar(self.root)
        # 文本框！创建！
        self.in_account = tk.Entry(self.root, textvariable=self.account,font=("微软雅黑", 17),justify="right",bg="#123F3C",fg="#BFF5EF")
        self.in_account.place(x = 250,y=180,width =200,height=30)
        lab1 = tk.Label(self.root,
                       text="账号:",
                       font=("微软雅黑", 17),
                       bg = miku["bg"],
                       fg=miku["text"])
        lab1.place(x=190,y=175)
        #=======================================
        # 密码
        self.password = tk.StringVar(self.root)
        # 文本框！创建！
        self.in_password = tk.Entry(self.root, textvariable=self.password,font=("微软雅黑", 17),justify="right",bg="#123F3C",fg="#BFF5EF")
        self.in_password.place(x = 250,y=230,width =200,height=30)
        lab1 = tk.Label(self.root,
                       text="密码:",
                       font=("微软雅黑", 17),
                       bg = miku["bg"],
                       fg=miku["text"])
        lab1.place(x=190,y=225)
        #==================================================
        #登录
        self.in_login = tk.Button(
            self.root,
            text="登录",  # 字
            font=("微软雅黑", 20, "bold"),  # 字体
            bg="#FFFFFF",  # 按钮背景色
            fg="#0F4C49",  # 按钮字体色
            activebackground="#D9F3EE")  # 背景
            #command=lambda:pass  # 按下执行
        self.in_login.place(x=220, y=270, width=100, height=40)
        # ==================================================
        #注册
        self.in_register = tk.Button(
            self.root,
            text="注册",  # 字
            font=("微软雅黑", 20, "bold"),  # 字体
            bg="#FFFFFF",  # 按钮背景色
            fg="#0F4C49",  # 按钮字体色
            activebackground="#D9F3EE")  # 背景
            #command=lambda:pass  # 按下执行
        self.in_register.place(x=370, y=270, width=100, height=40)











        self.root.mainloop()  # 循环



class Login:
    def __init__(self):
        self.account = ""
        self.password = ""
        self.mistake = ""
        self.lo_status = False#登录状态
        self.re_status=False#注册状态
    def infor(self):#界面
        print("=" * 30)
        print("\t登录系统V1.0")
        print("1.登录\n2.注册\n")
        print("=" * 30)
# ------------------------------------------注册--------------------------------------------------------------
# ==============================================================================================================
    def login(self):#登录
        os.system("cls")
        print("=" * 30)
        print("\t登录")
        lo_account = input("请输入账号")
        lo_password = input("请输入密码")
        if not self.generality(lo_account,lo_password):
            print(self.error())
            input("按任意键退出")
            return False
        else:
            if not self.login_error(lo_account, lo_password):
                print(self.error())
                input("按任意键退出")
                return False
            else:
                print("登录成功")
        input("按任意键退出")
        return True
    def login_error(self,lo_account, lo_password):#登录错误判断
        with open("book.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                words = line.split(",")
                if words[0] == lo_account and words[1] == lo_password:
                    return True
            else:
                self.mistake = "IncorrectAccountPassword"
                return False
    def generality(self,account,password): #共性
        chinese = re.compile(r'[\u4e00-\u9fa5]+')  # 中文
        char = re.compile(r"[!@#$%^&*-+=|:;'<>,.?]")  # 特殊字符
        uppercase = re.compile(r'[A-Z]')  # 包含大写字母
        lowercase = re.compile(r'[a-z]')  # 小写字母
        # 空账号
        if account == "":
            self.mistake = "EmptyAccountError"
            return False
        elif password == "":
            self.mistake = "EmptyPasswordError"
            return False
        # 7到15以内字符，包含字母大小写和"!@#$%^&*-+=|:;'<>,.?"中的特殊字符
        if not (not bool(chinese.search(password))
                and
                bool(char.search(password))
                and
                bool(uppercase.search(password))
                and
                bool(lowercase.search(password))
                and
                7 <= len(password) <= 15):
            self.mistake = "FormatError"
            return False
        return True
# ===========================================结束=====================================================================
#--------------------------------------------注册--------------------------------------------------------------
#=============================================================================================================
    # 注册
    def register(self):
        os.system("cls")
        print("=" * 30)
        print("\t注册")
        print("账号:1-10以内字符")
        print("密码:7到15以内字符，包含字母大小写，!@#$%^&*-+=|:;'<>,.?中的一种特殊字符")
        print("=" * 30)
        re_account = input("账号:")
        re_password = input("密码:")
        password = input("确认密码输入")
        if not self.generality(re_account,re_password):
            print(self.error())
            input("按任意键退出")
            return False
        else:
            if not self.register_error(password, re_account, re_password):
                print(self.error())
                input("按任意键退出")
                return False
            else:
                with open("book.txt", "a") as f:
                    f.write(f"{re_account},{re_password},\n")
                    print("注册成功")
                    input("按任意键退出")
                    return True
    #注册错误判断
    def register_error(self,password,re_account,re_password):# 临时变量
        words = ""
        # 账号格式错误
        if not len(re_account) <= 10:
            self.mistake = "AccountFormatError"
            return False
        # 判断是否重复密码错误
        if not password == re_password:
            self.mistake = " ConfirmPasswordError"
            return False
        with open("book.txt","r") as f:
            lines = f.readlines()
            for line in lines:
                words = line.split(",")
                #账号是否重复
                if  words[0]==re_account:
                    self.mistake = "AccountDuplicationError"
                    return False
            return True
#============================================结束=================================================================================================================
    #运行
    def run(self):
        while True:
            self.infor()
            ordinal = input("输入序号:")
            if ordinal == "1":
                self.login()
            #注册页面
            elif ordinal == "2":
                self.register()
            self.mistake = "InputError"
            os.system("cls")
            continue
    #错误
    def error(self):
        if self.mistake=="InputError":
            return "输入错误"
        elif self.mistake=="AccountDuplicationError":
            return "账号重复"
        elif self.mistake==" ConfirmPasswordError":
            return "确认密码错误"
        elif self.mistake=="IncorrectAccountPassword":
            return "账号或密码错误"
        elif self.mistake=="EmptyAccountError":
            return "账号为空"
        elif self.mistake=="EmptyPasswordError":
            return "密码为空"
        elif self.mistake=="FormatError":
            return "密码格式错误"
        elif self.mistake=="AccountFormatError":
            return "账号格式错误"
        return True
if __name__ == "__main__":
    n = Window()



























