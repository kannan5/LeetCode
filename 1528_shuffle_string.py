import math


class Solution:

    def restoreString(self, s, indices):
        str_list, mov_index = list(s), 0
        traverse = len(indices)
        for x in range(0, traverse):
            mov_index = indices[x]
            if mov_index == x:
                continue
            str_list[mov_index] = s[x]
        return "".join(str_list)


if __name__ == '__main__':
    a = Solution()
    print(a.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
    print(a.restoreString("aiohn", [3, 1, 4, 2, 0]))
