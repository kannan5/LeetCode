import sys
class Solution:
    def find132pattern(self, nums):
        if not nums:
            return nums
        final_min = nums[0]
        min_val, max_val = nums[0], 0
        for i in range(1, len(nums)):
            curr = nums[i]
            if min_val > curr:
                min_val = curr
            else:
                if curr > max_val:
                    max_val = curr
                    final_min = min_val
                if max_val > curr and curr > final_min:
                    return True
        return False





if __name__ == "__main__":
    a = Solution()
    print(a.find132pattern([4,1,3,2]))
    print(a.find132pattern([1,0,1,-4,-3]))
    print(a.find132pattern([1,4,0,-1,-2,-3,-1,-2]))
