"""v2.1
加上了如果要用窗口可以自动计算路线
"""
import BFS


class MAIN:
    def __init__(self, machine, goods, obstacle):
        self.machine_x, self.machine_y = machine  # 机器人实际初置
        self.machine_dx, self.machine_dy = 0, 1  # 机器人方向为南方
        self.goods = goods
        self.goods_x, self.goods_y = None, None  # 货物放置
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
        # 检查地图边界
        if not (0 <= (self.machine_x + self.machine_dx) <= self.map_x
                and
                0 <= (self.machine_y + self.machine_dy) <= self.map_y):
            self.error = "BoundaryError"
            return False
        # 检查障碍边界
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

    # 取货路线d=|x2-x1|+|y2-y1|
    def cargo(self):
        i = 0
        if self.goods_x is None and self.goods_y is None:
            for subscript, coordinate in enumerate(self.goods):
                route = BFS.bfs(
                    start=(self.machine_x, self.machine_y),  # 开始位置
                    end=(coordinate[0], coordinate[1]),  # 货物位置
                    obstacle=self.obstacle,  # 障碍位置
                    map_size=(self.map_x, self.map_y)  # 地图位置
                )
                if route is None:  # 如果都被挡住了i+1
                    i += 1
                    if len(self.goods) == i:  # 如果货物的长度和i相等，说明全被围住了，不可以继续了
                        self.error = "RouteNotFoundError"
                        return False
                    else:
                        continue
                elif subscript == 0:
                    key = len(route)
                    add = subscript
                    i = 0
                else:
                    if key > len(route):
                        key = len(route)
                        add = subscript
                        i = 0
                # 最近的路线
            self.goods_x, self.goods_y = self.goods[add]
            return True
        else:
            return False

    # 删除坐标
    def cargo_del(self):
        for subscript, coordinate in enumerate(self.goods):
            if coordinate[0] == self.goods_x and coordinate[1] == self.goods_y:
                self.goods.pop(subscript)
                self.goods_x, self.goods_y = None, None
                return True
        return False

    # 窗口运行
    def bfs_run(self):
        self.cargo()
        self.route = BFS.bfs(
            start=(self.machine_x, self.machine_y),  # 开始位置
            end=(self.goods_x, self.goods_y),  # 货物位置
            obstacle=self.obstacle,  # 障碍位置
            map_size=(self.map_x, self.map_y)  # 地图位置
        )

        # 判断是否到达终点
        if (self.goods_x == self.machine_x  # 已经到达货物位置
                and
                self.goods_y == self.machine_y):
            self.cargo_del()
            if self.goods:
                return 124  # 还有坐标
            else:
                self.record_log()
                return 123  # 没有坐标了
        # 找到路线
        elif self.route is not None:
            # 直接赋值给方向
            direction = self.decision_bfs()
            if isinstance(direction, tuple):
                self.machine_dx, self.machine_dy = direction[0], direction[1]
                if self.move():
                    self.general_log.append(
                        f"方向:{self.towards[self.machine_dx, self.machine_dy]},位置:{self.machine_x, self.machine_y}")
                    self.num_moves += 1  # 移动次数
                    return 111
                else:
                    return False
            else:
                self.error = "RouteNotFoundError"
                return False
        elif self.route is None:  # 无法找到路线
            self.error = "RouteNotFoundError"
            return False

    # =====================自身运行===================================
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
    # =======man函数调用==========
    machine = (2, 2)  # 机器初始位置
    goods = [(0, 0), (2, 3), (5, 5)]  # 货物位置
    obstacle = ((4, 2), (5, 3), (3, 3))
    man = MAIN(machine, goods, obstacle)
    man.cargo()
