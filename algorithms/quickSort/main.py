def partition(arr, low, high):
    pivot = arr[high]  # choose last element as pivot
    i = low - 1        # index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)  # partition index
        quick_sort(arr, low, p - 1)    # sort left subarray
        quick_sort(arr, p + 1, high)   # sort right subarray

# Example usage
numbers = [10, 7, 8, 9, 1, 5]
print("Original:", numbers)
quick_sort(numbers, 0, len(numbers) - 1)
print("Sorted:", numbers)
