class Dog:                          # class = 定义一张"狗"的图纸
    def __init__(self, name, age):  # __init__ = 狗"出生"时，登记它的特点
        self.name = name            # self.name 是属性："名字"
        self.age = age              # self.age 是属性："年龄"

    def bark(self):                 # def = 在图纸上写"会叫"这个动作
        print(f"{self.name}：汪汪！")  # 这就是方法：叫

# —— 下面开始用图纸造狗（叫"创建对象"）——

dog1 = Dog("旺财", 3)   # 造出第 1 只狗，它就是一个对象
dog2 = Dog("大黄", 5)   # 造出第 2 只狗，它是另一个对象

print(dog1.name)   # 看属性：输出 旺财
print(dog2.age)    # 看属性：输出 5
dog1.bark()        # 用方法：输出 旺财：汪汪！
dog2.bark()        # 用方法：输出 大黄：汪汪！