#https://www.youtube.com/watch?v=6Gv8vg0kcHc
#best case : O(n)
#worst case : O(n^2)

def bubble_sort(arr):
    last_unsorted_index = len(arr) - 1
    sorted= False
    while sorted is False:
        sorted = True
        for i in range(0,last_unsorted_index):
            if arr[i]> arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        last_unsorted_index-=1
    return arr




a = bubble_sort([1,1,3,2])
print(a)












