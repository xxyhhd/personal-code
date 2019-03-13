##给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
##找出那个只出现了一次的元素。

class Solution():
    # 使用列表的count方法
    def fun_one(self, list1):     
        for x in list1:
            if list1.count(x) == 1:
                return x
                break

    # 使用异或方法，相同为0，不同为1
    def fun_two(self, list1):
        a = 0
        for x in list1:
##            相当于用0和列表中的每一个元素同时进行异或，相等的两个元素异或等于1，
##            最后只剩下0^当个元素
            a = a^x
        return a

            
list1 = [5,2,5,3,4,2,4]    
a = Solution()
print(a.fun_one(list1))
print(a.fun_two(list1))


