import copy
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_list = copy.copy(nums)
        sorted_list.sort()
        res = list()
        for x in nums:
            res.append(sorted_list.index(x))
        return res









if __name__ == '__main__':
    a = Solution()
    print(a.smallerNumbersThanCurrent([8,1,2,2,3]))

