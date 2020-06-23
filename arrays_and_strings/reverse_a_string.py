#https://leetcode.com/problems/reverse-string/
#O(1) 2 pointer
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        size = len(s)
        p1 = 0
        p2 = size-1
        while p1<p2:
            s[p1],s[p2] = s[p2],s[p1]
            p1+=1
            p2-=1
        return s


s = Solution()
s.reverseString(["H","a","n","n","a","h"])

