class Solution:
    def interpret(self, command):
        if not command:
            return command
        str_list = list(command)
        len_str,i = len(str_list),0
        while i < len_str:
            if str_list[i] == "(" and i + 1 < len_str: 
                if str_list[i+1] == ")":
                    str_list[i] = "o"
                    str_list.pop(i+1)
                    len_str -= 1
            if str_list[i] == "(" and i + 3 <= len_str :
                if ''.join(str_list[i:i+4]) == "(al)":
                    str_list.pop(i)
                    str_list.pop(i+2)
                    len_str -= 3
            i+=1
        return ''.join(str_list)

if __name__ == "__main__":
    a = Solution()
    print(a.interpret("G()a(al)"))
        



