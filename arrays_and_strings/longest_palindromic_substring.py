#https://leetcode.com/problems/longest-palindromic-substring/solution/

class Solution:
    def longestPalindrome(self, s):
        S = s
        largest_palindrome = ""
        largest_palindrome_length = 0
        for i in range(len(S)):
            j = i
            k = i
            while j >= 0 and k <= len(S) - 1 and S[j] == S[k]:

                tmp=(S[j:k + 1])
                if len(tmp)> len(largest_palindrome):
                    largest_palindrome = tmp
                    largest_palindrome_length = len(largest_palindrome)
                j -= 1
                k += 1

            j = i
            k = i + 1
            while (j >= 0 and k <= len(S) - 1 and S[j] == S[k]):
                tmp = (S[j:k + 1])
                if len(tmp)> len(largest_palindrome):
                    largest_palindrome = tmp
                    largest_palindrome_length = len(largest_palindrome)
                j -= 1
                k += 1

        return largest_palindrome



s = Solution()
s.longestPalindrome(
"babad")