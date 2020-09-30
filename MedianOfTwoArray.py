arr1 = [1, 2, 3, 4, 6, 7]
arr2 = [3, 5, 6, 8, 9, 10, 11]

# Python code for median with
# case of returning double
# value when even number
# of elements are present
# in both array combinely




# def to find median
# of two sorted arrays
def findMedianSortedArrays(arr1,  arr2):
    median = 0
    pos_x = 0
    pos_y = 0
    if(len(arr1) > len(arr2)):
        return findMedianSortedArrays(arr2, arr1)
    n = len(arr1)
    m = len(arr2)
    min_index = 0
    max_index = n
    while min_index <= max_index:
        pos_x = int((min_index + max_index) / 2)
        pos_y = int(((n + m + 1) / 2) - pos_x)
        if pos_x < n and pos_y > 0 and arr2[pos_y - 1] > arr1[pos_x]:
            min_index = pos_x + 1

        elif pos_x > 0 and pos_y < m and arr2[pos_y] < arr1[pos_x - 1]:
            max_index = pos_x - 1
        else:
            if pos_x == 0:
                median = arr2[pos_y - 1]

            elif pos_y == 0:
                median = arr1[pos_x - 1]
            else:
                median = max(arr1[pos_x - 1], arr2[pos_y - 1])
            break
    if (n + m) % 2 == 1:
        return median
    if pos_x == n:
        return (median + arr2[pos_y]) / 2.0

    if pos_y == m:
        return (median + arr1[pos_x]) / 2.0

    return (median + min(arr1[pos_x], arr2[pos_y])) / 2.0

# Driver code
a = [900]
b = [10, 13, 14]
# we need to define the
# smaller array as the
# first parameter to make
# sure that the time complexity
# will be O(log(min(n,m)))

print("The median is : {}".format(findMedianSortedArrays(arr1,  arr2)))
print("The median is : {}".format(findMedianSortedArrays(b, a)))


