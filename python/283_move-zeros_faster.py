"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros=0
        l= len(nums)
        for each in nums:
            if each==0: zeros=zeros+1
        for i in range(l):
            temp= nums[i]
            nums[i]= nums[l-zeros]
            nums[l-zeros]= temp






if __name__=='__main__':
    obj= Solution()
    nums = [0, 1, 0, 3, 12]
    nums=[0,1,0,0,0]
    nums=[2,4,2,1]
    print nums
    obj.moveZeroes(nums)
    print nums
