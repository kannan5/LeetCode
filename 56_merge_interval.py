class Solution:
    def merge(self, intervals):
        res = list()
        int_len = len(intervals)
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.merge([[1, 3], [2, 6], [8, 9]]))
    print(a.merge([[1, 4], [4, 5]]))
