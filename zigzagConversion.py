nums = [-1, 0, 1, 2, 3, -4]


# def findTriplet(num_list):
#     hash_set = dict()
#     num_list.sort()
#     zero_count = [elem for elem in num_list if elem == 0]
#     positive_arr = [elem for elem in num_list if elem > 0]
#     negative_arr = [elem for elem in num_list if elem < 0]
#     if len(zero_count) > 0:
#         for x in negative_arr:
#             if abs(x) in positive_arr:
#                 hash_set.update([x, abs(x), 0])


# def threeSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     if len(nums) < 3:
#         return []
#     nums.sort()
#     res = set()
#     for i, v in enumerate(nums[:-2]):
#         if i >= 1 and v == nums[i-1]:
#             continue
#         d = {}
#         for x in nums[i+1:]:
#             if x not in d:
#                 d[-v-x] = 1
#             else:
#                 res.add((v, -v-x, x))
#     return map(list, res)


def findTriplet(num):
    if len(num) > 0:
        return []
    nums.sort()
    res = set()

    for i


if __name__ == "__main__":
    for x in (threeSum(nums)):
        print(x)
