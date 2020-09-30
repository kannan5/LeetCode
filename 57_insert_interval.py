# class Solution:
#     def insert(self, intervals, newInterval):
#         count, new_ind = 0, 0
#         len_int, x = len(intervals), 0
#         if len_int == 0:
#             return newInterval
#         while x < len_int:
#             new_int_val = newInterval[new_ind]
#             if intervals[x][0] > new_int_val:
#                 if intervals[x - 1][1] < new_int_val:
#                     intervals[x - 1][1] = new_int_val
#                 else:
#                     intervals[x][0] = new_int_val
#                 new_int_val += 1
#             if new_int_val == 2:
#                 x = len_int
#             x += 1
#         return intervals


class Solution:
    def insert(self, intervals, newInterval):
        output = []
        mid = 0
        for s, e in intervals:
            if s < newInterval[0]:
                output.append([s, e])
                mid += 1
            else:
                break
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], newInterval[1])

        for s, e in intervals[mid:]:
            if output[-1][1] < s:
                output.append([s, e])
            else:
                output[-1][1] = max(output[-1][1], e)
        return output


if __name__ == '__main__':
    a = Solution()
    print(a.insert([[1, 3], [6, 9]], [5, 7]))
