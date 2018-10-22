#https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle.strip()=="":
            return 0
        hay_length = len(haystack)
        needle_length= len(needle)
        for i in range(0,hay_length-needle_length+1):
            if haystack[i:i+needle_length] == needle:
                return i
        return -1



s = Solution()
b=s.strStr(haystack = "hello", needle = "m")
print(b)