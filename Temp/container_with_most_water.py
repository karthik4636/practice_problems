# Python code for Max
# Water Container
def maxArea(A):
    l = 0
    r = len(A) - 1
    area = 0

    while l < r:
        # Calculating the max area
        area = max(area, min(A[l],
                             A[r]) * (r - l))

        if A[l] < A[r]:
            l += 1
        else:
            r -= 1
    return area


# Driver code
a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]

print(maxArea(a))
print(maxArea(b))
