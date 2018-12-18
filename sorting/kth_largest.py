#https://leetcode.com/problems/kth-largest-element-in-an-array/
#use quick sort to sort
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]
