"""
创建一个机器人方向控制类。
机器人初始方向为北。
能够接收左转和右转指令，每次转动 90 度。
能够正确处理北、南、东、西四个方向。
统计左转次数和右转次数。
记录每次成功执行的转向操作。
输入无效指令时，不改变方向、不增加计数、不记录日志。
可以随时查看当前方向、转向次数和行动日志。
输入退出指令后，结束程序并显示最终统计结果。
#测试要求======================================================
- 至少测试 6 次有效转向。
- 左转和右转都要测试。
- 必须包含无效指令测试。
- 必须测试连续转向。
- 最后检查方向、计数器和日志是否一致。"""

class Robot:
    def __init__(self):
        self.direction = "北"
        self.dir = ["北","西","南","东"]
        self.Success={"左" : 0,"右" : 0}
        self.log = []
    def turn_left(self):
        i = self.dir.index(self.direction)
        self.direction = self.dir[(i + 1)% 4]
        self.Success["左"] += 1
        print(f"左转90度，当前位置{self.direction}")
        self.log.append(f"左转90度，当前位置:{self.direction}")
    def turn_right(self):
        i = self.dir.index(self.direction)
        self.direction = self.dir[(i - 1)% 4]
        self.Success["右"] += 1
        print(f"右转90度，当前位置{self.direction}")
        self.log.append(f"右转90度，当前位置:{self.direction}")
    def information(self):
        print("=========属性显示============")
        print(f"左转次数：{self.Success.get("左")}")
        print(f"右转次数：{self.Success.get("右")}")
        print(f"当前方向：{self.direction}")
        print("============================")
    def log_recording(self):
        i =0
        with open("10月30日日志", "w",encoding="utf-8") as f:
            for line in self.log:
                i+=1
                f.write(f"{i}. {line}\n")
    def read_log(self):
        with open("10月30日日志", "r",encoding="utf-8") as f:
            content = f.read()
            print("=========日志显示============"
            f"\n{content}"
            "============================")
r=Robot()
print("请输入:左转，右转，退出")
while True:
    s = input("输入指令喵")
    if s not in  ("左转","右转","退出"):
        print("指令错误")
        continue
    elif s == "左转":
        r.turn_left()
    elif s =="右转":
        r.turn_right()
    elif s == "退出":
        break
r.information()
r.log_recording()
r.read_log()