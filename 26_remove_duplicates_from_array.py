class Solution:
    def removeDuplicates(self, nums):
        move = 1
        for i in range(len(nums)-2,-1,-1):
            prev,curr = nums[i+1], nums[i]
            if prev == curr:
                if i >= 1 and curr == nums[i - 1]:
                    move += 1
                    continue
                else:
                    for j in range(i+1, len(nums)-move):
                        nums[j] = nums[j+move]
                    nums = nums[:-move]
                    move = 1
        print(nums)
        return len(nums)


    def removeDuplicatesA(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]
        for j in range(newTail+1, len(A)):
            A.pop()
        return newTail + 2







if __name__ == "__main__":
    a  = Solution()
    a.removeDuplicatesA([0,0,1,1,1,2,2,3,3,4])
