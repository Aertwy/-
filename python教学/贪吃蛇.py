#随机数
import random
#清空终端屏幕
import os
#键盘控制
import turtle
#地图
def draw_map (snake,food):
    print("#\t"*12)
    #生成边框
    for y in range(0, 10):
        print("#",end="\t")
        for x in range(0, 10):
        #食物
            if   [x,y] == food :
                print("@",end="\t")
                #蛇头
            elif [x,y] == snake[0]:
                print("O",end="\t")
            elif [x,y] in snake[1:]:
                print("*",end="\t")
            #地图
            else:
                print(".", end="\t")

        print("#", end="")
        print()
    print("#\t"*12)


#方向
def shifting(movement,snake,food) :
    x = snake[0][0]
    y = snake[0][1]
    if movement =="上":
        y -= 1
    elif movement =="下":
        y += 1
    elif movement == "左":
        x -= 1
    elif movement == "右":
        x += 1

    snake.insert(0,[x,y])
    if food !=[x,y] :
        snake.pop()
    return snake

#撞墙
def check_wall(snake):
    x = snake[0][0]
    y = snake[0][1]
    if x > 9 or x < 0 or y > 9 or y < 0 :
        return True
    return False
#身体重合
def check_self(snake):
    x = snake[0][0]
    y = snake[0][1]
    for miao in snake[1:] :
        if [x,y]== miao :
            return True
    return False
#生成食物
def create_food(snake):
    while True :
        food=[
        random.randint(0,9),
        random.randint(0, 9)
        ]
        if food in snake:
            continue
        else:
            break
    return food

#初始化
last_movement="右"
snake = [[3, 3], [2, 3], [1, 3]]
food = create_food(snake)
score = 0 #分
while True :

    os.system("cls")
    draw_map(snake,food)
    print(f"分数:{score}")
    print("食物位置：", food)
    print(f"长度:{len(snake)}")
    movement = input("请输入方向（上、下、左、右）:")

    if movement not in ["上","下","左","右"]:
        print("输入错误，请重新输入")
        continue


    if(
        (last_movement == "右" and movement == "左")
        or(last_movement == "左" and movement == "右")
        or(last_movement == "上" and movement == "下")
        or(last_movement == "下" and movement == "上")
    ):
        print("不能直接掉头呢")
        continue

    # 控制方向
    snake = shifting(movement, snake, food)
    print(snake)

    # 检查撞墙and身体重合
    failed = check_wall(snake) or check_self(snake)

    if failed:
        print(f"游戏结束\n分数:{score}")
        break

    #生成食物
    if snake[0] == food :
        score += 10
        if len(snake) == 100:
            print(f"玩家胜利\n分数:{score}")
            break
        food = create_food(snake)


    # 更新上一次方向
    last_movement = movement





















