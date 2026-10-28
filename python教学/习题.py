# ──────────────────────────────────────────
# 输出九九乘法表
"""
for i in range(1,10):

    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}",end="\t")


    print(end="\n")


# 需求：编写一个程序，该程序用于找出并打印所有的水仙花数。
# 水仙花数：指一个三位数，其各位数字立方和等于该数本身。(几位数就是几次方)输入判断
for mun in range(100,1000):
    i = mun //100
    k = mun //10 % 10
    j = mun % 10
    jk=i**3+k**3+j**3
    if mun == jk:
        print(mun)
"""


# 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个，第二天早上又将剩下的桃
# 子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个，到第10天早上想再吃时，
# 见只剩下一个桃子了，求第一天共摘了多少个。
"""
# 第一天摘下了X个桃子，吃了X÷2—1, (X÷2-1)÷2—1,((X÷2-1)÷2—1)÷2—1....=1
tao1= 1
for x in range(1,10):
    tao1= 2*(1+tao1)
print(f"一共摘{tao1}了个桃子")
"""
# ──────────────────────────────────────────
# 需求：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
num=0
b=0
c=0
abc =0
chinese = 0
rest = 0

shu = input()

# 遍历数字
for i in shu:

    if i.isdigit():#判断数字
        num += 1

    elif i.isalpha():#判断字母，中文
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z': #判断字母
            abc += 1
        else:
            chinese +=1
    elif i == " ":#判断空格
        c += 1
    else:
        rest+=1

print(f"数字次数:{num},"
        f"字母次数:{abc}"
        f"中文次数:{chinese}"
        f"空格次数:{c}"
        f"其他字符次数:{rest}")
"""
# ──────────────────────────────────────────
# 需求：给定一个简单列表，对其元素进行排序。
# 简单列表：元素类型不是复合类型（列表/元组/字典）。
# 示例：
# -形式1:[20,50,10,40,30]
# -形式2:[bb','ee','aa','dd','cc']
"""
li=[10,829,89201,890,890,8]
# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
# 遍历所有数组元素
    for i in range(n):
# 内循环每次将最大值放在最右边
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # 打印
    for i in range(len(arr)):
        print ("%d" %arr[i])#
# bubble_sort(li)
# 或者
li.sort(reverse=False)#
print(li)
"""
# ──────────────────────────────────────────
## 需求：给定一个学生信息列表，根据学生的成绩进行排序。
# 学生成绩数据格式：复杂列表，元素是字典或者元组。
# 示例：
# [
# {'sno': 101, 'same': "小张", 'grade': 88},
# {'sno': 102, 'same': "小王", 'grade': 77},
# {'sno': 103, 'same': "小李", 'grade': 99},
# {'sno': 104, 'same': "小赵", 'grade': 66}
"""
li=[
    {'sno': 101,'same':"小张",'grade':88},
    {'sno': 102,'same':"小王",'grade':77},
    {'sno': 103,'same':"小李",'grade':99},
    {'sno': 104,'same':"小赵",'grade':66}
]
su1=sorted(li,key=lambda x:x['sno'])
print(su1)
"""
# ──────────────────────────────────────────
# 需求：给定一个整数列表，计算并打印该列表中所有偶数的和。
"""
i1=0
li = [100,80,9021,8905,10,92]
for i in li:
    if i % 2 == 0:
        i1 += i

print(i1)
"""

# ──────────────────────────────────────────
# 需求：给定一个字典，其中每个人的姓名作为键，对应的年龄作为值。请找出年龄最大者的姓名与年龄，并将其打印出来。
"""
# 只通过if和for找最大的（先找值，然后用循环遍历，在用内嵌循环和所以值对比，不对的话就让原始值更大的来比
dian={"快乐":18,"猫娘":20,"大肥鱼":999,"克劳德":1000}
通过max找的key最大值
zuida = max(dian.values())
for k,v in dian.items():
    if v == zuida:
        print(f"最大年龄:{v}岁\n名字：{k}")
"""

# 思路一，两层for
"""
i =0
for i in dian.values():
    for j in dian.values():
        if i>j:
            pass
print(i)
"""
# 思路二，只用一层for
"""
zhuida=0
name = ""
a = 0
for i,a in dian.items():

    # 假设zhuida为最大，让他和a比
    if  zhuida<a:       #如果不大于a那么zuida就不是最大的，所以要赋值给a这样a就是最大的
        zhuida = a
        name = i
print(f"最大年龄:{zhuida}岁\n名字：{name}")
"""

#需求：给定一个已排序的整数列表，要求输入一个数，并根据列表原有的排序规律将其插入到正确的位置上。
"""
li = [1,28,88,100,590,10000,100000]
insert = input("输入整数")
insert = int(insert)
cishu = 0
for i in li:
    if insert < i:
        li.insert(cishu,insert)#insert(变量，下标)
        cishu += 1
        break
    else:
        cishu += 1
print(li)
"""

#需求：接收用户输入的三个数字，并按从小到大的顺序输出。
"""
a,b,c = map(float,input().split())
li = [a,b,c]
li.sort()
print(*li)
"""

# 需求：用户输入一个奇数，程序需要找到一个最小的由连续9组成的数（例如9，99，999，9999等），这
# 个数能被用户输入的奇数整除。输出这个最小的数以及它除以用户输入的奇数的结果。
"""
divisor = 0
num = int(input())
jpeg = 0
cishu = 0

if num <= 0 or num % 2 == 0 or num % 5 == 0:#判断是不是奇数
    print("不存在符合要求的数字")
else:
    for i in range(10):#10次没找到循环就退出
        cishu += 1#每次循环次数+1
        divisor = divisor * 10 + 9#每次生成比上一次循环更大的9

        if divisor % num == 0: #判断是否有余数
            jpeg = divisor // num
            break

    if divisor % num != 0:
        print("超过10个9，结束计算")
    else:
        print(f"由最小的{cishu}个9组成的数能被{num}整除：{divisor}/{num}={jpeg}")
"""

# 需求：提示用户连续输入最多7个整数（每个数在1至50之间，包含1和50）。对于每个有效输入（即
# 在1至50之间的数），程序将打印该数个数的*。

#li=map(int,input().split())
#用了乘号的
"""
for i in li:
    if 0 < i <=50:
        print("*" * i)
"""
#不用乘号
"""
for i in li:
    if 0 < i <=50:
        for n in range(i):
            print("*", end="")
    print()
"""
# 需求：用户输入一个数，判断该数是奇数还是偶数，并给出相应的输出结果。
# 偶数：能够被2所整除的整数，是2的倍数。
"""
user = input()
user=int(user)
if user %2 ==0:
    print("是偶数")
else:
    print("是奇数")
"""

# 需求：用户输入年份，判断该年份是否为闰年，并给出相应的输出结果。
# 闺年：
# 1.如果一个年份能被4整除但不能被100整除，那么它是闰年。
# 2.如果一个年份能被400整除，那么它也是闰年。、
"""
user = int(input())
if user %4==0 and user % 100 !=0 or user % 400 ==0:
    print("是闰年")
"""

#需求：用户输入一个数字，实现十进制向二进制、八进制、十六进制的转换功能，并打印出转换结果。
"""
num = int(input("请输入一个十进制整数："))

print("二进制：", bin(num))
print("八进制：", oct(num))
print("十六进制：", hex(num))
"""

#需求：编写一个程序，计算a+aa+aaa+aaaa+的值，其中a是一个数字，且加数的个数由键盘输
#入决定。例如，当a=2且共有5个数相加时，表达式为2+22+222+2222+22222。
"""
user,frequency=map(int, input("值和加的次数").split())
nue = 0
for i in range(frequency):
    nue +=user
    user = user * 10 + (user % 10)

print(nue)
"""

# 需求：定义一个名为factorial的函数，该函数用于计算并返回给定整数的阶乘值。
# 阶乘：一个正整数的阶乘是所有小于及等于该数的正整数的积，0的阶乘为1。
# 示例：5的阶乘：1*2*3*4*5;10 的阶乘：1*2*3*4*5*6*7*8*9*10。
"""
a = input("输入阶乘:")
a = int(a)
def factorial(num):
    se = 1
    if a ==0:
        return se
    for i in range(num+1):
        if i >0:
            se *= i
    return se
se1=factorial(a)
print(se1)
"""

#需求：定义一个函数，该函数用于计算并返回给定半径的圆的面积（要求结果保留两位小数）。
"""
def circle_area (num):
    a= 3.14*num**2
    return round(a, 2) #round，保留2位小数
print(circle_area(5))
"""

#需求：定义一个函数，该函数用于计算从1²到N²的所有整数的平方和。
"""
def sum_squares(num):
    u = 0
    for i in range(num+1):
        u += i**2
    return u
print(sum_squares(6))
"""

#需求：定义一个函数，该函数用于计算并返回给定数字列表中所有数字的总和。
"""
def sum_squares(list):
    s =0
    for i in list:
        s+=i
    return s
li = [10, 20, 30, 40, 50]
su = sum_squares(li)
print(su)
"""

#需求：定义一个函数，该函数用于返回指定范围内所有偶数的列表。
"""
def sum_squares(min_scope,max_scope):
    li=[]
    for i in range(min_scope,max_scope+1):
        if i % 2==0:
            li.append(i)
    return li
miao= sum_squares(10,20)
print(miao)
"""


# 需求：定义一个函数，该函数用于从第一个列表list1中移除所有存在于第二个列表list2中的元素。
# 示例：原始列表：[3，5,7,9，11，13]，移除元素列表：[7，11]，移除后：[3，5，9，13]
"""
def remove_list(list1,list2):
    su = []
    for i in list1:
        if i not in list2:
            su.append(i)
    return su
su1 = remove_list([3, 5, 7, 9, 11, 13], [3, 7, 9, 11, ])
print(su1)
"""


# 需求：定义一个函数，该函数用于对列表进行去重处理，并返回一个新的列表，其中不包含任何重复的元素。
# 示例：原始列表：[10,20,30,10,20]，去重后：[10,20，30]
"""
def remove_list(list1):
    su = []
    for i in list1:
        if i not in su:
            su.append(i)
    return su
su1 = [10, 20, 30, 10, 20]
print(remove_list(su1))
"""
#单列表去重
"""
def remove_list(list1):
    combined_list = list(set(list1))
    return combined_list

su1 = [10, 20, 30, 10, 20]
lie = remove_list(su1)
print(lie)
"""
#两列表去重
"""
def remove_list(list1,list2):
    combined_list = list(set(list1 + list2))
    return combined_list
su1 = [3, 5, 7, 9, 11, 13]
su2 = [3, 7, 9, 11,15,1 ]
lie = remove_list(su1,su2)
print(lie)
"""

#需求：定义一个函数，该函数用于实现两个变量值的互换操作。
"""
def variable(var1,var2):
    var1, var2 = var2, var1
    return var1, var2

su1,su2 = variable(3,5)
print(su1,su2)
"""

#需求：定义一个函数，该函数接收一个字典作为参数，并返回该字典中所有值的总和。
"""
def sum_dictionary(dictionary):
    miao = 0
    for value in dictionary.values():
        miao += value
    return miao
s1 = {"快乐":18,"猫娘":15,"deek":999,"克劳德":1000}
miao1 = sum_dictionary(s1)
print(miao1)
"""


# 需求：定义一个函数，该函数用于根据传入的整数n返回对应的倒数序列和：若n为偶数，则计算和1/2
# +1/4+...+1/n；若n为奇数，则计算和1/1+1/3+..+1/n。
"""
from fractions import Fraction
def sum_descending_sequence(n):
    f1 = Fraction(0, 1)
    if n % 2 == 0:
        for i in range(2,n+1,2):
            f1 += Fraction(1, i)

    else:
        for i in range(1, n + 1, 2):
            f1 += Fraction(1, i)

    return f1

f2 = sum_descending_sequence(11)
d1 = sum_descending_sequence(10)
print(f"这是奇数{f2}，这是偶数{d1}")
"""

# 需求：定义一个函数，该函数接收年份、月份和日期作为参数，计算这一天是该年的第几天。
#一个月是30.4天，约成30天
"""
def yrmd(year, month, day):
    yrde = 0
    common_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = leap_year
    else:
        days = common_year
    for i in range(month - 1):
        yrde += days[i]
    yrde += day
    return yrde
su1=yrmd(2026,7,29)
print(su1)
"""

# 需求：定义一个函数，该函数用于计算斐波那契数列中的第n项。
# 斐波那契数列：数列的前两项均为1，从第三项开始，每+项都是其前两项的和。如：1、1、2、3、5、8、13、21、34、．
"""
def fibonacci(num):
    a = 1
    b = 1
    c = 1
    for i in range(1,num+1) :
        c = a+b
        a = c
        print(f"{a}+{i}={b}")
fibonacci(10)
"""















































