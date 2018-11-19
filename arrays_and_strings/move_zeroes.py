#https://leetcode.com/problems/move-zeroes/submissions/
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):

            if nums[i]!=0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero+=1



s= Solution()
s.moveZeroes([1,2,0,3,4,0])
b=1