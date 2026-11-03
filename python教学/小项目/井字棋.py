import tkinter as tk



class Main:
    def __init__(self):
        self.first_X=True#先手
        self.second_Y=False#后手
        self.chess = "×"#棋子
        self.miao = []#输入坐标

        # 坐标
        self.coordinate=[[0, 0], [0, 1], [0, 2],
                         [1, 0], [1, 1], [1, 2],
                         [2, 0], [2, 1], [2, 2]]
    #地图
    def map(self):
        print("#\t" * 5)
        # 生成边框
        for y in range(0, 3):
            print("#", end="\t")
            for x in range(0, 3):
                #这里是如果遍历到输入的值就可以创建一个
                if [x,y] in self.miao :
                    if  self.first_X:
                        print("X",end="\t")
                    else:
                        print("O",end="\t")
                else:
                    print(".", end="\t")
            print("#", end="")
            print()
        print("#\t" * 5)

    def start(self):

        if self.first_X:
            print("先手输入坐标:")
            self.chess = "×"
            # 状态切换
            self.first_X,self.second_Y = False,True
        else:
            self.chess = "O"
            print("后手输入坐标:")
            # 状态切换
            self.first_X, self.second_Y = True,False
        coord = input()
        coord = int(coord)
        self.miao.append(self.coordinate[coord])
        main.map()




if __name__ == "__main__":
    main = Main()
    main.start()
    main.start()
    main.start()




































































