def mergeSort(arr:list[int]) -> list:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left:list = mergeSort(arr[:mid])
    right:list = mergeSort(arr[mid:])

    sorted_list:list = []
    i:int = 0
    j:int = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

arr = [3, 5, 6, 2, 3, 7, 2, 9]

print(mergeSort(arr))