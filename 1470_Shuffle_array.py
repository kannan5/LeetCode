class Solution:
    def shuffle(self, nums, n):
        lenCut = 2 * n
        x, y = 0, 0
        list2, list3 = nums[:n], nums[n:]
        while x < lenCut:
            nums[x] = list2[y]
            nums[x + 1] = list3[y]
            x += 2
            y += 1
        return nums


if __name__ == '__main__':
    a = Solution()
    arr1 = [2, 5, 1, 3, 4, 7]
    print(a.shuffle(arr1, 3))
