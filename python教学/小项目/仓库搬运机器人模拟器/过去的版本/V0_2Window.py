import tkinter as tk

import ui_common as ui

from V2_1机器人 import MAIN


# v0,2加上了动态避障，走一步算一步，并且分开了运算，但是没加动态按钮了
# 但是我打算界面直接用ai写了，我主要去研究避障之类的，，，
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
        obstacle = ((0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3))  # 障碍物
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
            self.start_run()

    def start_run(self):
        self.is_running = True
        bfs_run = self.man.bfs_run()
        if bfs_run == 123:
            print("已到达终点位置")
            self.is_running = False
        elif not bfs_run:
            print("错误")
            print(self.man.m_error())
            self.is_running = False
        elif bfs_run == 111:
            self.canvas.move(self.good_car, self.man.machine_dx * 60, self.man.machine_dy * 60)
            self.ui.after(500, self.start_run)


if __name__ == "__main__":
    window = Window()
    window.ui.mainloop()
