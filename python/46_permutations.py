"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def backtrack(self, nums, start, l, res):
        if start>=l:
            res.append(nums[::])
            return
        for i in range(start, l+1):
            nums[i], nums[start]= nums[start],nums[i]
            self.backtrack(nums, start+1, l, res)
            nums[i], nums[start]= nums[start],nums[i]

    def permutation(self, nums):
        res =[]
        l= len(nums)-1
        self.backtrack(nums, 0, l, res)
        return res

if __name__=="__main__":
    testcases= [ [1,2,3], [1,2,3,4], [1] ]
    obj= Solution()
    for test in testcases:
        print test, " -> ", obj.permutation(test)
