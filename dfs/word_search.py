"""
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
    """
    


from typing import List


class Solution:
    
    def dfs(self, board, i , j, word, temp = ""):
        m =  len(board)
        n = len(board[0])
        temp+= board[i][j]
        if word == temp:
            return True, temp
        if word[0:len(temp)] == temp:
            for k in [(0,1),(1,0),(0,-1),(-1,0)]:
                i1 = i+ k
                j1 = j+k
                if 0<=i1<m and 0<=j1<n:
                    still_recurse, temp =  self.dfs(board,i1,j1, word, temp)
                
                    
        return False, temp
            
        
    
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m =  len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word):
                    return True
        return False      
                