# https://leetcode.com/problems/top-k-frequent-elements/
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
                freq[i] += 1

        d1 = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        b = []
        for key, value in d1:
            if k <= 0:
                break
            b.append(key)
            k -= 1
        return sorted(b)

    def bucket_sort(self, nums):
        hashmap = {}

        # buckets
        buckets = [[] for i in range(len(nums) + 1)]

        # record the num of instances of occurrence for each number
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # add hashmap entries according to frequencies to freq-array
        # index = frequency
        for number, frequency in hashmap.items():
            buckets[frequency].append(number)

        res = []

        i = len(buckets) - 1

        while i > 0 and len(res) < k:
            res.extend(buckets[i])
            i -= 1

        return res


s = Solution()
s.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2)

