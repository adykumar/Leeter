"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeros(self, nums):
        l= len(nums)
        if l<2: return nums
        ptr= 0
        while ptr<l and nums[ptr]!= 0:
            ptr+=1
        if ptr==l: return nums
        i= ptr+1
        while i<l:
            if nums[i]!=0:
                nums[ptr]= nums[i]
                ptr+=1
            i+=1
        while ptr<l:
            nums[ptr]=0
            ptr+=1
        return nums

if __name__=="__main__":
    testcases= [[0,1,0,3,12], [0], [1,2,3,4], [0,0,0,0,1,0,0,3]]
    obj= Solution()
    for test in testcases:
        print test, " -> ", obj.moveZeros(test)
