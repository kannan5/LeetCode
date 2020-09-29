
class Solution:
    def InsertInterval(self, Interval, newInterval):
        nums,mid = list(), 0
        int_len = len(Interval)
        for s,e in Interval:
            if  s < newInterval[0]:
                nums.append([s,e])
                mid += 1
            else:
                break
        if not nums or nums[-1][1] < newInterval[0]:
            nums.append(newInterval)
        else:
            nums[-1][1] = max(newInterval[1], nums[-1][1])

        for s,e in Interval[mid:]:
            if s > nums[-1][1]:
                nums.append([s,e])
            else:
                nums[-1][1] = max(nums[-1][1], e)
        return nums

if __name__ == "__main__":
    a = Solution()
    print(a.InsertInterval([[2,3],[6,9]], [5,7]))
    print(a.InsertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(a.InsertInterval([], [4,8]))

