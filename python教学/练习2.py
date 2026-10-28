class Solution:
    def __init__(self,su1,su2):
        self.su1=su1
        self.su2=su2

    def solve(self):
        print(self.su1+self.su2)

    def solve2(self):
        print(self.su1*self.su2)

    def solve3(self):
        print(self.su1-self.su2)

sol=Solution(10,10)
sol.solve()
sol.solve2()
sol.solve3()