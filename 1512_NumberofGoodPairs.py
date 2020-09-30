class Solution:
    def numIdenticalPairs(self, nums):
        res = 0
        hashmap = dict()
        for x in nums:
            hashmap[x] = hashmap.get(x, 0) + 1
        for x, y in hashmap.items():
            if y == 1:
                continue
            else:
                res += (y * (y - 1) // 2)
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(a.numIdenticalPairs([1, 1, 1, 1]))
    print(a.numIdenticalPairs([1,5,3,2,4,2,5,2,2,6,6,2,4,4,5,1,5]))
