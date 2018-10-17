#https://leetcode.com/problems/permutations/

def permute1(a, l, r):
    if l == r:
        print(a)
        return
    for i in range(l, r + 1):
        a[l], a[i] = a[i], a[l]
        permute1(a, l + 1, r)
        a[l], a[i] = a[i], a[l]


def permute(nums):
    permute1(nums, 0, len(nums) - 1)


permute([1, 2, 3])