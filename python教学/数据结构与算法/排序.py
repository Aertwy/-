#冒泡排序
"""
def bubble(a):
    while True:
        f = False
        for i in range(len(a)-1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                f = True
        if not f:return a
test = [1,24,57,2,4,6879,32,576,879,321,45,678,3,8]
print(bubble(test))
"""
#选择排序
"""
def choose(num):
    #先将0下标送入min_index里面。len长度为6，会遍历6次
    for i in range(len(num)):
        min_index = i
    #送入之后就会从i+1=1开始遍历到j，每次上面遍历一次这里遍历i+1到6，如果上一个循环是0这里就是从1-6
        for j in range(i + 1, len(num)):
        #如果a[0]>a[j],也就是从10开始到20
            if num[min_index] > num[j]:
            #那就替换掉，将最小的下标从j移动到min_index里面
                min_index = j
        #找到最小的之后就开始替换
        num[i], num[min_index] = num[min_index], num[i]
    return a
print(choose(a))
"""

#冒泡排序
def bubble(num):
    while True:
        f = False
        for i in range(len(num)-1):
            if num[i] > num[i + 1]:
                num[i], num[i + 1] = num[i + 1], num[i]
                f = True
        if not f:
            return num
















































































































































