import re
class Calculator:
    def __init__(self):
        self.result=0
        self.expression=None
        self.numbers = []
        self.operators = []

    # 先判断是否是包含特殊字符
    def jud(self):
        pattern = r'[a-zA-Z]'  # 全字母
            # 输入

        result = bool(re.search(pattern, self.expression))
        if result:
            print("错误:有英文字母")
            return False
        else:
            return True
    # 拆分字符串
    def parse(self):
        self.numbers = []
        self.operators = []
        current = ""
        self.expression = input()
        if self.jud():
            for i in self.expression:
                # 判断i是否在里如果是则为Ture
                if i in ("+", "-", "×", "÷"):
                    # 乘法加进去
                    self.operators.append(i)
                    self.numbers.append(float(current))
                    current = ""
                else:
                    current += i
            else:
                self.numbers.append(float(current))
                current = ""

    #计算
    def calculate(self):
        #初始化
        opera1 = 0#下标
        result = 0#计算结果
        state = False#是否有乘除
        while len(self.operators) != 0:
            # 状态判断
            for i in self.operators:
                if i in ("×", "÷"):
                    state = True
                    break
                else:
                    state = False
            for opera, a in enumerate(self.operators):
                if state:
                    if a in ("×", "÷"):
                        opera1 = opera
                        if self.operators[opera1] == "×":
                            result = self.numbers[opera1] * self.numbers[opera1 + 1]
                        elif self.operators[opera1] == "÷":
                            try:
                                result = self.numbers[opera1] / self.numbers[opera1 + 1]
                            except ZeroDivisionError:
                                print("除数不能为零")
                                return
                        break
            if not state:
                for opera, a in enumerate(self.operators):
                    if a in ("+", "-"):
                        opera1 = opera
                        if self.operators[opera1] == "+":
                            result = self.numbers[opera1] + self.numbers[opera1 + 1]
                        elif self.operators[opera1] == "-":
                            result = self.numbers[opera1] - self.numbers[opera1 + 1]
                        break
            self.numbers[opera1] = result
            self.numbers.pop(opera1 + 1)
            self.operators.pop(opera1)
        self.result = self.numbers[0]
        return self.result

r = Calculator()
r.parse()
r.calculate()
print(r.result)














