# #导入判断工具(从collections_abc 模块导入Iterable
# from _collections_abc import Iterable
#
# #第二步:通过 isinstance (对象,类型)判断
# print(isinstance([1, 2, 3], Iterable))#==1说明这个列表是可迭代对象
# print(isinstance({"name":"小小", "age":19}, Iterable))
# print(isinstance("abc",Iterable))
# print(isinstance(123,Iterable))#==0说明这个整数不是可迭代对象
# li = [1,2,3,4]
#
# #通过 liter(可迭代对象)获取对应的迭代器
# li_iter = iter(li)
#
# #通过next(迭代器）逐个获取元素
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# #遍历完所有元素，所以会报错
# print(next(li_iter))
# print(next(li_iter))
#有误会
"""
#iter是迭代器,next能把迭代器的可迭代对象读取出来且。next每次只能取出一组数据，取多了会报错，
#和for的区别在于迭代器加next可以多批量多批次的取出大量数据，适合用在内存小但是需要处理大数据的地方
#但是for就是集成了迭代器和next的集合体
"""
#迭代器的定义
"""iter() 是获取迭代器的函数，next() 可以从迭代器中一次取出一个数据，数据取完后继续调用就会报 StopIteration。
迭代器可以记录读取位置，让程序按需获取数据。对于按需产生数据的迭代器，可以避免一次性加载大量数据，节省内存。
for 循环底层就是自动使用 iter() 和 next() 进行迭代，并自动处理迭代结束的情况。
next() 和 for 都可以节省内存，区别在于 next() 可以手动控制取数据的时机，而 for 自动不断取数据。
# li = [1,2,3,4]
# iter([1,2,3])
class MyIterator:
    def __init__(self,current):
        self.current = 5 #遍历初始值

    #实现__iter__方法，返回自身
    def __iter__(self):
        return self

        # 实现__next__方法，返回下一个元素
    def __next__(self):
        if self.current >5:
            raise StopIteration()
        #返回当前数字，然后增加1
        self.current += 1
        return  self.current
myIterator = MyIterator(5)
for i in myIterator:
    print(i)
"""
#列表推导式
"""
li=([n for n in range(1,11)])
print([n * 5 for n in li])

print([n for n in range(1, 11) if n % 2 == 0])
"""
#生成器（列表推导式吧[]改为()）
"""
li=(n for n in range(1,11))
li2= iter(li)
print(next(li2))
print(next(li2))
print(next(li2))
print(next(li2))
print(next(li2))
"""
#yield函数
def generator():
    yield 10
    yield 20
    yield 30

g = generator()

print(next(g))  # 10
print(next(g))  # 20
print(next(g))  # 30
print("======================================")
# ==================== Python 迭代器与生成器总结 ====================

# 一、基本概念
# 1. 迭代：一个一个地获取数据。
# 2. 可迭代对象：能通过 iter() 获取迭代器的对象，如列表、字符串、元组等。
# 3. 迭代器：能通过 next() 不断获取下一个元素，并记录读取进度的对象。
# 4. 生成器：一种特殊的迭代器，通常用 yield 或生成器表达式创建。
# 5. 所有迭代器都是可迭代对象，但不是所有可迭代对象都是迭代器。


# 二、iter() 与 next()
# iter(obj)：从可迭代对象获取迭代器。
# next(it)：获取迭代器的下一个元素。
# 数据耗尽后再调用 next(it)，会抛出 StopIteration 异常。

numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

# 三、for 循环的底层原理
# for 会先使用 iter() 获取迭代器，再重复调用 next()。
# 遇到 StopIteration 时，for 会自动结束循环。

for n in numbers:
    print(n)


# 四、可迭代对象与迭代器的区别
# 列表是可迭代对象，但列表本身不是迭代器。
# 自定义迭代器通常需要实现 __iter__() 和 __next__()。
# __iter__() 返回迭代器；__next__() 返回下一个值。
# 普通迭代器的 __iter__() 通常直接 return self。

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


for n in MyIterator(1, 5):
    print(n)  # 依次输出 1、2、3、4、5

# 五、迭代器的独立性
# 对同一个列表分别调用两次 iter()，会获得两个独立的迭代器。

numbers = [10, 20, 30]
a = iter(numbers)
b = iter(numbers)

print(a is b)  # False
print(next(a))  # 10
print(next(b))  # 10
print(next(a))  # 20

# 如果 b = num，则 num 和 b 引用同一个迭代器，共享读取进度。

b = a
print(a is b)  # True
print(next(b))  # 30

# 对已经存在的迭代器调用 iter()，通常会返回它自己。

it = iter([1, 2, 3])
print(iter(it) is it)  # True


# 六、next() 不一定要求对象实现 __iter__()
# 只要对象实现了 __next__()，直接 next(obj) 就可以调用它。
# 但要作为规范的迭代器并供 for 正常使用，还需要 __iter__()。

class Test:
    def __next__(self):
        return 100


t = Test()
print(next(t))  # 100


# 七、生成器与 yield
# yield 会返回一个值并暂停函数，下次 next() 从暂停处继续执行。
# return 会结束函数。

def generator():
    yield 10
    yield 20
    yield 30


g = generator()

print(next(g))  # 10
print(next(g))  # 20
print(next(g))  # 30

# 生成器表达式：使用小括号，按需计算元素。
g = (i for i in range(1000000))

# 八、内存与实际应用
# for 与 next() 都可以按需读取数据。
# 是否节省内存，取决于数据源是否按需产生或加载，
# 而不是 for 或 next() 本身。
# next() 的优势是可以手动控制什么时候取下一个值。
# for 的优势是代码简洁，可以自动处理迭代结束。


# 九、最终记忆
# iter()：获取迭代器。
# next()：取下一个值。
# __iter__()：定义如何获取对象的迭代器。
# __next__()：定义如何取下一个值。
# for：自动调用 iter() 和 next()。
# yield：产生一个值并暂停生成器。
# StopIteration：告诉程序迭代结束。














































































