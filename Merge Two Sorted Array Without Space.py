


arr1 = [1,5,9,10,11,20]
arr2 = [2,3,6,7]


for i in reversed(range(len(arr1))):
    for j in range(len(arr2)):
        if(arr1[i]>arr2[j]):
            arr1[i] = arr1[i]+arr2[j]
            arr2[j] = abs(arr1[i] - arr2[j])
            arr1[i] = abs(arr1[i] - arr2[j])

arr1.sort()
arr2.sort()

#for x in range(len(arr1)):
print(arr1)

#for y in range(len(arr2)):
print(arr2)