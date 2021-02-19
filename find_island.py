class Solution:
    def visit_island(self, row, col):
        pass

    def find_island(self, arr1):
        count = 0
        if not arr1:
            return count
        height = len(arr1)
        if type(arr1[0]) is not list:
            for x in arr1:
                if x == 1:
                    count +=1
            return count

        width = len(arr1[0])
        for i in range(height):
            for j in range(width):
                if arr1[i][j] == 1:
                    count  += 1
                    # self.visit_island(i, j)
        return count


if __name__ == '__main__':
    a = Solution()
    print(a.find_island([0]))
    print(a.find_island([1]))
    print(a.find_island([[0, 1], [1,0]]))
    print(a.find_island([[0, 1], [1,0]]))
    print(a.find_island([[0, 0, 0, 1], [0,1,0,1], [0,1,0,1], [0,0,0,1]]))
