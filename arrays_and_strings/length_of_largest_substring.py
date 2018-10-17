# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        last_seen = {}
        left_most=0
        longest = 0
        for index,char in enumerate(s):
            if char  in last_seen:
                left_most = max(left_most,last_seen[char]+1)
            last_seen[char] = index
            longest = max(longest,index-left_most+1)
        return longest





s = Solution()
a=s.lengthOfLongestSubstring("dvdf")
print(a)