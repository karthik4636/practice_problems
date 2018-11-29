#https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum_n_3(self, nums):
        """
        o(n3) soultion
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if sum([nums[i],nums[j],nums[k]])==0:
                        print(nums[i], nums[j], nums[k])

    def threeSum(self, nums):

        nums.sort()
        r = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums)-1

            while (j<k):

               s=nums[i]+nums[j]+nums[k]

               if s > 0:
                   k-=1
               elif s < 0:
                   j+=1
               elif s == 0:
                   r.append([nums[i], nums[j], nums[k]])
                   while j < k and nums[j]==nums[j+1]:
                       j+=1
                   while j<k and nums[k] == nums[k-1]:
                       k-=1
                   j+=1
                   k-=1

        return r








s = Solution()
s.threeSum(nums = [-1, 0, 1, 2, -1, -4])