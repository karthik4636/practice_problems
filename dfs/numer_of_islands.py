#https://leetcode.com/problems/number-of-islands/description/?envType=problem-list-v2&envId=depth-first-search


# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


class Solution:


    def dfs(self, grid, i, j):
        grid[i][j] = "0"
        for (i1, j1) in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<=i+i1<len(grid) and 0<=j+j1<len(grid[0]) and grid[i+i1][j+j1]=="1":
                self.dfs(grid, i+i1, j+j1)
                

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        m = len(grid)

        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]== "1":
                    self.dfs(grid, i, j)
                    count+=1
                    
        return count