#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.strip().lower()
        start = 0
        end = len(s) - 1
        if s=="":
            return True

        while start < end:
            if  not s[start].isalnum():
                start+=1
                continue
            if  not s[end].isalnum():
                end -= 1
                continue

            if s[start]!=s[end]:
                return False
            else:
                start+=1
                end-=1
        return True

s=Solution()
c=s.isPalindrome(".")
print(c)
