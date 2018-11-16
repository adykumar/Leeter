
"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        prev= triangle[0]
        for row in triangle[1:]:
            temp= row[::]
            temp[0]+= prev[0]
            temp[-1]+= prev[-1]
            for i in range(1, len(row)-1):
                temp[i]+= min(prev[i-1], prev[i])
            prev= temp
        return min(prev)
