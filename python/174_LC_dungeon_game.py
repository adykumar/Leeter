"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:
The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""

import sys

class Solution(object):
    
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows= len(dungeon)
        cols= len(dungeon[0])
        dp=[]
        inner=[]
        for i in range(rows):
            for j in range(cols):
                inner.append([0,0])
            dp.append(inner)


        for i in range(rows):
            for j in range(cols):
		if i==0 and j==0:
			dp[0][0]= [dungeon[0][0], dungeon[0][0]]
			continue
                top=  [-sys.maxsize,0]
                left= [-sys.maxsize,0]
                if i-1>=0: 
			top=  dp[i-1][j]
			print "t",
                if j-1>=0: 
			left= dp[i][j-1]
			print "l",
		src= [0,0]
                if top[0]>left[0]:
			src= top
		else:
			src= left
       		dp[i][j][1]= src[0]+dungeon[i][j]
		dp[i][j][0]= min(dp[i][j][1], src[0])
		print i,j,"--",top, left, src, "--",dungeon[i][j],"**",dp[i][j]
	
	for k in range(rows):
            for l in range(cols):
                print dungeon[k][l],
            print ""
	print ""
        for m in range(rows):
            for n in range(cols):
                print dp[m][n],
	    print ""
	return "ZZZ"

if __name__=="__main__":
	testarr= [   [[-2,-3,3],[-5,-10,1],[10,30,-5]],    [[0]] ]
	for each in testarr:
		obj= Solution()
		print each
		print obj.calculateMinimumHP(each) 
		break
