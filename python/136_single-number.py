"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
class Solution(object):
    def findSingle(self, nums):
        """
        params- list(int)
        return- int
        """
        if len(nums)< 3: return
        res= nums[0]
        for i in range(1, len(nums)):
            res^= nums[i]

        return res


if __name__=="__main__":
    testcases= [[2,2,1], [4,1,2,1,2], [4,4,1,2,1,2,-4]]
    obj= Solution()
    for test in testcases:
        print test, " -> ", obj.findSingle(test)
