#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            pivot = nums[mid]
            if pivot >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1





s = Solution()
s.search(nums = [3,1], target = 1)
