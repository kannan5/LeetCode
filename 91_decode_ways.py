import time


class Solution:
    def decode_ways(self, arr, type=0):
        if not arr or arr[0] is "0":
            return 0
        if type == 0:
            return self._decode_ways_rec(arr, len(arr) - 1)
        if type == 1:
            dp = [-1 for _ in range(0, len(arr))]
            return self._decode_ways_dp_down(arr, len(arr) - 1, dp)

    def _decode_ways_rec(self, arr, w_len):
        if w_len <= 0:
            return 1
        ways = 0
        if arr[w_len - 1] is "1" or (arr[w_len - 1] is "2" and int(arr[w_len]) < 7):
            if arr[w_len] is "0":
                ways += self._decode_ways_rec(arr, w_len - 2)
            else:
                ways += self._decode_ways_rec(arr, w_len - 1) + self._decode_ways_rec(arr, w_len - 2)
        else:
            ways += self._decode_ways_rec(arr, w_len - 1)
        return ways

    def _decode_ways_dp_down(self, arr, w_len, dp):
        if w_len >= 0 and dp[w_len] is not -1:
            return dp[w_len]

        if w_len <= 0:
            return 1

        ways = 0
        if arr[w_len] is "0" and (arr[w_len - 1] is "0" or int(arr[w_len - 1])>2):
            return 0
        if arr[w_len - 1] is "1" or (arr[w_len - 1] is "2" and int(arr[w_len]) < 7):
            if arr[w_len] is "0":
                ways += self._decode_ways_dp_down(arr, w_len - 2, dp)
            else:
                ways += self._decode_ways_dp_down(arr, w_len - 1, dp) + self._decode_ways_dp_down(arr, w_len - 2, dp)
        else:
            ways += self._decode_ways_dp_down(arr, w_len - 1, dp)
        dp[w_len] = ways

        return ways

    def decode_str(self, str_num):
        l = len(str_num)
        count = 0
        if not str_num:
            return 0
        num_len = l - 1
        while num_len >0:
            if str_num[num_len] is "0":
                if int(str_num[num_len - 1]) > 2:
                    return 0
                else:
                    count += 1
                num_len -= 1
            else:
                count += 2
                num_len -= 2
        return count










if __name__ == "__main__":
    a = Solution()
    t = time.time()
    print(a.decode_ways("11210"))
    print(a.decode_ways("0212"))
    print(a.decode_ways("1253"))
    print(a.decode_ways("11106"))
    print(a.decode_ways("226"))
    print(time.time() - t)
    # print("Here Comes DP-- ")
    # t = time.time()
    # print(a.decode_ways("11210", 1))
    # print(a.decode_ways("0212", 1))
    # print(a.decode_ways("1253", 1))
    # print(a.decode_ways("11106", 1))
    # print(a.decode_ways("226", 1))
    # print(time.time() - t)
    print(a.decode_str("11210"))
    print(a.decode_str("0212"))
    print(a.decode_str("1253"))
    print(a.decode_str("11106"))
    print(a.decode_str("226"))