"""
使用 Python 的类来表示机器人。
可以设置机器人的初始位置和目标位置。
机器人每次只能移动一个单位。
机器人需要根据当前位置和目标位置，自动决定移动方向。
到达目标位置后，自动停止并输出最终位置。
如果初始位置就是目标位置，程序也必须正确结束。
"""
class Robot:
    def __init__(self,in_pos,destination):
        self.in_pos = in_pos    #初始位置   #速度
        self.destination = destination#终点
    #前移动
    def add_move(self):
        self.in_pos +=1

    #后移动
    def sub_move(self):
        self.in_pos -=1
    def information(self):
        print(f"起点位置:{self.in_pos}")
        print(f"终点位置:{self.destination}")
    #判断距离
    def move(self):
        self.information()
        print("======开始运行========")
        while True:
            print(f"当前距离:{self.in_pos}")
            if self.in_pos == self.destination:
                print("======结束运行========")
                print("已到达指定位置喵！")
                break
            #当现在位置大于终点，则后退
            elif self.in_pos > self.destination:

                self.sub_move()
            #当现在位置小于终点，则前进
            elif self.in_pos < self.destination:
                self.add_move()
            #初始位置    终点      速度
r2 = Robot(0,10)
r1 = Robot(8,3)
r = Robot(5,5)
r2.move()
r1.move()
r.move()