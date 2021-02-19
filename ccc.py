class Solution:
    def minSteps(self, n: int):
        nops, curr = 0, 1
        if n == 1:
            return 0
        while n >0:
            if n % 2 == 0:
                n = n / 2
                nops += 2
            if n % 2 == 0:
                n = n / 2
                nops += 2
            else:


if __name__ == '__main__':
    a = Solution()
    print(a.minSteps(3))
    print(a.minSteps(5))
    print(a.minSteps(6))
