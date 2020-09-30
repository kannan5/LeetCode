class Solution:
    def maxProfit(self, prices):
        cur_max, final_max = 0, 0
        for x in range(1, len(prices)):
            cur_max += prices[x] - prices[x - 1]
            cur_max = max(0, cur_max)
            final_max = max(cur_max, final_max)
        return final_max


if __name__ == '__main__':
    a = Solution()
    print(a.maxProfit([7, 1, 5, 3, 6, 4]))
    print(a.maxProfit([]))
    print(a.maxProfit([2, 1]))
    print(a.maxProfit([3, 2, 6, 5, 0, 3]))
    print(a.maxProfit([2, 4, 1]))
    print(a.maxProfit([2, 1, 2, 1, 0, 1, 2]))
    print(a.maxProfit([2, 2, 5]))
