
class Solution:
    def removeElement(self, nums, val):
        delCount = 0
        for i in range(0,len(nums)):
            if nums[i] == val: 
                if i < len(nums):
                    nums[i] = nums[i+1]
                    delCount += 1
                else:
                    delCount += 1
        for x in range(delCount, - 1 , -1):
            nums.pop()
        print(nums)


    def removeEl(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        nums = nums[:i]
        print(nums)
        








if __name__ == "__main__":
    a = Solution()
    # a.removeElement([22,3,4,5,6,3,3,1], 3)
    a.removeEl([22,3,4,5,6,3,3,1], 3)
    a.removeEl([2,2,1], 2)
    a.removeEl([2,2,1,5,3,4], 2)