# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
# 使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。


class Solution():

    # 使用循环方法
    def fun_one(self, nums, k):
        for x in range(len(nums)):
            for y in range(len(nums)):
                if abs(x-y) == k and nums[x] == nums[y]:
                    return True
        return False


nums = [2, 6, 4, 5, 7, 2, 6, 4]
k = 5
a = Solution()
print(a.fun_one(nums, k))
