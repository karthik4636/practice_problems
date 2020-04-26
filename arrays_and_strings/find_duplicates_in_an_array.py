#https://leetcode.com/problems/find-all-duplicates-in-an-array/


class Solution:
    def findDuplicates(self, nums):
        duplicates = []
        i = 0
        while i < len(nums):
            num = nums [i]
            j = abs(num) - 1
            if nums[j] < 0:
                duplicates.append(abs(num))
            else:
                nums[j]*= -1
            i+=1
        return duplicates



s = Solution()
s.findDuplicates([4,3,2,7,8,2,3,1])



