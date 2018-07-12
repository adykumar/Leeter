"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution(object):
    def pdt(self, nums):
        if len(nums)<2: return []
        res= [ nums[0] ]
        for i in range(1, len(nums)):
            res.append(res[i-1]*nums[i-1])
        right= 1
        for i in range(len(nums)-1, -1, -1):
            res[i]*= right
            right*= nums[i]
        return res

if __name__=="__main__":
        testcases= [[1,2,3,4], [1,4], [1], [], [5,8,7,1,1,4,5]]
        obj = Solution()
        for test in testcases:
            print test, " -> ",obj.pdt(test)
