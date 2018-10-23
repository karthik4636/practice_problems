



def binary_search(nums,l,r,x):
    while (l<=r):
        mid = l+((r-l)//2)
        if nums[mid] ==x:
            return mid
        if nums[mid] < x:
            l = mid+1
        else:
            r = mid-1
    return -1


def binary_search_recursive(nums,l,r,x):
    if r < l:
        return -1
    mid= l + ((r-l)//2)
    if nums[mid] == x:
        return mid

    if nums[mid] < x:
        return binary_search_recursive(nums,mid+1,r,x)
    else:
        return binary_search_recursive(nums,l,mid-1,x)




arr = [ 2, 3, 4, 10, 40 ]
x = 10
c=binary_search_recursive(arr,0,len(arr)-1,x)
print(c)

