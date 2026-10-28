#微信支付
"""""
class WechatPay:
    def pay(self,money):
        print(f"微信支付:扣除余额{money}元")
#支付宝支付
class ZfbPay:
    def pay(self,money):
        print(f"支付宝支付:扣除余额{money}元")
#银行卡支付
class BankPay:
    def pay(self,money):
        print(f"银行卡支付:扣除余额{money}元")

def pay_order(pay_obj,money):
    pay_obj.pay(money)#存款

pay_order(WechatPay(),1000)
pay_order(ZfbPay(),1000)
pay_order(BankPay(),1000)


class Animal:
    def make_sound(self):
        print("动物发出声")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("大狗叫叫叫")

class Cat(Animal):
    def make_sound(self):
        print("小猫喵喵喵")

def ani(anime):
    anime.make_sound()


ani(Dog())
ani(Cat())

#父类
class Pet :
    def eat(self):
        print("吃饭喵")
#子类继承父类的属性
class Dog(Pet) :

    def eat (self):
        super().eat()
        print("狗爱吃似")

class Cat(Pet):
    def eat(self):
        print("猫爱吃猫粮")

class Pig(Pet):

    def eat(self):
        print("猪不爱吃饭")
class Mast:
    def eat_go(self,pet):
        print("主人喂养实物")
        pet.eat()


Mast1 = Mast()
Mast1.eat_go(Dog())
Mast1.eat_go(Cat())
"""""


#父类图形
class Shape :
    def area(self):
        print("未实现")

class Circle(Shape) :
    def __init__(self,radius ):#半径
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape) :
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle(Shape) :
    def __init__(self,base ,height):
        self.base = base
        self.height  = height

    def area(self):
        return (self.base * self.height)/2


def print_area(a1):
    print(f"面积为{a1.area()}")

print_area(Rectangle(3,4))
print_area(Circle(3))
print_area(Triangle(3,4))





















