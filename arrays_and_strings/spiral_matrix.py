#https://leetcode.com/problems/spiral-matrix/submissions/
class Solution:

    def spiralOrder(self, matrix):
        if not matrix:
            return []

        a = 0  # row-first
        result = []
        b = len(matrix[0]) - 1  # column end
        c = 0  # column start
        d = len(matrix) - 1  # row end
        while a <= d and c <= b:
            i = c
            while i <= b:
                result.append(matrix[a][i])
                i += 1
            a += 1
            i = a
            while i <= d:
                result.append(matrix[i][b])
                i += 1
            b -= 1
            if a <= d:
                i = b
                while i >= c:
                    result.append(matrix[d][i])
                    i -= 1
                d -= 1
            if c <= b:
                i = d
                while i >= a:
                    result.append(matrix[i][c])
                    i -= 1
                c += 1
        return result