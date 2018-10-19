
#https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for i in range(len(nums)-1,-1,-1):
                if nums[i]==val:
                    del nums[i]

        return len(nums)




s=Solution()
s.removeElement([3,2,2,3],3)
b=1