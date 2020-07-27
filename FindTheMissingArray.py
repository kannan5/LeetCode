

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


arr2 = [3, 5, 67, 8, 9]

arr1.sort()
arr2.sort()

for x in arr1:
    if x not in arr2:
        print(x)