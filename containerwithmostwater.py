# list1 = [1, 8]
list1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]


class Solution:

    def maximum_water_outcome(self, height: list) -> int:
        x, y = 0, len(height) - 1
        final_max = 0
        while x <= y:
            if height[x] < height[y]:
                cur_max = height[x] * (y - x)
                x += 1
            else:
                cur_max = height[y] * (y - x)
                y -= 1
            if cur_max > final_max:
                final_max = cur_max
        return final_max


if __name__ == "__main__":
    s = Solution()
    print(s.maximum_water_outcome(list1))
