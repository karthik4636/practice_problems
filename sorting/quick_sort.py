#https://www.youtube.com/watch?v=SLauY6PpjW4


def partition(arr, left, right):
    pivot = (left + right) // 2
    print(arr[left],"..",arr[right])
    print(arr[pivot])
    while left <= right:

        while arr[left] < arr[pivot]:
            left += 1

        while arr[right] > arr[pivot]:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    print(arr)
    return left


def quick_sort_helper(arr, left, right):
    if left >= right:
        return

    index = partition(arr, left, right)
    quick_sort_helper(arr, left, index - 1)
    quick_sort_helper(arr, index, right)
    return arr


def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)


a=quick_sort([10, 8, 11, 3, 4, 20])
print(a)