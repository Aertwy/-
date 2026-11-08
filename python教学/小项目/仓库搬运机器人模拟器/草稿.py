"""
machine_x, machine_y = 0, 5

if not (0 < machine_x < 5
        or
        0 < machine_y < 5):
    print("可以报错")
else:
    print("不可以报错")
    # 判断方向
 def direction(self):
        #判断距离
        distance_x = self.goods_x - self.machine_x
        distance_y = self.goods_y - self.machine_y
        #到达货物位置
        if (self.machine_x == self.goods_x
                and
                self.machine_y == self.goods_y):
            return True
        #Y移动
        if self.goods_y != self.machine_y:
            if distance_y >= 0:#南方
                while self.mobile_log != "南方":
                    if self.mobile_log != "东方":
                        self.turn_left()
                    else:
                        self.turn_right()
                return False
            elif distance_y < 0:#当y距离是负数
                while self.mobile_log != "北方":#当方向不为北方
                    if self.mobile_log != "东方":#当方向不为东方
                        self.turn_left()        #则左转
                    else:
                        self.turn_right()       #为东方则右转
                return False
        # X移动
        if self.goods_x != self.machine_x:
            if distance_x > 0  :
                while self.mobile_log != "东方":#当方向不为东方
                    if self.mobile_log != "北方":#当方向不为南方
                        self.turn_left()        #则左转
                    else:
                        self.turn_right()       #为南方则右转
                return False
            elif distance_x < 0:
                while self.mobile_log != "西方":#当方向不为西方
                    if self.mobile_log != "南方":#当方向不为南方
                        self.turn_left()        #则左转
                    else:
                        self.turn_right()       #为南方则右转
                return False
        self.error = "CannotDetermineError"
        return -1
    """
import tkinter as tk

root = tk.Tk()

w = tk.Canvas(root, width=200, height=100)
w.pack()

# 画一条黄色的横线
w.create_line(0, 50, 200, 50, fill="yellow")
# 画一条红色的竖线（虚线）
w.create_line(100, 0, 100, 100, fill="red", dash=(4, 4))
# 中间画一个蓝色的矩形
w.create_rectangle(50, 25, 150, 75, fill="blue")

root.mainloop()
