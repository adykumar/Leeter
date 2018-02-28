"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

"""
Time complexity- O(n)
Space- O(1)


"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        limit=0
        l= len(nums)
        i=0
        while i<=limit:
            limit= max(limit, i+nums[i])
            #print limit
            if limit>=l-1:
                return True
            i+=1
        return False
        
if __name__=="__main__":
	obj= Solution()
	testcases= [[2,3,1,1,4], [3,2,1,0,4]]
	for test in testcases:
		print test, "->", obj.canJump(test)
