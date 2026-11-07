import os
import random as r


class Guess:

    def __init__(self):
        self.guess = r.randint(0, 101)
    def guesss(self):
        print("猜一个0-100以内的整数:")
        while True:
            try:
                in_put = input()
                in_put = int(in_put)
            except ValueError:
                print("输入错误")
                continue
            print(self.guess)
            if in_put < self.guess:
                os.system("cls")
                print(f"该数字大于{in_put}")
            elif in_put > self.guess:
                os.system("cls")
                print(f"该数字小于{in_put}")
            else:
                print("猜对辣")
                break
        if input("按Q再来把！").lower() == "q":
            self.guess = r.randint(0, 101)
            self.guesss()
        return
if __name__ == "__main__":
    g= Guess()
    g.guesss()