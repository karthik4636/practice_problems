# https://leetcode.com/problems/max-area-of-island/description/?envType=problem-list-v2&envId=depth-first-search

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.




class Solution:
    
    def dfs(self, grid, i, j, area=0):
        grid[i][j] = 0
        area += 1
        for (i1, j1) in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<=i+i1<len(grid) and 0<=j+j1<len(grid[0]) and grid[i+i1][j+j1]==1:
                area = self.dfs(grid, i+i1, j+j1, area)
                # dont forget to update area with the return value.
        return area
        
    

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
