import tkinter as tk

import BFS
import ui_common as ui
from V2_0机器人 import MAIN


class Window:
    def __init__(self):
        self.is_running = False  # 状态
        self.ui = ui.create_window("避障小车(～￣▽￣)～", size=(600, 600))
        text = ui.label(self.ui, "避障小车", x=250, y=0, font=("微软雅黑", 17))
        try:
            self.ui.iconbitmap('pigm.ico')
        except tk.TclError:
            pass
            # 函数调用=============================
        machine = (0, 0)  # 机器初始位置
        goods = (4, 4)  # 货物位置
        # 障碍模板设置，蛇形：(0,1),(1,1),(2,1),(3,1),(4,1),(1,3),(2,3),(3,3),(4,3),(5,3)
        # 正常:(4, 2),(3, 3),(2,3),(0,3),(2,5),(1,1),(3,4),(4,5),(2,0)
        obstacle = ((4, 2), (3, 3), (2, 3), (0, 3), (2, 5), (1, 1), (3, 4), (4, 5), (2, 0))  # 障碍物
        self.man = MAIN(machine, goods, obstacle)
        # 货物位置
        goods_x, goods_y = self.man.goods_x, self.man.goods_y
        # 小车位置
        actual_machine_x, actual_machine_y = self.man.machine_x, self.man.machine_y
        # 障碍位置
        obstacle = self.man.obstacle
        # 地图=================================
        self.canvas = tk.Canvas(self.ui, width=360, height=360,
                                bg="#EFFBF8",
                                highlightthickness=0, bd=0)
        for i in range(6):
            for j in range(6):
                x1 = i * 60
                y1 = j * 60
                x2 = x1 + 60
                y2 = y1 + 60
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="#4CC38A")
        self.canvas.place(x=120, y=100)
        # 小车===================================
        # 圆心
        center_x = actual_machine_x * 60 + 30
        center_y = actual_machine_y * 60 + 30
        radius = 20  # 半径
        # 边界
        self.good_car = self.canvas.create_oval(center_x - radius,  # 左
                                                center_y - radius,  # 上
                                                center_x + radius,  # 右
                                                center_y + radius,  # 下
                                                fill="#39C5BB", outline="#1F8C85", width=2)
        # 障碍位置====================================
        obstacle_half_size = 25  # 矩形半径
        for i in obstacle:
            obstacle_x, obstacle_y = i
            obstacle_x = obstacle_x * 60 + 30
            obstacle_y = obstacle_y * 60 + 30
            self.canvas.create_rectangle(obstacle_x - obstacle_half_size,  # 左
                                         obstacle_y - obstacle_half_size,  # 上
                                         obstacle_x + obstacle_half_size,  # 右
                                         obstacle_y + obstacle_half_size,  # 下
                                         fill="#3F5350", width=2)
        # 货物位置====================================
        goods_x = goods_x * 60 + 30
        goods_y = goods_y * 60 + 30
        self.canvas.create_rectangle(goods_x - obstacle_half_size,  # 左
                                     goods_y - obstacle_half_size,  # 上
                                     goods_x + obstacle_half_size,  # 右
                                     goods_y + obstacle_half_size,  # 下
                                     fill="#F4C95D",
                                     outline="#C99730",
                                     width=2)
        # 启动按钮=====================================
        self.start_button = ui.button(self.ui, "启动",
                                      x=230, y=480, width=150, height=50,
                                      command=self.start, font=("微软雅黑", 17))

    def start(self):
        if not self.is_running:
            self.man.route = BFS.bfs(
                start=(self.man.machine_x, self.man.machine_y),  # 开始位置
                end=(self.man.goods_x, self.man.goods_y),  # 货物位置
                obstacle=self.man.obstacle,  # 障碍位置
                map_size=(self.man.map_x, self.man.map_y))  # 地图位置
            if (self.man.goods_x == self.man.machine_x  # 已经到达货物位置
                    and
                    self.man.goods_y == self.man.machine_y):
                self.is_running = False
                self.man.record_log()
                return True
            elif self.man.route is not None:
                self.is_running = True
                self.move_step()
            elif self.man.route is None:  # 无法找到路线
                print("找不到路")
                self.man.error = "RouteNotFoundError"
                self.is_running = False
                return False

    def move_step(self):
        direction = self.man.decision_bfs()
        if isinstance(direction, tuple):
            self.man.machine_dx, self.man.machine_dy = direction[0], direction[1]
            if self.man.move():
                self.canvas.move(self.good_car, self.man.machine_dx * 60, self.man.machine_dy * 60)
                self.man.general_log.append(
                    f"方向:{self.man.towards[self.man.machine_dx, self.man.machine_dy]},位置:{self.man.machine_x, self.man.machine_y}")
                self.man.num_moves += 1  # 移动次数
            else:
                self.is_running = False
                return False
        else:
            self.man.error = "RouteNotFoundError"
            self.is_running = False
            return False
        if (self.man.goods_x == self.man.machine_x  # 已经到达货物位置
                and
                self.man.goods_y == self.man.machine_y):
            self.man.record_log()
            print("到达货物位置！")
            self.is_running = False
            return True
        else:
            self.ui.after(500, self.move_step)


if __name__ == "__main__":
    window = Window()
    window.ui.mainloop()
