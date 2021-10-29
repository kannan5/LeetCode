alphabets = [[], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"],
             ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]


class Solution:
    def letterCombinations(self, digits):
        self.dict = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
        result = [""]
        for digit in digits:
            lst = self.dict[digit]
            newresult = []
            for char in lst:
                for str in result:
                    newresult.append(str+char)
            result = newresult
        return result





if __name__ == "__main__":
    a = Solution()
    print(a.letterCombinations("239"))
