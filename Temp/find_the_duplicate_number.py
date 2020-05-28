#https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums):
        if not nums:
            return -1
        nums.sort()
        cur = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==cur:
                break
            cur = nums[i]
        return cur







s = Solution()
s.findDuplicate( [1,3,4,2,2])

