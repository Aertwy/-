"""v1.0
新增头部概念，使用向量来来求出障碍的位置，
删掉原有的4个方向控制,改为左右转来控制方向
可以稍微稍微带一点点的避障捏，OVO
"""



class MAIN:
    def __init__(self, machine, goods, obstacle):
        self.machine_x, self.machine_y = machine  # 机器人实际初置
        self.machine_dx, self.machine_dy = 0, 1  # 机器人方向为南方
        self.goods_x, self.goods_y = goods  # 货物初置
        self.map_x, self.map_y = 5, 5  # 地图边界
        self.obstacle = obstacle  # 障碍坐标
        self.mobile_log = "南方"  # 移动方向
        self.general_log = []  # 记录日志
        self.num_moves = 0  # 移动次数
        self.error = ""  # 错误显示
        self.speed = 1  # 移动速度
    # ====================移动类=============================
    # 左转
    def turn_left(self):
        self.machine_dx, self.machine_dy = self.machine_dy, -self.machine_dx
        general_log = ["南方", "东方", "北方", "西方"]
        i = general_log.index(self.mobile_log)
        self.mobile_log = general_log[(i + 1) % 4]

    # 右转
    def turn_right(self):
        self.machine_dx, self.machine_dy = -self.machine_dy, self.machine_dx
        general_log = ["南方", "西方", "北方", "东方"]
        i = general_log.index(self.mobile_log)
        self.mobile_log = general_log[(i + 1) % 4]

    # 移动
    def move(self):
        if self.move_error():
            self.machine_x += self.machine_dx  # 判断边界
            self.machine_y += self.machine_dy
            return True
        return False

    def move_error(self):
        if not (0 <= (self.machine_x + self.machine_dx) <= self.map_x
                and
                0 <= (self.machine_y + self.machine_dy) <= self.map_y):
            self.error = "BoundaryError"
            return False
        for i in self.obstacle:
            obstacle_x, obstacle_y = i  # 障碍坐标

            if (self.machine_x + self.machine_dx == obstacle_x
                    and
                    self.machine_y + self.machine_dx == obstacle_y
            ):
                self.error = "CrashObstacleError"
                return False
        return True
    # 终点决策
    def direction(self):
        # 判断距离
        distance_x = self.goods_x - self.machine_x
        distance_y = self.goods_y - self.machine_y
        # 到达货物位置
        if (self.machine_x == self.goods_x
                and
                self.machine_y == self.goods_y):
            return False
        # X移动
        if self.goods_x != self.machine_x:
            if distance_x > 0:
                while self.mobile_log != "东方":  # 当方向不为东方
                    if self.mobile_log != "北方":  # 当方向不为南方
                        self.turn_left()  # 则左转
                    else:
                        self.turn_right()  # 为南方则右转
                return True
            elif distance_x < 0:
                while self.mobile_log != "西方":  # 当方向不为西方
                    if self.mobile_log != "南方":  # 当方向不为南方
                        self.turn_left()  # 则左转
                    else:
                        self.turn_right()  # 为南方则右转
                return True
        # Y移动
        if self.goods_y != self.machine_y:
            if distance_y >= 0:  # 南方
                while self.mobile_log != "南方":
                    if self.mobile_log != "东方":
                        self.turn_left()
                    else:
                        self.turn_right()
                return True
            elif distance_y < 0:  # 当y距离是负数
                while self.mobile_log != "北方":  # 当方向不为北方
                    if self.mobile_log != "东方":  # 当方向不为东方
                        self.turn_left()  # 则左转
                    else:
                        self.turn_right()  # 为东方则右转
                return True
        self.error = "CannotDetermineError"
        return -1

    # 障碍决策
    def decide(self):
        # 判断障碍
        front_blocked, left_blocked, right_blocked = self.obstacle_avoidance()
        temp = [front_blocked, left_blocked, right_blocked]
        if temp == [True, True, True]:
            self.error = "RouteError"
            return -1
        # 前,左方有障碍，右没有障碍
        elif temp == [True, True, False]:
            self.turn_right()  # 右转
            return False
        # 前,右方有障碍，左没有障碍 或前有有障碍，左右没有
        elif temp == [True, False, True] or temp == [True, False, False]:
            self.turn_left()  # 左转
            return False
        return True

    # 避障
    def obstacle_avoidance(self):
        left_x, left_y = self.machine_dy, -self.machine_dx  # 左转位置
        right_x, right_y = -self.machine_dy, self.machine_dx  # 右转位置
        front_blocked, right_blocked, left_blocked = False, False, False
        for i in self.obstacle:  # 障碍物坐标
            obstacle_x, obstacle_y = i  # 障碍物
            vec_x = obstacle_x - self.machine_x  # 相对向量
            vec_y = obstacle_y - self.machine_y
            # 点积
            dot = {
                "front": (self.machine_dx * vec_x) + (self.machine_dy * vec_y),
                "left": (left_x * vec_x) + (left_y * vec_y),
                "right": (right_x * vec_x) + (right_y * vec_y)}
            temp = [dot["front"], dot["left"]]
            if temp == [1, 0]:  # 前方
                front_blocked = True
            elif temp == [0, -1]:  # 右边
                right_blocked = True
            elif temp == [0, 1]:  # 左边
                left_blocked = True
        return front_blocked, left_blocked, right_blocked

    # ======================数据类================================
    # 写入日志
    def record_log(self):
        # print(f"货物位置:{[self.goods_x, self.goods_y]},机器人位置:{[self.machine_x, self.machine_y]}")
        # print(f"方向:{self.mobile_log }")
        # 移动次数
        with open("../日志.txt", "w", encoding="utf-8") as f:
            for index, i in enumerate(self.general_log):
                f.write(f"{index + 1}. {i}\n")

    # 读取日志
    def read_log(self):
        print(" " * 10, "日志")
        print("==" * 15)
        print(f"移动次数:{self.num_moves}")
        with open("../日志.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                print(line)
        print("==" * 15)

    # 错误
    def m_error(self):
        if self.error == "BoundaryError":
            return "超出边界"
        elif self.error == "CannotDetermineError":
            return "direction函数判断错误"
        elif self.error == "RouteError":
            return "无路可走"
        elif self.error == "CrashObstacleError":
            return "撞到障碍"
        return "无错误"

    # =====================运行===================================
    # 运行
    def run(self):
        while True:
            direction = self.direction()  # 先找终点位置
            if not direction:  # 到终点了
                print("到达终点")
                self.record_log()
                break
            elif direction:  # 没到终点，执行避障判断
                if self.decide() != -1:
                    if self.move():
                        self.general_log.append(f"方向:{self.mobile_log},位置:{self.machine_x, self.machine_y}")
                        self.num_moves += 1  # 移动次数
            error = self.m_error()
            if error != "无错误":
                print(error)
                break


if __name__ == "__main__":
    machine = [2, 2]  # 机器初始位置
    goods = [4, 3]  # 货物位置
    obstacle = [[2, 1], [3, 3]]
    m = MAIN(machine, goods, obstacle)
    m.run()
