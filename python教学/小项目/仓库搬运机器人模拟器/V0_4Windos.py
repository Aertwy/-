import tkinter as tk

import ui_common as ui
from V2_2机器人 import MAIN


class Window:
    CELL = 64  # 每格 64 像素；地图共 6×6 格
    COUNT = 6
    DELAY = 500  # 自动移动的时间间隔（毫秒）

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
        self.default_start = (0, 0)
        self.default_goal = (4, 4)
        self.default_obstacles = {
            (4, 2), (3, 3), (2, 3), (0, 3), (2, 5),
            (1, 1), (3, 4), (4, 5), (2, 0),
        }
        self.start_pos = self.default_start
        self.goal_pos = self.default_goal
        self.obstacles = set(self.default_obstacles)
        self.man = MAIN(self.start_pos, self.goal_pos, tuple(sorted(self.obstacles)))

        self.is_running = False
        self.after_id = None
        self.mode = "obstacle"  # 默认点击格子即可增删障碍
        self.mode_buttons = {}

        self.ui = ui.create_window("仓库机器人", size=(760, 550))
        self.ui.configure(bg=self.BG)
        try:
            self.ui.iconbitmap("pigm.ico")
        except (tk.TclError, OSError):
            pass

        self._build_ui()
        self._choose_mode("obstacle")
        self._draw_map()
        self._status("就绪 · 点击地图编辑")

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
            self.ui, text=text, command=command, relief="flat", bd=0,
            bg=self.DARK_MINT if primary else self.WHITE,
            fg=self.WHITE if primary else self.TEXT,
            activebackground=self.MINT, activeforeground=self.TEXT,
            font=("微软雅黑", 11), cursor="hand2")
        button.place(x=x, y=y, width=width, height=42)
        return button

    def _build_ui(self):
        self._label("仓库机器人", 28, 20, 350, 35, size=19, bold=True)
        self._label("点击地图格子编辑", 29, 55, 350, 24, color=self.MUTED, size=10)

        # 只有网格和色块，不在小车、障碍、货物上绘制任何文字。
        side = self.CELL * self.COUNT
        self.canvas = tk.Canvas(
            self.ui, width=side, height=side, bg=self.WHITE,
            highlightthickness=0, bd=0, cursor="hand2",
        )
        self.canvas.place(x=28, y=98)
        self.canvas.bind("<Button-1>", self._on_map_click)

        # 右侧只有三种编辑模式；障碍模式点击一次添加、再次点击删除。
        self._label("编辑模式", 447, 102, 280, 28, size=13, bold=True)
        for name, caption, y in (
                ("obstacle", "障碍（点击增删）", 144),
                ("start", "设置起点", 195),
                ("goal", "设置货物", 246),
        ):
            self.mode_buttons[name] = self._button(
                caption, 447, y, 280,
                lambda selected=name: self._choose_mode(selected),
            )

        self._button("开始导航", 447, 317, 280, self.start, primary=True)
        self._button("停止", 447, 369, 134, self.stop)
        self._button("重置", 593, 369, 134, self.reset_map)
        self._button("清空障碍", 447, 421, 280, self.clear_obstacles)

        self.info_label = self._label("", 29, 491, 405, 26, color=self.MUTED, size=10)
        self.status_label = self._label("", 447, 485, 290, 35, size=10)

    def _choose_mode(self, mode):
        self.mode = mode
        for key, button in self.mode_buttons.items():
            active = key == mode
            button.configure(
                bg=self.DARK_MINT if active else self.WHITE,
                fg=self.WHITE if active else self.TEXT,
            )

    def _status(self, text):
        self.status_label.configure(text=text)

    def _draw_map(self):
        """全部内容统一从 MAIN 当前位置与地图配置读取。"""
        self.canvas.delete("all")
        s = self.CELL

        for y in range(self.COUNT):
            for x in range(self.COUNT):
                self.canvas.create_rectangle(
                    x * s, y * s, (x + 1) * s - 1, (y + 1) * s - 1,
                    fill=self.WHITE, outline=self.GRID,
                )

        # 深灰方块代表障碍
        for x, y in sorted(self.obstacles):
            self.canvas.create_rectangle(
                x * s + 10, y * s + 10,
                (x + 1) * s - 10, (y + 1) * s - 10,
                fill=self.OBSTACLE, outline=self.OBSTACLE,
            )

        # 黄色方块代表货物
        gx, gy = self.goal_pos
        self.canvas.create_rectangle(
            gx * s + 12, gy * s + 12,
            (gx + 1) * s - 12, (gy + 1) * s - 12,
            fill=self.GOODS, outline="#C99730", width=2,
        )

        # 青绿色圆形代表小车；没有任何车、障碍等文字。
        mx, my = self.man.machine_x, self.man.machine_y
        cx, cy = mx * s + s // 2, my * s + s // 2
        self.good_car = self.canvas.create_oval(
            cx - 22, cy - 22, cx + 22, cy + 22,
            fill=self.MINT, outline=self.DARK_MINT, width=2,
        )
        self.info_label.configure(
            text=f"起点 {self.start_pos}   货物 {self.goal_pos}   步数 {self.man.num_moves}"
        )

    def _new_robot(self):
        """创建新任务。核心算法仍全部保留在 MAIN 中。"""
        self.man = MAIN(self.start_pos, self.goal_pos, tuple(sorted(self.obstacles)))
        self._draw_map()

    def _sync_obstacles(self):
        # 运行期间改地图，下次 MAIN.bfs_run() 就能拿到新的障碍坐标。
        self.man.obstacle = tuple(sorted(self.obstacles))

    def _on_map_click(self, event):
        x, y = event.x // self.CELL, event.y // self.CELL
        if not (0 <= x < self.COUNT and 0 <= y < self.COUNT):
            return
        pos = (x, y)
        robot_pos = (self.man.machine_x, self.man.machine_y)

        if self.mode == "obstacle":
            if pos in self.obstacles:
                self.obstacles.remove(pos)
            elif pos in (self.start_pos, self.goal_pos, robot_pos):
                self._status("这里不能放障碍")
                return
            else:
                self.obstacles.add(pos)
            self._sync_obstacles()
        else:
            if self.is_running:
                self._status("请先停止导航")
                return
            if pos in self.obstacles:
                self._status("请先移除该格障碍")
                return
            if self.mode == "start":
                if pos == self.goal_pos:
                    self._status("起点不能与货物重合")
                    return
                self.start_pos = pos
            elif self.mode == "goal":
                if pos == self.start_pos:
                    self._status("货物不能与起点重合")
                    return
                self.goal_pos = pos
            self._new_robot()

        self._draw_map()
        self._status("地图已更新")

    def clear_obstacles(self):
        self.obstacles.clear()
        self._sync_obstacles()
        self._draw_map()
        self._status("障碍已清空")

    def reset_map(self):
        self.stop()
        self.start_pos = self.default_start
        self.goal_pos = self.default_goal
        self.obstacles = set(self.default_obstacles)
        self._new_robot()
        self._status("已恢复默认地图")

    def start(self):
        if self.is_running:
            return
        # 仍遵循之前版本：点击开始时从所设起点执行一趟新任务。
        self._new_robot()
        self.is_running = True
        self._status("导航中…")
        self.start_run()

    def start_run(self):
        self.after_id = None
        if not self.is_running:
            return

        result = self.man.bfs_run()  # 原有算法：123=到达，111=移动一步，False=失败
        if result == 123:
            self.is_running = False
            self._draw_map()
            self._status(f"已到达 · 共 {self.man.num_moves} 步")
        elif result == 111:
            self._draw_map()
            self.after_id = self.ui.after(self.DELAY, self.start_run)
        else:
            self.is_running = False
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
