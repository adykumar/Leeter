"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:
Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
"""

class Solution(object):
    def mineNear(self, board, x, y):
        m= 0
        if x>0 and y>0 and board[x-1][y-1]=='M': m+=1
        if y>0 and board[x][y-1]=='M': m+=1
        if x<len(board)-1 and y>0 and board[x+1][y-1]=='M': m+=1

        if x>0 and board[x-1][y]=='M': m+=1
        if x<len(board)-1 and board[x+1][y]=='M': m+=1

        if x>0 and y<len(board[0])-1 and board[x-1][y+1]=='M': m+=1
        if y<len(board[0])-1 and board[x][y+1]=='M': m+=1
        if x<len(board)-1 and y<len(board[0])-1 and board[x+1][y+1]=='M': m+=1
        return m



    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x= click[0]
        y= click[1]
        if board[x][y]=='M':
            board[x][y]= 'X'
        elif board[x][y]=='E':
            stack= [[x,y]]
            while len(stack)>0:
                a, b= stack.pop()
                if board[a][b]!= 'E': continue
                mines= self.mineNear(board, a, b)
                if mines>0: board[a][b]= str(mines)
                else:
                    board[a][b]= 'B'
                    for i in range(-1,2):
                        for j in range(-1, 2):
                            r= a+i; c= b+j
                            if r>=0 and c>=0 and r<len(board) and c<len(board[0]) and board[r][c]== 'E':
                                stack.append([r,c])
        return board

        
