
class Solution:
    def longestPalindrome(self, s: str) -> str:
        va = ""
        max_ind = 0
        max_val = ""
        for x in range(0, len(s)):
            va = va + s[x]
            if (va == va[::-1]):
                cur_ind = len(va)
                cur_max = va
                if (cur_ind > max_ind):
                    max_val = cur_max
                    max_ind = cur_ind
            else:
                if x != (len(s) - 1):
                    if not (va[0] == s[x+1] or va[1] == s[x+1]):
                        va = s[x]
        print(max_val)

a = Solution()
res = a.longestPalindrome("asdewnn1111sdfesu")
