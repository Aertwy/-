class BankAccount:
    def __init__(self, name, money):
        self.name = name  #账户名
        self.__money = money  #余额
    #查询余额
    def view_in(self):
        print(f"账户名:{self.name},余额:{self.__money}")
    #存款
    def deposit(self, amount):
        if amount > 0:
            self.__money += amount
            print("存款成功")
        else:
            print("金额不合法")
    # 取款
    def withdraw(self, amount):
        if amount <= self.__money:
            self.__money -= amount
            print("取款成功")
        else:
            print("余额不足！")
#接口
noe1 = BankAccount("Aertwy",3100)
noe1.deposit(1000)#存
noe1.withdraw(8700)#取

noe1.view_in()

















