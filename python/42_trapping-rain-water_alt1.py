"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3: return 0 # edge cases
        result=0
        ml=0
        mr=0
        left=0
        right= len(height)-1
        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=ml:
                    ml= height[left]
                else:
                    result= result+ ml-height[left]
                left=left+1
            else:
                if height[right]>=mr:
                    mr= height[right]
                else:
                    result= result+mr- height[right]
                right=right-1
        return result

if __name__=="__main__":
    lis= [0,1,0,2,1,0,1,3,2,1,2,1]
    obj= Solution()
    print obj.trap(lis)
