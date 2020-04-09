#https://leetcode.com/problems/summary-ranges/
class Solution:
    def summaryRanges(self, nums):

        if not nums:
            return []
        delimiter = "->"
        out = []
        size = len(nums)
        i = 0
        tmp = []
        while i < size:
            if tmp:
                if nums[i] - tmp[-1] == 1:
                    tmp.append(nums[i])
                else:
                    if len(tmp) >= 2:
                        out.append("{}{}{}".format(tmp[0],delimiter,tmp[-1]))
                    else:
                        out.append(str(tmp[0]))
                    tmp = [nums[i]]
            else:
                tmp.append(nums[i])
            i+=1
        if len(tmp) >= 2:
            out.append("{}{}{}".format(tmp[0], delimiter, tmp[-1]))
        else:
            out.append(str(tmp[0]))
        return out











s = Solution()
s.summaryRanges([0,1,2,4,5,7])
