class Fruit :
    def __init__(self, apple, orange, banana):
        self.apple = apple
        self.Orange = orange
        self.Banana = banana
    def pr(self):
        print(self.apple)
        print(self.Orange)
        print(self.Banana)


my_Fruit = Fruit("香蕉","橘子","苹果")
my_Fruit1 = Fruit("笨蛋喵","聪明喵","坏喵")
try:
    my_Fruit.pr()
    my_Fruit1.pr()
except TypeError :
    print('类型错误')





















