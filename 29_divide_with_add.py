class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        count = 0
        if dividend < divisor:
            return 0
        while res + divisor <= dividend:
            res += divisor
            count += 1
        return count


if __name__ == "__main__":
    c = Solution()
    print(c.divide(10, 3))
