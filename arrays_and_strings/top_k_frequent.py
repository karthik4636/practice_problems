#https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] +=1

        d1 = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        b = []
        for key, value in d1:
            if k <=0:
                break
            b.append(key)
            k-=1
        return sorted(b)






s = Solution()
s.topKFrequent( nums = [4,1,-1,2,-1,2,3], k = 2)

