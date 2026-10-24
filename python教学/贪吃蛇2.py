import turtle
#随机数
import random
# 创建屏幕
screen = turtle.Screen()
#设置长宽
screen.setup(width=800, height=800)
# 创建食物
food = turtle.Turtle()
# 创建分数
score_writer = turtle.Turtle()
# 初始化

def initialization() :

    score_writer.penup()
    score_writer.goto(-20, 315)
    score_writer.hideturtle()
    # 修改窗口标题
    screen.title("猫猫贪吃蛇")
    # 海龟变方
    turtle.shape("square")
    # 海龟变绿
    turtle.color("green")
    # 不留线条
    turtle.penup()
    # 初始化方位
    turtle.goto(0, 0)
    food.shape("square")
    food.color("red")
    food.penup()
    food.goto(80, 100)
    #边框

    wall = turtle.Turtle()
    wall.color("black")
    wall.penup()  # 不线
    wall.hideturtle()  # 隐藏光标

    wall.goto(-330, 330)  # 左上
    wall.pendown()

    wall.goto(330, 330)  # 右上
    wall.pendown()


    wall.goto(330, -330)  # 右下角



    wall.pendown()
    wall.goto(-330, -330)  # 左下

    wall.pendown()

    wall.goto(-330, 330)  # 左上
    wall.pendown()
initialization()
#                                                                                                                                                                                                                                                           #看不到我喵
class MM:
    def __init__(self,dx,dy,score):
        self.dx = dx
        self.dy = dy
        self.score = score
        self.game_over =False

    # 移动喵
    def move(self,dx, dy):
        x,y = turtle.xcor(),turtle.ycor()
        x, y = x + dx, y + dy
        turtle.goto(x, y)
    #生成一个蛇身
    def create_body(self):
        body = turtle.Turtle()
        body.shape("square")
        body.color("blue")
        # 不留线条
        body.penup()
        return body
    # 上
    def move_up(self):
        if self.dy != -20:
            self.dx, self.dy = 0, +20
    # 下
    def move_down(self):
        if self.dy != +20:
            self.dx, self.dy = 0, -20
    # 左
    def move_left(self):
        if self.dx != +20:
            self.dx,self.dy = -20,0
    # 右
    def move_right(self):
        if self.dx != -20:
            self.dx,self.dy = +20,0
    #吃掉食物,生成食物
    def check_food(self):
        if turtle.distance(food) < 10:
            self.score += 10
            score_writer.clear()
            score_writer.write(f"分数：{self.score}")
            she = self.create_body()#新蛇身
            x,y = bodies[-1].pos()
            she.goto(x,y)
            bodies.append(she)
            print(f"当前蛇身数量：{len(bodies)}")
            # 食物是否在循环当中
            li = list(range(-280, 281, 20))
            while True:
                chongdie = False
                f_x = random.choice(li)
                f_y = random.choice(li)
                for b in bodies:
                    x, y = b.pos()
                    if x == f_x and y == f_y:
                        chongdie = True
                        break
                if f_x == turtle.xcor() and f_y == turtle.ycor():
                    chongdie = True
                if not chongdie:
                    food.goto(f_x, f_y)
                    break
    #运行时钟（饿啊）
    def auto_move(self):
        x1, y1 = turtle.xcor(), turtle.ycor()#保存蛇头原来的目标
        #将最后一节蛇身往前挪，依次
        for b in range(len(bodies) - 1, 0, -1):
            x, y = bodies[b - 1].pos()
            bodies[b].goto(x,y)
        #0号蛇身移动到蛇头的位置

        bodies[0].goto(x1, y1)
        self.move(self.dx, self.dy) #移动
        self.check_food()
        if not self.check_wall() and not self.check_self():#判断撞墙or自撞
            screen.ontimer(self.auto_move, 200) #重复
        else:
            screen.title("游戏结束")
            score_writer.clear()
            score_writer.goto(0, 0)
            score_writer.write(
                f"游戏结束\n最终分数为:{self.score}\n按R重来""",
                align="center",                 #center：居中
                font=("Arial", 24, "bold")      #bold:粗体
            )
            self.game_over = True
    #撞墙
    def check_wall(self):
        x, y = turtle.xcor(), turtle.ycor()
        if x < -300 or x > 300 or y < -300 or y > 300:
            return True
        return False
    #自撞
    def check_self(self):
        for i in bodies:
            if turtle.distance(i)<10: #蛇头turtle和蛇身bodies的距离
                return True
        return False
    #复位
    def restart(self):
        if self.game_over:
            self.score = 0  # 分数0
            self.dx, self.dy = 20, 0  # 方向右
            turtle.goto(0, 0)  # 蛇头
            score_writer.clear()  # 字
            score_writer.goto(-20, 315)
            score_writer.write(f"分数：{self.score}")  # 显示
            while len(bodies) > 2:  # 删列表
                she = bodies.pop()
                she.hideturtle()
            body0.goto(-20, 0)
            body1.goto(-40, 0)
            screen.ontimer(self.auto_move, 200)
            food.goto(80, 100)
            self.game_over = False





mm=MM(20,0,0)
score_writer.write("分数：0",)
# 创建蛇身

body0,body1 = mm.create_body(),mm.create_body()
body0.goto(-20,0)
body1.goto(-40,0)
bodies=[body0, body1]

mm.auto_move()
screen.listen()
#让窗口接收键盘输入
screen.onkey(mm.restart, "R")
screen.onkey(mm.move_up, "W")
screen.onkey(mm.move_down, "S")
screen.onkey(mm.move_left, "A")
screen.onkey(mm.move_right, "D")

# 进入图形事件循环，让窗口保持响应
turtle.done()




















