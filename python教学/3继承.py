"""""
#父类
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}吃东西")

    def sleep(self):
        print(f"{self.name}睡觉")
#子类
class Dog(Animal):
    def dark(self):
        super().eat()

        super().__init__(self.name,self.age)
        print("大狗叫不叫:叫~叫~叫~")
dog1= Dog("大黄",5)
dog1.dark()
dog1.eat()
dog1.sleep()
"""""

# 父类：员工
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):               # 公共方法：子类直接继承
        print(f"姓名:{self.name}, 工号:{self.id}")


# 全职员工
class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary


# 兼职员工
class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days


# 测试
full = FullTimeEmployee("大伟", "114514", 20000)
part = PartTimeEmployee("冰冰", "4594", 100, 30)

full.print_info()
print("月薪:", full.calculate_monthly_pay())

part.print_info()
print("月薪:", part.calculate_monthly_pay())
"""""
#类继承练习：人力系统
员工分为两类:全职员工 FuLlTimeEmpLoyee、  
兼职员工 PartTimeEmpLoyee.
#-全职和兼职都有姓名 name"“工号 id"属性，
都具备"打印信息 print_info" (打印姓名、工号）方法。
#-全职有“月薪 monthty_ salary"属性，
兼职有“日薪 daily_salary"属性、“每月工作天数 work_days"的属性。
全职和兼职都有“计算月薪 calculate_ monthly_pay"的方法，但具体计算过程不一样。
"""""#题目

















