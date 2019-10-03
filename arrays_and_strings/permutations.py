#https://leetcode.com/problems/permutations/solution/
class Solution:

    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        perms = []
        for i in range(len(nums)):
            element = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for p in self.permute(remaining):
                p.append(element)
                perms.append(p)
        return perms






s = Solution()
a=s.permute([1,2,3])
b=1
