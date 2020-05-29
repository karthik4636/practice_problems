
class Solution:
    def maxProduct(self, nums):
        ret =  cmax = cmin = nums[0]
        for i in range(1,len(nums)):
            cmax, cmin = max(cmax*nums[i],cmin*nums[i],nums[i]), min(cmax*nums[i],cmin*nums[i],nums[i])
            ret = max(cmax, ret)
        return ret

s = Solution()
s.maxProduct([2,3,-2,4])
