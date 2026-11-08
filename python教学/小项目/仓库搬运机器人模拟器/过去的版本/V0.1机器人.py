"""V0.1版本
无避障，可视化界面，有即将超出边界判断，可以无障碍物的单向运输货物，带有日志
和简单寻路功能"""


class MAIN:
    def __init__(self, machine, goods):
        self.machine_x, self.machine_y = machine  # 机器人实际初置
        self.machine_dx, self.machine_dy = None, None  # 机器人方向
        self.goods_x, self.goods_y = goods  # 货物初置
        self.map_x, self.map_y = 5, 5  # 地图边界
        self.general_log = []  # 记录日志
        self.mobile_log = ""  # 移动方向
        self.num_moves = 0  # 移动次数
        self.speed = 1  # 速度
        self.error = ""  # 错误显示

    # ====================移动类=============================
    # 北方
    def north_direction(self):
        self.machine_dx, self.machine_dy = 0, -self.speed

    # 南方
    def difficult_direction(self):
        self.machine_dx, self.machine_dy = 0, self.speed

    # 西方
    def westward_direction(self):
        self.machine_dx, self.machine_dy = -self.speed, 0

    # 东方
    def eastward_direction(self):
        self.machine_dx, self.machine_dy = self.speed, 0

    # 移动
    def move(self):
        if not (0 <= (self.machine_x + self.machine_dx) <= self.map_x
                and
                0 <= (self.machine_y + self.machine_dy) <= self.map_y):
            self.error = "BoundaryError"
            return False
        else:
            # 判断边界
            self.machine_x += self.machine_dx
            self.machine_y += self.machine_dy
        return True

    # 判断方向
    def direction(self):
        # 判断距离
        distance_x = self.goods_x - self.machine_x
        distance_y = self.goods_y - self.machine_y
        # 到达货物位置
        if (self.machine_x == self.goods_x
                and
                self.machine_y == self.goods_y):
            return True
        # Y移动
        if self.goods_y != self.machine_y:
            if distance_y >= 0:  # 南方
                self.difficult_direction()
                self.mobile_log = "南方"
                return False
            elif distance_y < 0:
                self.north_direction()  # 北方
                self.mobile_log = "北方"
                return False
        # X移动
        if self.goods_x != self.machine_x:
            if distance_x > 0:
                self.eastward_direction()  # 东方
                self.mobile_log = "东方"
                return False
            elif distance_x < 0:
                self.westward_direction()  # 东方
                self.mobile_log = "西方"
                return False
        self.error = "CannotDetermineError"
        return 9

    # ======================数据类================================
    # 写入日志
    def record_log(self):
        # print(f"货物位置:{[self.goods_x, self.goods_y]},机器人位置:{[self.machine_x, self.machine_y]}")
        # print(f"距离:{[distance_x, distance_y]}")
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
        return "无错误"

    # =====================运行===================================
    # 运行
    def run(self):
        while True:
            direction = self.direction()
            error = self.m_error()
            if error == "无错误":
                if direction == 9:
                    break
                elif not direction:
                    if not self.move():  # 移动完成后记录日志和次数
                        continue
                    else:
                        self.general_log.append(f"方向:{self.mobile_log},位置:{self.machine_x, self.machine_y}")
                        self.num_moves += 1  # 移动次数
                elif direction:
                    self.record_log()  # 写入日志
                    self.read_log()  # 读取日志
                    print("到达货物位置")
                    break
            else:
                print(f"因为:{error}停止了")
                return False


if __name__ == "__main__":
    machine = [2, 2]  # 机器初始位置
    goods = [0, 0]  # 货物位置
    m = MAIN(machine, goods)
    m.run()

"""
"左上":[0,0],"右上":[0,5],
"左下": [0,5],"右下":[5,5]
"""
