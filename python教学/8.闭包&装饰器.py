#闭包定义：函数嵌套;内层函数用了外层函数的局部变量，并在外层函数结束后还能用
"""
def outer():
    print("我是外层函数")
    def inner():
        print("我是内层函数")
    inner()

outer()
================================================================

#外层
def outer():
    tang = "三分糖"
    print("执行外包")
    #内层
    def inner():
        print(f"制作一杯{tang}的奶茶")
    return inner   #不要加()，加()==调用

out1 = outer()
out1()
=================================================================
升级版
def outer(base_num):
    def inner(add_num):
        print(f"{base_num}+{add_num}={base_num+add_num}")
    return inner
#调用外部函数并接受返回值
add = outer(10)
#调用内部函数
add(100)
add(110)
#创建一个闭包
add15 = outer(15)
add15(3)
"""
#============================================
"""
def send_msg():
    print("登录验证")
    print("发送消息给快乐")
    
def sned_mony():
    print("登录验证")
    print("转账给快乐")
    
def look_news():
    print("登录验证")
    print("查看快乐的动态")
    痛点：每次都要函数都要加一个登录验证
"""
#=======================================
#装饰器
"""def denglyz(func):
    print("执行外包")
    def wrapper():
        #新增功能：登录验证
        print("登录验证......")
        func()
    return wrapper

def send_msg():
    print("发送消息给快乐")


def sned_money():
    print("转账给快乐")


def look_news():
    print("查看快乐的动态")


# deng = denglyz(send_msg)
# deng()

denglyz(look_news)()
痛点：手动包装很麻烦
======================================
痛点：只适用于直接加上去的地方，不可以传参
def send_msg(diaoyon):
    def inner():
        print('登录验证')
        diaoyon()
    return inner
@send_msg      #send_msg(send_1)
def send_1():
    print("发送消息给快乐")

@send_msg
def sned_2():
    print("送外卖给快乐")

send_1()
#send_1() == send_msg(send_1)() 这两个是一样的

"""

def send_msg(diaoyon):
    def inner():
        print("登录验证")
        diaoyon()
    return inner

@send_msg
def send_msg1(name):
    print(f"发送消息给{name}")

@send_msg
def send_money(name,money):
    print(f"转账给{name}，{money}")

send_msg1("快乐")

send_money("快乐",111)




