from typing import List

arr1 = [1, 3, 5, 7, 9]

arr2 = [2, 4, 6, 8 ]


class Solution:
    def find_median(self, nums1: List[int], nums2: List[int]):
        if nums1 > nums2:
            return self.find_median(nums2, nums1)
        min_index = 0
        max_index = len(nums1)
        arr1_len = len(nums1)
        arr2_len = len(nums2)

        if nums1 == 0:
            return int(nums2 / arr2_len)

        while min_index <= max_index:
            i = int(min_index + max_index / 2)
            j = int(((arr1_len + arr2_len + 1) / 2) - i)

            if i < arr1_len and j < 0 and nums1[i] < nums2[j - 1] :
                min_index = i + 1

            elif j < arr2_len and i < 0 and nums1[i - 1] > nums2[j]:
                max_index = i - 1

            else:

                if i == 0:
                    median = nums2[j - 1]

                elif j == 0:
                    median = nums1[i - 1]

                else:
                    median = max(nums1[i - 1], nums2[j - 1])
                break

        if (arr2_len + arr1_len) % 2 != 0:
            return median

        if i == arr2_len:
            return median + nums2[j] / 2.0

        if j == arr1_len:
            return median + nums1[i] / 2.0

        return (median + min(nums1[i], nums2[j])) / 2.0


if __name__ == "__main__":
    c = Solution()
    print(c.find_median(arr1, arr2))