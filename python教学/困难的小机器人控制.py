#计算函数
import math

class Robot :
    def __init__(self,x,y,speed):
        self.x = x  #当前X坐标
        self.y = y  #当前Y坐标
        self.speed=speed#每秒速度
        self.angle = 0

    # dx=distance×cos(angle)
    # distance=speed×time
    #前进
    def move_forward(self,time):#time=移动秒数
        # 角度转弧度
        rad = math.radians(self.angle)
        distance =self.speed*time
        dx = distance * math.cos(rad)
        dy = distance * math.sin(rad)
        self.x += dx
        self.y += dy

        print(f"机器人当前坐标为[{self.x},{self.y}]")

    #后退
    def move_backward(self, time):
        #和前进相反
        rad = math.radians(self.angle)
        distance = self.speed * time
        dx = distance * math.cos(rad)
        dy = distance * math.sin(rad)
        self.x -= dx
        self.y -= dy

    #左角度
    def turn_left(self, angle):
        self.angle += angle
        self.angle %= 360

    #右角度
    def turn_right (self, angle):
        self.angle -= angle
        self.angle %= 360

    #计算障碍位置
    def detect_obstacle(self, obstacle_x, obstacle_y):
        #math.sqrt(数字)计算平方根，勾股定理
        num = math.sqrt((obstacle_x-self.x) ** 2 + (obstacle_y-self.y)** 2)
        if num > 12:
            print("detect_obstacle==True")
            return False

        else:
            print("detect_obstacle==False")
            return  True

    #障碍转向
    def safe_move(self, time, obstacle_x, obstacle_y):
        if  (
                    # 障碍物距离小于等于12
                self.detect_obstacle(obstacle_x, obstacle_y)
                and # 障碍物在行进路线2cm范围内
                self.is_ahead(obstacle_x, obstacle_y)
                and # 障碍不在行进方向的2距离以内
                self.is_blocking(obstacle_x, obstacle_y)
        ):
            #左转90度
            self.turn_left(90)
            print("检测到障碍，左转90度")
        else:
            self.move_forward(time)
            print("移动")
    #头部
    def is_ahead(self, obstacle_x, obstacle_y):
        # 角度转弧度
        rad = math.radians(self.angle)
        #障碍物相对机器人的方向
        dx = obstacle_x - self.x
        dy = obstacle_y - self.y
        #向量点积（点积可以判断障碍物对于机器人的朝向在前半部分还是后半部分）
        dot =dx*math.cos(rad)+dy*math.sin(rad)
        #设为0.000001是考虑有误差
        if dot > 0.000001:
            print("is_ahead==True")
            return True
        print("is_ahead==False")
        return False
    #判断障碍物挡路
    def is_blocking(self, obstacle_x, obstacle_y):
        #要是障碍物在前方
        if self.is_ahead(obstacle_x, obstacle_y):
            #要是头部的角度为0   和  绝对值障碍物的y轴-机器人的y轴小于等于2
            if (self.angle in(0,180) and abs(obstacle_y - self.y)<=2
                or
                self.angle in(90,270) and abs(obstacle_x - self.x)<=2
            ):
                    print("is_blocking==True")
                    return True
        print("is_blocking==False")
        return False


#        当前X坐标   当前Y坐标   每秒速度
r1 =Robot(x = 10,      y = 0,  speed = 10)
#障碍物坐标

r1.turn_left(90)

r1.safe_move(1, 11, 6)






























