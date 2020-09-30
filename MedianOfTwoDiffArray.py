arr1 = [1, 2, 3, 4, 6, 7]
arr2 = [3, 5, 6, 8, 9, 10, 11]


def median_of_array(arr1, arr2):
    len_arr1, len_arr2 = len(arr1), len(arr2)
    total = (len_arr1 + len_arr2)
    if len_arr1 > len_arr2:
        median_of_array(arr2, arr1)
    start = 0
    end = len_arr1

    while start <= end:
        pos_x = (start + end) / 2
        pos_y = (len_arr1 + len_arr2 + 1) / 2 - pos_x
        maxL1 = arr1[pos_x - 1]
        minR1 = arr1[pos_x]
        maxL2 = arr2[pos_y - 1]
        minR2 = arr2[pos_y]

        if minR1 < maxL2 and pos_y > 0 and pos_x < len_arr1:
            start = pos_x + 1
        elif minR2 < maxL1 and pos_x > 0 and pos_y < len_arr2:
            end = pos_x - 1

        if pos_x == 0:
            pos_x -= 1
        if pos_y == 0:
            pos_y -= 1
        if minR1 <= maxL2 and minR2 <= maxL1:
            if total % 2 == 0:
                return (max(maxL1, maxL2) + min(minR1, minR2)) / 2
            else:
                return max(maxL1, maxL2)

    IOError("Enter Valid Input Array")


print(median_of_array(arr1, arr2))
