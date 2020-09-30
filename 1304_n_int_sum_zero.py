class Solution:
    def sumZero(self, n: int):
        x, y,xsum = 1, -1, n //2
        res_list = list()
        while x <= xsum:
            res_list.append(x)
            x += 1
        while len(res_list) != n:
            res_list.append(-xsum)
            xsum -= 1
        return res_list


if __name__ == '__main__':
    a = Solution()
    print(a.sumZero(1))
