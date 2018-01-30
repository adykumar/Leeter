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
        if len(nums)<=1: return
        l= len(nums)
        left=0
        while nums[left]!=0:
            left=left+1
            if left==l: return
        right=left+1
        while right<l:
            if nums[right]==0:
                right=right+1
            else:
                nums[left]=nums[right]
                left=left+1
                right=right+1
        while left<l:
            nums[left]=0
            left=left+1
        print nums






if __name__=='__main__':
    obj= Solution()
    nums = [0, 1, 0, 3, 12]
    nums=[0,1,0,0,0]
    #nums=[2,4,2,1]
    print nums
    obj.moveZeroes(nums)
    print nums
