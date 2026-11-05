import tkinter as tk
import re
import os


class Login:
    def __init__(self):
        self.account = ""
        self.password = ""
        self.mistake = ""
        self.lo_status = False#登录状态
        self.re_status=False#注册状态
    #界面
    def infor(self):
        print("=" * 30)
        print("\t登录系统V1.0")
        print("1.登录\n2.注册\n3.忘记密码\n")
        print("=" * 30)


# ------------------------------------------注册--------------------------------------------------------------
# ==============================================================================================================
    #登录
    def login(self):
        os.system("cls")
        self.account = input("请输入账号")
        self.password = input("请输入密码")
        input("按任意键退出")
        return True
    #登录错误判断
    def login_error(self):
        pass
# ===========================================结束======================================================================


#--------------------------------------------注册--------------------------------------------------------------
#=============================================================================================================
    # 注册

    def register(self):
        os.system("cls")
        print("=" * 30)
        print("\t注册")
        re_account = input("请输入账号")
        re_password = input("请输入密码")
        password = input("确认密码输入")
        if not self.register_error(password,re_account,re_password):
            return False
        else:
            with open("Account book.txt", "a", encoding='utf-8') as f:
                f.write(f"{re_account},{re_password},\n")
                print("注册成功")
                input("按任意键退出")
                return True
    #注册错误判断
    def register_error(self,password,re_account,re_password):# 临时变量
        words = ""
        #判断是否重复密码错误
        if not password == re_password:
            self.mistake = " ConfirmPasswordError"
            return False
        #账号重复错误
        with open("Account book.txt","r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                words = line.split(",")
                #账号是否重复
                if  words[0]==re_account:
                    self.mistake = "AccountDuplicationError"
                    return False
            return True
#============================================结束=================================================================================================================
    #忘记密码
    def forget(self):
        print("忘记")

    #运行
    def run(self):
        while True:
            self.infor()
            ordinal = input("输入序号:")
            if ordinal == "1":
                self.login()
                return True
            #注册页面
            elif ordinal == "2":
                if not self.register():
                    print(f"错误:{self.error()}")
                    input()
            elif ordinal == "3":
                self.forget()
                return True
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
            return "账号错误"

        return True


if __name__ == "__main__":
    win = Login()
    win.run()



























