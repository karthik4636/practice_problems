#https://leetcode.com/problems/decode-string/submissions/

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.ans=""
        self.backtracking(0,s)
        return self.ans
    def backtracking(self,start,s):
        path=""
        nums=""
        i=start
        while i<len(s):
            if '0'<=s[i]<='9':
                nums+=s[i]
            elif s[i]=='[':
                index,curpath=self.backtracking(i+1,s)
                i=index
                path+=curpath*int(nums)
                nums=""
            elif s[i]==']':
                return i,path
            else:
                path+=s[i]
            i+=1
        self.ans=path