"""V2.2 多货物仓库机器人 · 简约 Tkinter 界面

只负责显示、地图编辑和动画调度；BFS 和多目标贪心选择仍由 V2_2机器人.MAIN 负责。

操作：
- 障碍模式：点击格子添加/删除障碍
- 起点模式：点击格子设置机器人起点
- 货物模式：点击格子添加/删除多个货物
- 开始导航：从起点重新开始一轮多货物任务

与 MAIN.bfs_run() 的状态码对应：
    111 = 已成功移动一格
    124 = 已取走一个货物，仍有其他货物
    123 = 全部货物取完
    False = 寻路或移动失败
"""

import tkinter as tk
import traceback

import ui_common as ui
from V2_2机器人 import MAIN


class Window:
    CELL = 64
    COUNT = 6
    DELAY = 500  # 每一步之间等待的毫秒数

    BG = "#F3F9F7"
    WHITE = "#FFFFFF"
    TEXT = "#21413C"
    MUTED = "#6E8983"
    GRID = "#CEE6DE"
    MINT = "#39C5BB"
    DARK_MINT = "#1A817A"
    OBSTACLE = "#3F5350"
    GOODS = "#F4C95D"

    def __init__(self):
        # 地图配置与 MAIN 的“任务执行状态”分开保存。
        # MAIN 内部会 pop 已取货物，所以必须传一份新列表给它。
        self.default_start = (0, 0)
        self.default_goods = {(1, 4), (4, 4), (5, 1)}
        self.default_obstacles = {
            (4, 2), (3, 3), (2, 3), (0, 3), (2, 5),
            (1, 1), (3, 4), (4, 5), (2, 0),
        }
        self.start_pos = self.default_start
        self.goods_positions = set(self.default_goods)
        self.obstacles = set(self.default_obstacles)

        self.is_running = False
        self.after_id = None
        self.mode = "obstacle"
        self.mode_buttons = {}

        self.ui = ui.create_window("仓库机器人 · V2.2", size=(760, 550))
        self.ui.configure(bg=self.BG)
        try:
            self.ui.iconbitmap("pigm.ico")
        except (tk.TclError, OSError):
            pass

        self.man = self._create_robot()
        self._build_ui()
        self._choose_mode("obstacle")
        self._draw_map()
        self._status("就绪 · 点击地图编辑")

    def _create_robot(self):
        """复制配置生成一轮新任务；不改变你的 MAIN 类。"""
        goods = sorted(self.goods_positions)  # 一定传 list，供 MAIN.cargo_del() 删除
        obstacles = tuple(sorted(self.obstacles))
        return MAIN(self.start_pos, goods, obstacles)

    def _label(self, text, x, y, width, height, *, size=11, color=None, bold=False):
        label = tk.Label(
            self.ui, text=text, bg=self.BG, fg=color or self.TEXT,
            font=("微软雅黑", size, "bold" if bold else "normal"),
            anchor="w",
        )
        label.place(x=x, y=y, width=width, height=height)
        return label

    def _button(self, text, x, y, width, command, *, primary=False):
        button = tk.Button(
            self.ui, text=text, command=command,
            relief="flat", bd=0,
            bg=self.DARK_MINT if primary else self.WHITE,
            fg=self.WHITE if primary else self.TEXT,
            activebackground=self.MINT, activeforeground=self.TEXT,
            font=("微软雅黑", 11), cursor="hand2",
        )
        button.place(x=x, y=y, width=width, height=42)
        return button

    def _build_ui(self):
        self._label("仓库机器人", 28, 20, 360, 35, size=19, bold=True)
        self._label("点击格子设置地图", 29, 55, 370, 24, color=self.MUTED, size=10)

        side = self.CELL * self.COUNT
        self.canvas = tk.Canvas(
            self.ui, width=side, height=side, bg=self.WHITE,
            highlightthickness=0, bd=0, cursor="hand2",
        )
        self.canvas.place(x=28, y=98)
        self.canvas.bind("<Button-1>", self._on_map_click)

        self._label("编辑模式", 447, 102, 280, 28, size=13, bold=True)
        for name, caption, y in (
                ("obstacle", "障碍（点击增删）", 144),
                ("start", "设置起点", 195),
                ("goods", "货物（点击增删）", 246),
        ):
            self.mode_buttons[name] = self._button(
                caption, 447, y, 280,
                lambda selected=name: self._choose_mode(selected),
            )

        self._button("开始导航", 447, 317, 280, self.start, primary=True)
        self._button("停止", 447, 369, 134, self.stop)
        self._button("重置", 593, 369, 134, self.reset_map)
        self._button("清空障碍", 447, 421, 134, self.clear_obstacles)
        self._button("清空货物", 593, 421, 134, self.clear_goods)

        self.info_label = self._label("", 29, 491, 405, 26, color=self.MUTED, size=10)
        self.status_label = self._label("", 447, 485, 295, 35, color=self.TEXT, size=10)

    def _choose_mode(self, mode):
        self.mode = mode
        for name, button in self.mode_buttons.items():
            selected = (name == mode)
            button.configure(
                bg=self.DARK_MINT if selected else self.WHITE,
                fg=self.WHITE if selected else self.TEXT,
            )

    def _status(self, message):
        self.status_label.configure(text=message)

    def _draw_map(self):
        """只画网格、颜色块和圆形；地图格子里不添加文字。"""
        self.canvas.delete("all")
        s = self.CELL

        for y in range(self.COUNT):
            for x in range(self.COUNT):
                self.canvas.create_rectangle(
                    x * s, y * s, (x + 1) * s - 1, (y + 1) * s - 1,
                    fill=self.WHITE, outline=self.GRID,
                )

        for x, y in sorted(self.obstacles):
            self.canvas.create_rectangle(
                x * s + 10, y * s + 10,
                (x + 1) * s - 10, (y + 1) * s - 10,
                fill=self.OBSTACLE, outline=self.OBSTACLE,
            )

        # 显示本轮尚未取走的货物，而不是总任务的初始货物。
        for x, y in self.man.goods:
            self.canvas.create_rectangle(
                x * s + 12, y * s + 12,
                (x + 1) * s - 12, (y + 1) * s - 12,
                fill=self.GOODS, outline="#C99730", width=2,
            )

        x, y = self.man.machine_x, self.man.machine_y
        cx, cy = x * s + s // 2, y * s + s // 2
        self.good_car = self.canvas.create_oval(
            cx - 22, cy - 22, cx + 22, cy + 22,
            fill=self.MINT, outline=self.DARK_MINT, width=2,
        )
        finished = len(self.goods_positions) - len(self.man.goods)
        self.info_label.configure(
            text=(f"起点 {self.start_pos}   "
                  f"货物 {finished}/{len(self.goods_positions)}   "
                  f"步数 {self.man.num_moves}")
        )

    def _restart_robot(self):
        """编辑地图之后，用新配置创建机器人；核心算法保持不变。"""
        self.man = self._create_robot()
        self._draw_map()

    def _on_map_click(self, event):
        x, y = event.x // self.CELL, event.y // self.CELL
        if not (0 <= x < self.COUNT and 0 <= y < self.COUNT):
            return
        if self.is_running:
            # V2.2 只做静态多目标贪心；动态编辑留给以后版本。
            self._status("请先停止导航再编辑")
            return

        pos = (x, y)
        if self.mode == "obstacle":
            if pos in self.obstacles:
                self.obstacles.remove(pos)
            elif pos == self.start_pos or pos in self.goods_positions:
                self._status("起点或货物位置不能放障碍")
                return
            else:
                self.obstacles.add(pos)

        elif self.mode == "start":
            if pos in self.obstacles or pos in self.goods_positions:
                self._status("起点不能与货物或障碍重合")
                return
            self.start_pos = pos

        elif self.mode == "goods":
            if pos in self.goods_positions:
                self.goods_positions.remove(pos)
            elif pos == self.start_pos or pos in self.obstacles:
                self._status("货物不能与起点或障碍重合")
                return
            else:
                self.goods_positions.add(pos)

        self._restart_robot()
        self._status("地图已更新")

    def clear_obstacles(self):
        if self.is_running:
            self._status("请先停止导航再编辑")
            return
        self.obstacles.clear()
        self._restart_robot()
        self._status("障碍已清空")

    def clear_goods(self):
        if self.is_running:
            self._status("请先停止导航再编辑")
            return
        self.goods_positions.clear()
        self._restart_robot()
        self._status("货物已清空，请添加货物")

    def reset_map(self):
        self.stop()
        self.start_pos = self.default_start
        self.goods_positions = set(self.default_goods)
        self.obstacles = set(self.default_obstacles)
        self._restart_robot()
        self._status("已恢复默认地图")

    def start(self):
        if self.is_running:
            return  # 防止连续点击创建多条 after 任务
        if not self.goods_positions:
            self._status("请先添加至少一个货物")
            return
        self._restart_robot()  # 每次启动都从所设置的起点重新执行完整任务
        self.is_running = True
        self._status("导航中…")
        self.start_run()

    def start_run(self):
        self.after_id = None
        if not self.is_running:
            return

        try:
            result = self.man.bfs_run()
        except Exception as exc:
            # 不偷偷修正你的算法。打印异常，方便继续独立调试 MAIN / BFS。
            traceback.print_exc()
            self.is_running = False
            self._status(f"算法报错：{type(exc).__name__}")
            return

        if result == 111:
            # MAIN 已更新坐标；界面只刷新显示，不额外调用 move()。
            self._draw_map()
            self.after_id = self.ui.after(self.DELAY, self.start_run)
        elif result == 124:
            # 已取走一个货物、还有货物：不移动机器人图形，只删除货物并继续。
            self._draw_map()
            self._status(f"已取货，剩余 {len(self.man.goods)} 个")
            self.after_id = self.ui.after(self.DELAY, self.start_run)
        elif result == 123:
            # 所有货物已完成：停止安排 after。
            self.is_running = False
            self._draw_map()
            self._status(f"全部完成 · 共 {self.man.num_moves} 步")
        else:
            self.is_running = False
            self._draw_map()
            self._status(f"导航停止 · {self.man.m_error()}")

    def stop(self):
        self.is_running = False
        if self.after_id is not None:
            try:
                self.ui.after_cancel(self.after_id)
            except tk.TclError:
                pass
            self.after_id = None
        self._status("已停止")


if __name__ == "__main__":
    window = Window()
    window.ui.mainloop()
