"""v1.2
修复了一些bug
"""
import BFS


class MAIN:
    def __init__(self, machine, goods, obstacle):
        self.machine_x, self.machine_y = machine  # 机器人实际初置
        self.machine_dx, self.machine_dy = 0, 1  # 机器人方向为南方
        self.goods_x, self.goods_y = goods  # 货物放置
        self.map_x, self.map_y = 5, 5  # 地图边界
        self.obstacle = obstacle  # 障碍坐标
        self.general_log = []  # 记录日志
        self.num_moves = 0  # 移动次数
        self.history = []  # 记录重复
        self.error = ""  # 错误显示
        self.route = None  # 路线
        self.towards = {(0, -1): "北方",
                        (0, 1): "南方",
                        (1, 0): "东方",
                        (-1, 0): "西方"}

    # 移动
    def move(self):
        if self.move_error():
            self.machine_x += self.machine_dx  # 判断边界
            self.machine_y += self.machine_dy
            return True
        return False

    def move_error(self):
        # 检查边界
        if not (0 <= (self.machine_x + self.machine_dx) <= self.map_x
                and
                0 <= (self.machine_y + self.machine_dy) <= self.map_y):
            self.error = "BoundaryError"
            return False
        # 检查障碍
        for i in self.obstacle:
            obstacle_x, obstacle_y = i  # 障碍坐标
            if (self.machine_x + self.machine_dx == obstacle_x
                    and
                    self.machine_y + self.machine_dy == obstacle_y):
                self.error = "CrashObstacleError"
                return False
        return True

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
                print(line, end="")
        print("==" * 15)

    # 错误
    def m_error(self):
        if self.error == "BoundaryError":
            return "超出边界"
        elif self.error == "CrashObstacleError":
            return "撞到障碍"
        elif self.error == "RouteNotFoundError":
            return "找不到路线"
        return "无错误"

    # 寻路决策
    def decision_bfs(self):
        if len(self.route) == 1:  # 长度只有0说明可以结束了
            return False
        dx, dy = self.route.pop(1)
        # 相对方向
        direction_x, direction_y = dx - self.machine_x, dy - self.machine_y
        return direction_x, direction_y

    # =====================运行===================================

    # 运行
    def se(self):
        self.route = BFS.bfs(
            start=(self.machine_x, self.machine_y),  # 开始位置
            end=(self.goods_x, self.goods_y),  # 货物位置
            obstacle=self.obstacle,  # 障碍位置
            map_size=(self.map_x, self.map_y)  # 地图位置
        )
        while True:
            if (self.goods_x == self.machine_x  # 已经到达货物位置
                    and
                    self.goods_y == self.machine_y):
                self.record_log()
                return True
            elif self.route is not None:  # 找到路线
                # 直接赋值给方向
                direction = self.decision_bfs()
                if isinstance(direction, tuple):
                    self.machine_dx, self.machine_dy = direction[0], direction[1]
                    if self.move():
                        self.general_log.append(
                            f"方向:{self.towards[self.machine_dx, self.machine_dy]},位置:{self.machine_x, self.machine_y}")
                        self.num_moves += 1  # 移动次数
                    else:
                        return False
                else:
                    self.error = "RouteNotFoundError"
                    return False
            elif self.route is None:  # 无法找到路线
                self.error = "RouteNotFoundError"
                return False

    def run(self):
        if self.se():
            self.read_log()
            print("已到达指定位置")
        error = self.m_error()
        if error != "无错误":
            print(error)


if __name__ == "__main__":
    machine = (0, 0)  # 机器初始位置
    goods = (4, 3)  # 货物位置
    obstacle = ((4, 2), (5, 3), (3, 3))
    m = MAIN(machine, goods, obstacle)
    m.run()
