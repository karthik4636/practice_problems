#Note we are using same array arr and not creating new arrays for merging


def merge_two_halves(arr,left, right):
    left_pointer = 0
    right_pointer = 0
    index = 0
    pass










def merge_sort(arr):
    if len(arr)<=1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_halves(arr,left,right)



