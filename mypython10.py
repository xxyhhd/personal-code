# 编写一个程序判断给定的数是否为丑数。
# 丑数就是只包含质因数 2, 3, 5 的正整数
import time
class Solution():

    def __init__(self, num):
        self.num = num

    def fun_one(self, num):
        for x in [2,3,5]:
            if self.num % x == 0:
                self.num /= x
                Solution.fun_one(self,num)
            if self.num == 1:
                return True
        return False


num = int(input())
a = Solution(num)
start = time.clock()
print(a.fun_one(num))
end = time.clock()
print(end-start)





