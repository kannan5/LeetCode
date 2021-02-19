str_pair = "{[]}]"


from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}", "[": "]", "(": ")"}
        list_str, len_str = deque(), len(s)
        if len_str % 2 != 0:
            return False
        for x in range(0, len_str):
            if len(list_str) == 0:
                list_str.append(s[x])
                continue
            curr = s[x]
            try:
                if pairs[list_str[-1]] == curr:
                    list_str.pop()
                else:
                    list_str.append(s[x])
            except KeyError:
                return False
        return len(list_str) == 0


if __name__ == '__main__':
    a = Solution()
    print(a.isValid(str_pair))
    print(a.isValid("()[]{}"))
    print(a.isValid("([)]"))
    print(a.isValid("({[)"))
