#  Url https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n):
        prod, sum_n, curr = 1, 0, 0
        while n != 0:
            curr = n % 10
            prod = prod * curr
            sum_n = sum_n + curr
            n = n//10
        return prod - sum_n


if __name__ == '__main__':
    a = Solution()
    print(a.subtractProductAndSum(234))

