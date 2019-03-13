## 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

class Solution():
    # 使用循环方法
    def fun_one(self, num):
        while True:
            num_str = str(num)
            num_list = [int(x) for x in num_str]
            num = sum(num_list)
            if num < 10:
                return num


            

    # 使用递归方法
    def fun_two(self, num):
        num_str = str(num)
        num_list = [int(x) for x in num_str]
        num = sum(num_list)
        if num < 10:
            return num
        return Solution.fun_two(self,num)
            

            
num = 22245126   
a = Solution()
print(a.fun_one(num))
print(a.fun_two(num))


