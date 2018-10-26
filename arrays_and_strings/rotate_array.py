#https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        k = k % len(nums)
        nums[0:len(nums) - k],nums[len(nums)-k:len(nums)] = nums[len(
            nums)-k:len(nums)],nums[0:len(nums) - k]





s = Solution()
s.rotate([1,2,3,4,5,6,7]
,3)