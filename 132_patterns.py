import sys
class Solution:
    def find132pattern(self, nums):
        if not nums:
            return nums
        min_val, max_val = nums[0], 0
        len_num = len(nums)
        for i in range(1, len_num -1):
            curr = nums[i]
            if min_val > curr and i != len_num -1:
                min_val = curr
            else:
                next = nums[i + 1]
                if curr > max_val:
                    max_val = curr
                if max_val > next and next > min_val:
                    return True
        return False





if __name__ == "__main__":
    a = Solution()
    print(a.find132pattern([1,0,1,-4,-3]))
    print(a.find132pattern([3,1,4,2]))
    print(a.find132pattern([1,2,3,4]))
    print(a.find132pattern([2,4,1,3]))
