

def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i,j,k = 0,0,0

        while i< len(left_arr) and j< len(left_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        
        while i< len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1

        while j< len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
        return arr
    
    

def subarray(arr):
    max_val = arr[0]
    cur_max = arr[0]
    for i in range(1, len(arr)):
        cur_max = max(arr[i], cur_max+arr[i])

        if max_val < cur_max:
            max_val = max(cur_max, max_val)
    return max_val


if __name__  == "__main__":
    # print(merge_sort([2,3,1,4,5]))
    print(subarray([-2, -3, 4, -1, -2, 1, 5, -3]))