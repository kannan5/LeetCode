import copy


class Solution:
    def countSmaller(self, nums):
        len_num = len(nums) - 2
        res, count, curr = [0] * len_num, 0, 0
        sorted_num = copy.copy(nums)
        sorted_num.sort()
        while len_num > 0:
            curr = nums[len_num]
            curr = nums.count(curr)

            len_num -= 1

        return res


if __name__ == '__main__':
    a = Solution()
    print(a.countSmaller([5, 2, 6, 1]))
    print(a.countSmaller([7, 3, 5, 2, 6, 1]))
