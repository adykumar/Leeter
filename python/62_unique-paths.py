"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""

"""
Core Logic:
This uses a DP solution. To get to any point (i,j) on the map, we can use paths from the top or the left.
So dp[i,j] is sum of dp[i-1, j] and dp[i, j-1]
"""
"""
Normal DP way uses O(mn) time and space
But main logic step uses only the current and previous rows. We can use this to reduce space use.
Space optimized DP uses O(m) space only.

## optimization similar to edit distance question (LC 72)
"""

class Solution(object):
    # NORMAL DP O(mn) space/time
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """ The grid is m x n: n rows, m cols"""
        dp= [ [1 for i in range(m)] for j in range(n)  ]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]= dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]          


class Solution(object):
# OPTIMIZED DP O(m) space, O(mn) time
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """ The grid is m x n: n rows, m cols"""
        prev= [1]*m
        for i in range(1, n):
            new= [1]*m
            for j in range(1,m):
                new[j]= new[j-1]+ prev[j]
            prev= new
        return prev[-1]
