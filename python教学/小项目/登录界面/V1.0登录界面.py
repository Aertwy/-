
import tkinter as tk
import re

class Window:
    def __init__(self):
        # ====================屏幕初始化==============================
        self._password=None
        self._account=None
        self.si_login =None
        self.account = ""
        self.password = ""
        self.root = tk.Tk()
        self.root.title("登录界面(～￣▽￣)～")
        self.root.geometry("700x500")
        # 设定是否能够改变窗口的宽和高尺寸
        self.root.resizable(False, False)
        # 窗口图标
        #self.root.iconbitmap('pigm.ico')
        # 颜色
        self.root.config(bg="#39C5BB")
        #=============================中间
        self.root.update_idletasks()  # 先让 Tk 算出窗口真实大小
        w, h = self.root.winfo_width(), self.root.winfo_height()
        x = (self.root.winfo_screenwidth() - w) // 2  # 屏幕宽 - 窗口宽 再对半分
        y = (self.root.winfo_screenheight() - h) // 2
        self.root.geometry(f"+{x}+{y}")
        #=======色卡======================
        self.miku={
            "bg": "#39C5BB", "surface": "#EAFBF7",
            "primary": "#1F8C85","primary_active": "#176F6A",
            "text": "#0F4C49", "accent": "#FF7043",
            "success": "#2E9E96","danger": "#E8505B"}
        #====标题===========================
        lab = tk.Label(self.root,
                       text="登录系统V1.0",
                       font=("微软雅黑", 25),
                       bg = self.miku["bg"],
                       fg=self.miku["text"])
        lab.pack()
        #账号
        self.__account = tk.StringVar(self.root)
        # 文本框！创建！
        self.in_account = tk.Entry(self.root, textvariable=self.__account,font=("微软雅黑", 17),justify="left",bg="#123F3C",fg="#BFF5EF")
        self.in_account.place(x = 250,y=180,width =200,height=30)
        lab1 = tk.Label(self.root,
                       text="账号:",
                       font=("微软雅黑", 17),
                       bg = self.miku["bg"],
                       fg=self.miku["text"])
        lab1.place(x=190,y=175)
        #=======================================
        # 密码
        self.__password = tk.StringVar(self.root)
        # 文本框！创建！
        self.in_password = tk.Entry(self.root,show="*",
                                    textvariable=self.__password,
                                    font=("微软雅黑", 17),
                                    justify="left",bg="#123F3C",fg="#BFF5EF",)
        self.in_password.place(x = 250,y=235,width =200,height=30)
        lab1 = tk.Label(self.root,
                       text="密码:",
                       font=("微软雅黑", 17),
                       bg = self.miku["bg"],
                       fg=self.miku["text"])
        lab1.place(x=190,y=235)
        #==================================================
        #登录
        self.in_login = tk.Button(
            self.root,
            text="登录",  # 字
            font=("微软雅黑", 20, "bold"),  # 字体
            bg="#FFFFFF",  # 按钮背景色
            fg="#0F4C49",  # 按钮字体色
            activebackground="#D9F3EE", # 背景
            command=lambda:self.denlu())  # 按下执行
        self.in_login.place(x=220, y=277, width=100, height=40)
        # ==================================================
        #注册
        self.in_register = tk.Button(
            self.root,
            text="注册",  # 字
            font=("微软雅黑", 20, "bold"),  # 字体
            bg="#FFFFFF",  # 按钮背景色
            fg="#0F4C49",  # 按钮字体色
            activebackground="#D9F3EE",  # 背景
            command=lambda:self.enrolled())# 按下执行
        self.in_register.place(x=370, y=277, width=100, height=40)
        self.l = Login()
        #====================================================
        #主页面报错信息
        self.error_text = tk.StringVar(self.root,value="")
        self.error = tk.Label(self.root,
                              textvariable=self.error_text,
                              fg='red',
                              bg='#39c5bb',
                              justify="left")
        self.error.place(x=250, y=210)
        self.root.mainloop()  # 循环
    #登录
    def denlu(self):
        self.account =self.__account.get()
        self.password =self.__password.get()
        if self.l.login(self.account,self.password):
            self.error_text.set("登录成功")
        else:
            error= self.l.error()
            self.error_text.set(str(error))
    #注册
    def enrolled(self):
    #=============子窗口==============================
        enr = tk.Toplevel(self.root)
        enr.title("注册账号")
        enr.geometry("300x300")
        # 设定是否能够改变窗口的宽和高尺寸
        enr.resizable(False, False)
        # 颜色
        enr.config(bg="#39C5BB")

        enr.update_idletasks()  # 先让 Tk 算出窗口真实大小
        w, h = enr.winfo_width(), enr.winfo_height()
        x = (enr.winfo_screenwidth() - w) // 2  # 屏幕宽 - 窗口宽 再对半分
        y = (enr.winfo_screenheight() - h) // 2
        enr.geometry(f"+{x}+{y}")
        #标题
        lab = tk.Label(enr,
                   text="注册",
                   font=("微软雅黑", 10),
                   bg=self.miku["bg"],
                   fg=self.miku["text"])
        lab.pack()
#=================================================
        # 账号
        self._account = tk.StringVar(enr)
        # 文本框！创建！
        si_account = tk.Entry(enr,textvariable=self._account, font=("微软雅黑", 10), justify="left",
                                   bg="#123F3C", fg="#BFF5EF")
        si_account.place(x=70, y=100, width=150, height=30)
        lab1 = tk.Label(enr,
                        text="账号:",
                        font=("微软雅黑", 10),
                        bg=self.miku["bg"],
                        fg=self.miku["text"])
        lab1.place(x=30, y=100)
        # =======================================
        # 密码
        self._password = tk.StringVar(enr)
        # 文本框！创建！
        si_password = tk.Entry(enr, show="*",
                                    textvariable=self._password,
                                    font=("微软雅黑", 10),
                                    justify="left", bg="#123F3C", fg="#BFF5EF", )
        si_password.place(x=70, y=150, width=150, height=30)
        lab1 = tk.Label(enr,
                        text="密码:",
                        font=("微软雅黑", 10),
                        bg=self.miku["bg"],
                        fg=self.miku["text"])
        lab1.place(x=30, y=150)

        # 登录
        self.si_login = tk.Button(
            enr,
            text="确认",  # 字
            font=("微软雅黑", 10, "bold"),  # 字体
            bg="#FFFFFF",  # 按钮背景色
            fg="#0F4C49",  # 按钮字体色
            activebackground="#D9F3EE",  # 背景
            command=lambda: self.in_enrolled())  # 按下执行
        self.si_login.place(x=70, y=200, width=150, height=30)
        # ==================================================
    #========================================================
    def in_enrolled(self):
        account =self._account.get()
        password =self._password.get()
        if self.l.register(account, password):
            print("注册成功")
        else:
            error= self.l.error()
            print(error)

class Login:
    def __init__(self):
        self.account = ""
        self.password = ""
        self.mistake = ""
        self.lo_status = False#登录状态
        self.re_status=False#注册状态
# ------------------------------------------注册--------------------------------------------------------------
# ==============================================================================================================
    def login(self,account,password):#登录
        lo_account = account
        lo_password = password
        if not self.generality(lo_account,lo_password):
            return False
        else:
            if not self.login_error(lo_account, lo_password):
                return False
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
    def register(self,account,password):
        re_account = account
        re_password = password
        if not self.generality(re_account,re_password):
            return False
        else:
            if not self.register_error(re_account):
                return False
            else:
                with open("book.txt", "a") as f:
                    f.write(f"{re_account},{re_password},\n")
                    return True

    #注册错误判断
    def register_error(self,re_account):# 临时变量
        words = ""
        # 账号格式错误
        if not len(re_account) <= 10:
            self.mistake = "AccountFormatError"
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
#============================================结束=======================================================
    #错误
    def error(self):
        if self.mistake=="InputError":
            return "输入错误"
        elif self.mistake=="AccountDuplicationError":
            return "账号重复"
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
























