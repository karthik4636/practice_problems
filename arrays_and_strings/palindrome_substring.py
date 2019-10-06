#https://helloacm.com/algorithms-to-count-the-number-of-palindromic-substrings/
#https://leetcode.com/problems/palindromic-substrings/
class Solution(object):
    def countSubstrings(self, S):
        count = 0
        for i in range(len(S)):
            j=i
            k=i
            while j>=0 and k<=len(S)-1 and S[j]==S[k]:
                j-=1
                k+=1
                count+=1
            j=i
            k=i+1
            while (j >= 0 and k <= len(S) - 1 and S[j] == S[k]):
                j -= 1
                k += 1
                count += 1
        return count




s = Solution()
s.countSubstrings("abba")