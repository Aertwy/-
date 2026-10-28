#主程序
class PatrolRobot:
    def __init__(self):
        self.history = []#日志
        self.status = "待机"
        self.obstacle = False
        self.start_count = 0  # 启动次数
        self.stop_count = 0   # 停止次数
        self.direction = "北" #机器人面朝方向
        self.has_turned = False #重复转向
        self.search_count = 0 #搜索次数
        self.saved_count = 0 #保存数
        print(f"机器人初始化:{self.status}")
        print("======= 开始运行喵 =======")
    #巡逻模式
    def start_patrol(self):
        self.status = "巡逻中"
        print(f"机器人启动:{self.status}")
        #日志
        self.history.append(f"机器人启动：{self.status}")
    #停止模式
    def stop(self):
        self.status = "停止"
        print(f"机器人停止:{self.status}")
        self.history.append(f"机器人停止：{self.status}")
    #是否有障碍
    def detect_obstacle(self, obstacle):
        if obstacle :
            self.obstacle = True
            return True

        else:
            self.obstacle = False
            print("前方安全，可以前进！")
            return False
    # 检测障碍
    def auto_move(self,front_obstacle,left_obstacle,right_obstacle):
        front_obstacle = self.detect_obstacle(front_obstacle)
        if  front_obstacle  :
            if self.status != "停止":
                print("检测到障碍物！")
                self.stop_count += 1
                self.stop()
            if not self.has_turned:
                # 左边无障碍就左转
                if not left_obstacle:
                    self.turn_left()
                    self.has_turned = True
                # 右边无障碍就右转
                elif not right_obstacle:
                    self.turn_right()
                    self.has_turned = True
                else:
                    print("左侧和右侧都有障碍物，暂时无法转向喵！")
        #前方无障碍复位
        else:
            self.has_turned = False
            if self.status != "巡逻中" :
                self.start_count +=1
                self.start_patrol()
    #左转喵
    def  turn_left(self):

        if  self.direction == "北":
            self.direction = "西"

        elif self.direction == "西":
            self.direction = "南"

        elif self.direction == "南":
            self.direction = "东"

        elif self.direction == "东":
            self.direction = "北"
        print(f"左转90度喵，方向:{self.direction}")
        self.history.append(f"左转90度，当前方向：{self.direction}")
    #右转喵
    def turn_right(self):
        if  self.direction == "北":
            self.direction = "东"

        elif self.direction == "西":
            self.direction = "北"

        elif self.direction == "南":
            self.direction = "西"

        elif self.direction == "东":
            self.direction = "南"
        print(f"右转90度喵，方向:{self.direction}")
        self.history.append(f"右转90度，当前方向：{self.direction}")
    #设置障碍
    def run_patrol(self, sensor_data):
        for i in sensor_data:
            self.auto_move(i[0],i[1],i[2])
    #状态管理
    def show_status(self):
        print(f"当前运行状态：{self.status}")
        print(f"当前方向：{self.direction}")
        print(f"是否已经转向：{self.has_turned}")
        print(f"启动次数：{self.start_count}")
        print(f"停止次数：{self.stop_count}")
        print(f"查找有效次数：{self.search_count}")
    #日志管理
    def show_history(self):
        print("===== 机器人行动日志 =====")
        #enumerate编号
        for num,i in enumerate(self.history,1):
            print(f"{num}. {i}")
        if not self.history:
            print("暂无行动日志喵！")
    #最近三条日志
    def show_recent_history(self):
        print("===== 机器人近三条行动日志 =====")
        for num,i in enumerate(self.history[-3:],1):
            print(f"{num}. {i}")
    #清除日志喵
    def clear_history(self):
        self.history.clear()
        print("已清除所有日志喵！")
    #统计日志数量
    def show_history_count(self):
        print(f"===当前日志数量为{len(self.history)}===")
    #统计数量
    def count_turns(self):
        zi = 0
        yi = 0

        for i in self.history:
            if "左转" in i:
                zi += 1
            elif "右转" in i :
                yi += 1
        print("======方向切换次数喵======")
        print(f"左转次数:{zi}"
            f"\n右转次数:{yi}")
    #显示最后日志
    def show_last_action(self):
        print("=======最后一个日志=======")
        if self.history:
            print(self.history[-1])
        else:
            print("机器人还没有行动记录喵！")
    #查找日志
    def search_history(self):
        t1 = 0
        keyword = input("请输入想要查找的文字喵:").strip()
        if keyword != "":
            print("======正在查找======")
            for i, num in enumerate(self.history, 1):
                if keyword in num:
                    t1 += 1
                    print(f"{i}. {num}")
            if t1 == 0:
                print(f"找不到{keyword}喵！")
            else:
                print(f"找到{t1}条日志喵")
            self.search_count+=1
        else:
            print("输入不能为空喵")
    #写入日志
    def save_log (self):
        t = 0
        with open("日志文件.txt", "w", encoding="utf-8") as f:
            for log in self.history:
                t +=1
                f.write(f"{t}. {log}\n")

            print("-"*15,"\n日志保存成功!")
            print("-"*15)
    # 读取保存的日志
    def read_log(self):
        #try尝试执行可能发生异常的代码
        try:
            with open("日志文件.txt", "r", encoding="utf-8") as f:
                content = f.read()
                self.history.clear()
                if content !="":
                    print("========读取日志========="
                        f"\n{content}\n"
                        "========读取结束=========")
                    #存入日志
                    for i in content.splitlines():
                        log = i.split(". ", 1)
                        #长度为2，且第一个为数字则去掉数字存到日志里
                        if len(log) == 2 and log[0].isdigit():
                            self.history.append(log[1])
                        # 没有有效数字编号时，保留原始日志
                        else:
                            self.history.append(i)

                else:
                    print("日志为空喵！")
        #except抛出并处理异常
        except FileNotFoundError :
            print("错误！找不到该文件喵")
        except PermissionError:
            print("错误！无权限读取该文件喵")
        else:
            print("读取成功喵！")
        #无论有没用都执行finally下
        finally:
            print("-" * 20)
            print("日志读取操作结束喵!")
            print("-" * 20)


r1 = PatrolRobot()
#前面障碍，左边障碍，右边障碍














