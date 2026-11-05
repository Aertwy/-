import re

"""
if bool(chinese.search(a)):
    print("可以通过")
else:
    print("不允许通过")
"""


a1 = "Aa12345@"
chinese = re.compile(r'[\u4e00-\u9fa5]+')#中文
char = re.compile(r"[!@#$%^&*-+=|:;'<>,.?]")#特殊字符
uppercase =re.compile( r'[A-Z]')#包含大写字母
lowercase = re.compile(r'[a-z]')#小写字母
bvi = a1
"""
if not bool(chinese.search(bvi)):
    if bool(char.search(bvi)):#包含特殊字符
        if bool(uppercase.search(bvi)):
            if bool(lowercase.search(bvi)):
                if len(bvi) >= 7:
                    print("注册成功")
                print("错误:密码长度大于7位")
            else:
                print("错误:没有小写")
        else:
            print("错误:没有大写")
    else:
        print("错误:没有特殊字符")
else:
    print("错误:有中文")
"""

#7到30以内字符，包含字母大小写和"!@#$%^&*-+=|:;'<>,.?"中的特殊字符
if (not bool(chinese.search(bvi))
    and
    bool(char.search(bvi))
    and
    bool(uppercase.search(bvi))
    and
    bool(lowercase.search(bvi))
    and
    7 <= len(bvi) <= 30
):
    print("注册成功")
else:
    print("格式错误")
