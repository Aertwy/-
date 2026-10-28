import os

"""
这是重命名
os.rename("T1.txt","这是重命名.txt")

移动文件
os.rename("这是重命名.txt",r"E:\\python\\这是重命名.txt")

删除文件，无法恢复
os.remove("T1.txt")


#创建目录
os.mkdir("T2")

#删除目录
os.chdir("T2")

#查看当前工作目录
print(os.getcwd())

#查看目录内容
print(os.listdir())
print(os.listdir("E:\\"))

"""
#存在这个目录就返回Ture
print(os.path.exists("E:\\"))
print(os.path.exists(r"/python教学/File operations/6.File operations.py"))
#不存在这个目录就返回False
print(os.path.exists("I:\\"))






































