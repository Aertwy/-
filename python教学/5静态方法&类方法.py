#实例属性就用实例方法（先创建对象在用对象访问）
#类属性就用类方法（可以直接通过@ classmethod，cls来访问类的属性）
#既不访问实例属性也不访问类属性就用静态方法（主要用来计算）


#class Person:
#    def __init__(self, name):
#        self.name = name
#    def hello(self):
#       print(f"你好呀我是{self.name}")
#p= Person("小明")
#p.hello()
"""
#场景用不到访问类属性或者示例属性
class GeometryTool:
    @staticmethod #静态方法（可以去掉self)，可以直接通过类名调用
    def circle_area(banjin):
        return 3.14* banjin ** 2

print(GeometryTool.circle_area(34))

虽然可以用实例化对象，但是不建议容易混淆
geo = GeometryTool()
print(geo.circle_area(34))
"""


class Renlei:
    pinjun_age = 899
    @classmethod #类方法带有cls参数(无需显式传参)，可以通过类来找
    def get_pinjun(cls):   #cls是class的简写，人类平均年龄
        return cls.pinjun_age

    @classmethod
    def set_pinjun(cls,age):   #修改人类平均年龄
        cls.pinjun_age = age
"""renlei = Renlei()
renlei.set_pinjun(1000)
print(renlei.get_pinjun())

renlei1 = Renlei()
print(renlei1.get_pinjun())
"""
Renlei.set_pinjun(100)
#可以通过类名直接调用，更简洁
#应用场景(获取更新全班的人数，产品默认价格)





























