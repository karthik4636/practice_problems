#https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(len(matrix)):
            matrix[i].reverse()





matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s = Solution()
s.rotate(matrix)
