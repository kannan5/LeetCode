

class Solution:
    def missing_brackets(self, brackets):
        str_len = len(brackets)
        list1 = list(brackets)
        while str_len is not 0:
            str_len = len(list1)//2
            if 1 == len(list1):
                return list1[1] == list1[0]
            if list1[str_len] == list1[str_len + 1]:
                del list1[str_len], list1[str_len + 1]
            else:
                return False









if __name__ == '__main__':
    a = Solution()
    print(a.missing_brackets("[(])"))