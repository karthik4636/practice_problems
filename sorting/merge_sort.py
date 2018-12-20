#https://www.youtube.com/watch?v=Nso25TkBsYI
# there are log n steps and each element is gone through n times. SO for n
# elements run time is o(n log n)
#preferable for large datasets . Always gives O(n log n) run time but uses O(
# n) space

def merge_two_halves(arr, left, right):
    left_pointer = 0
    right_pointer = 0
    index = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            arr[index] = left[left_pointer]
            left_pointer += 1
        else:
            arr[index] = right[right_pointer]
            right_pointer += 1
        index += 1
    while left_pointer < len(left):
        arr[index] = left[left_pointer]
        index += 1
        left_pointer += 1

    while right_pointer < len(right):
        arr[index] = right[right_pointer]
        right_pointer += 1
        index += 1
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    arr = merge_two_halves(arr, left, right)
    return arr



a=merge_sort([1,6,5,-10,100,4,5,90,97,0,8,67,59,-89,-69])
print(a)