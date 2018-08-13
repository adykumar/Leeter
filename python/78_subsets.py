"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):

    def helper(self, res, temp, nums, start, end):
        res.append(temp[::])
        for i in range(start, end):
            temp.append(nums[i])
            self.helper(res, temp, nums, i+1, end)
            temp.pop()

    def subsets(self, nums):
        res= []
        self.helper(res, [], nums, 0, len(nums) )
        return res

if __name__=="__main__":
    testcases= [[1,2,3], [1,2,3,4], []]
    obj= Solution()
    for test in testcases:
        print "\n",test, " -> ", obj.subsets(test)
