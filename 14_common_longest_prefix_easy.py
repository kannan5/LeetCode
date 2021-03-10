class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


    def _longestCommonPrefix(self, str_val):
        if str_val:
            shortest = min(str_val, key=len)
            for i in range(len(shortest)):
                if any(word[i] != shortest[i] for word in str_val):
                    return shortest[:i]
            return shortest
        return ""

if __name__ == "__main__":
    a = Solution()
    print(a._longestCommonPrefix(['car', 'carsorva',"renso"]))