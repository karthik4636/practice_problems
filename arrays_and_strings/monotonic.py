#https://leetcode.com/problems/monotonic-array/

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        parity = None
        for i in range(0,len(A)-1):
            if parity is None:
                parity = self.get_parity(A, i)
            else:
                    new_parity = self.get_parity(A,i)
                    if new_parity is not None and new_parity!=parity:
                        return False
        return True

    def get_parity(self, A, i):
        if A[i] < A[i + 1]:
            return True
        if A[i] > A[i + 1]:
            return False


s = Solution()
b=s.isMonotonic([])
print(b)