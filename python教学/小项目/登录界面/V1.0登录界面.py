# 修改注册，显示报错和退出功能就没了
import re
import tkinter as tk

import ui_common as ui


class Window:
    def __init__(self):
        self._password = None
        self._account = None
        self.register_window = None
        self.in_error_text = None
        # ====================屏幕初始化==============================
        self.root = ui.create_window("登录界面(～￣▽￣)～", size=(700, 500))
        result1 = ui.label(self.root, "登录系统V1.0", x=280, y=5, font=("微软雅黑", 17))
        self.root.iconbitmap('pigm.ico')
        # 主页面报错信息==============================================================================
        self.error = ui.label(self.root,
                              text="", x=250, y=210,
                              justify="left", bg='#39c5bb')
        # 账号==============================================================================
        self.__account = tk.StringVar(self.root)
        self.in_account = ui.labeled_entry(self.root,
                                           textvariable=self.__account,
                                           x=170, y=180, width=280, height=30,
                                           text="账号:",
                                           label_font=("微软雅黑", 17))
        # 密码=======================================
        self.__password = tk.StringVar(self.root)
        self.in_password = ui.labeled_entry(self.root,
                                            textvariable=self.__password,
                                            x=170, y=235, width=280, height=30,
                                            text="密码:",
                                            label_font=("微软雅黑", 17))
        # 登录==================================================
        self.in_login = ui.button(self.root, "登录",
                                  command=self.denlu,
                                  x=220, y=277,
                                  width=100, height=40,
                                  font=("微软雅黑", 20, "bold"))
        # 注册==================================================
        self.in_register = ui.button(self.root, "注册",
                                     command=self.enrolled,
                                     x=370, y=277,
                                     width=100, height=40,
                                     font=("微软雅黑", 20, "bold"))
        # ====================================================
        self.l = Login()
        self.root.mainloop()  # 循环

    def denlu(self):  # 登录
        account, password = self.__account.get(), self.__password.get()
        if self.l.login(account, password):
            ui.set_status(self.error, "登录成功", kind="success")
        else:
            ui.set_status(self.error, str(self.l.error()), kind="error")

    def enrolled(self):  # 注册
        # =============子窗口=========================================
        self.register_window = ui.create_window("注册账号", size=(300, 300), parent=self.root)
        self.register_window.iconbitmap('pigm.ico')
        result1 = ui.label(self.register_window, "注册", x=130, y=0, font=("微软雅黑", 10, "bold"))
        # 账号=================================================
        self._account = tk.StringVar(self.register_window)
        si_account = ui.labeled_entry(self.register_window, textvariable=self._account, x=30, y=100,
                                      width=200, height=30, text="账号:", label_font=("微软雅黑", 10))
        # 注册页面报错信息=======================================
        self.in_error_text = tk.StringVar(self.register_window, value="")
        in_error = ui.label(self.register_window, textvariable=self.in_error_text,
                            text="", x=60, y=76, justify="left", fg='red', bg='#39c5bb')
        # 密码=========================================
        self._password = tk.StringVar(self.register_window)
        si_password = ui.labeled_entry(self.register_window, textvariable=self._password, x=30, y=140,
                                       width=200, height=30, text="密码:", masked=True, label_font=("微软雅黑", 10))
        # 确认=======================================
        si_login = ui.button(self.register_window, "确认", command=self.in_enrolled,
                             x=70, y=200, width=120, height=30, font=("微软雅黑", 10, "bold"))

    # ========================================================
    def in_enrolled(self):
        account, password = self._account.get(), self._password.get()
        if self.l.register(account, password):
            self.register_window.after(3000, self.register_window.destroy)
        else:
            self.in_error_text.set(str(self.l.error()))


class Login:
    def __init__(self):
        self.mistake = ""

    # 登录
    def login(self, account, password):  # 登录
        words = ""
        if not self.generality(account, password):
            return False
        if not self.login_error(account, password):
            return False
        return True

    def login_error(self, account, password):  # 登录错误判断
        with open("book.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                words = line.split(",")
                if words[0] == account and words[1] == password:
                    return True
            else:
                self.mistake = "IncorrectAccountPassword"
                return False

    # 共性错误
    def generality(self, account, password):
        chinese = re.compile(r'[\u4e00-\u9fa5]+')  # 中文
        char = re.compile(r"[!@#$%^&*-+=|:;'<>.?]")  # 特殊字符
        uppercase = re.compile(r'[A-Z]')  # 包含大写字母
        lowercase = re.compile(r'[a-z]')  # 小写字母
        if account == "":  # 空账号
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

    # 注册
    def register(self, account, password):
        if not self.generality(account, password):
            return False
        else:
            if not self.register_error(account, password):
                return False
            else:
                with open("book.txt", "a") as f:
                    f.write(f"{account},{password},\n")
                    return True

    def register_error(self, re_account, re_password):  # 临时变量
        if not len(re_account) <= 10:  # 账号格式错误
            self.mistake = "AccountFormatError"
            return False
        if "," in re_account or "," in re_password:
            self.mistake = "IncorrectAccountPassword"
            return False
        with open("book.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                words = line.split(",")
                if words[0] == re_account:  # 账号是否重复
                    self.mistake = "AccountDuplicationError"
                    return False
        return True

    # 错误
    def error(self):  # 错误
        if self.mistake == "InputError":
            return "输入错误"
        elif self.mistake == "AccountDuplicationError":
            return "账号重复"
        elif self.mistake == "IncorrectAccountPassword":
            return "账号或密码错误"
        elif self.mistake == "EmptyAccountError":
            return "账号为空"
        elif self.mistake == "EmptyPasswordError":
            return "密码为空"
        elif self.mistake == "FormatError":
            return "密码格式错误"
        elif self.mistake == "AccountFormatError":
            return "账号格式错误"
        return True


if __name__ == "__main__":
    n = Window()
