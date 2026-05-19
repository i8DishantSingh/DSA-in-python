def bubble_sort(arr):
    n = len(arr)
    # Outer loop for passes
    for i in range(n - 1):
        swapped = False  # Optimization: track if any swap happened
        # Inner loop for comparisons
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps happened, array is already sorted
        if not swapped:
            break
    return arr
