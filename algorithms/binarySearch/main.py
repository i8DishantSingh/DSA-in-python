
def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while(high>=low):
        mid = (low + high)//2
        if (arr[mid] == target):
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr, 5))