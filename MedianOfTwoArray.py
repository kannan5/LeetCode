arr1 = [1, 2, 3, 4, 6, 7]
arr2 = [3, 5, 6, 8, 9, 10]


def splitting_array(arr1, arr2, iter=0):
    if len(arr1) > len(arr2):
        return splitting_array(arr2, arr1)

    pack = object
    pos_x, pos_y = 0, 0
    arr1_len, arr2_len = len(arr1), len(arr2)
    arr_total_len = len(arr1) + len(arr2)
    if arr_total_len / 2 == 0:
        pos_x = (iter + len(arr1)) / 2
        pos_y = ((arr1_len + arr2_len + 1) - pos_x) / 2

    elif arr_total_len / 2 != 0:
        pos_x = (iter + arr1_len) / 2
        pos_y = ((arr1_len + arr2_len + 1) - pos_x) / 2

    pack.pos_x = pos_x
    pack.pos_y = pos_y
    arr1_left, arr1_right = arr1[pack.pos_x:pos_x + 1]
    arr2_left, arr2_right = arr2[pack.pos_y:pos_y + 1]

    if arr2_left > arr1_right:
        splitting_array(arr1, arr2, iter=pos_x + 1)

    if arr2_left > arr1_right:
        splitting_array(arr1, arr2, iter=pos_x + 1)

    if arr1_left <= arr2_right and arr2_left <= arr1_right:
        return

    return pack


def logic_mould(arr1, arr2):
    split_xy = splitting_array(arr1, arr2)
