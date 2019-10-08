#https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums, k):
        l={}
        l[0] = 1
        sum=0
        ans = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in l:
                ans+= l[sum-k]
            if sum in l:
                l[sum]+=1
            else:
                l[sum] = 1
        return ans







s = Solution()
s.subarraySum(nums = [1,1,1], k = 2)

