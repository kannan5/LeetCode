class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) <4:
            return []
        res = list()
        curr = 0
        init, final = 0, (len(nums) - 1)
        while init <= final:
            low, high = (init + 1), (final - 1)
            while low < high:
                curr = nums[init] + nums[final] + nums[low] + nums[high]
                if curr == target:
                    numsList = [nums[init], nums[low], nums[high], nums[final]]
                    if numsList not in res:
                        res.append(numsList)
                if curr < target:
                    low += 1
                else:
                    high -= 1
            if curr < target:
                init += 1
            else:
                final -= 1
        return res


if __name__ == '__main__':
    nums, target = [-3,-1,0,2,4,5], 2
    a = Solution()
    print(a.fourSum(nums, target))
