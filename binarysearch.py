def binary_searchiter(arr, n):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1
arr = [4, 7, 9, 16, 20, 25]
n = 25
r = binary_searchiter(arr, n)
if r != -1:
    print("Element found at index", str(r))
else:
    print("Element is not present in array")