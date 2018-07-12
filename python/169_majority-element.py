"""
Given an array of size n, find the majority element. The majority element is the element that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution(object):
    def major(self, nums):
        res= nums[0]
        count=0
        for each in nums:
            if each == res:
                count+=1
            else:
                count-=1
                if count<0:
                    res= each
                    count= 1

        return res

if __name__=="__main__":
    testcases= [ [3,2,3],   [2,2,1,1,1,2,2], [1]  ]
    obj= Solution()
    for test in testcases:
        print test, " -> ", obj.major(test)
