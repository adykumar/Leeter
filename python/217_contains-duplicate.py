"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution(object):

    def findDup_map(self, nums):
        map= {}
        for each in nums:  # Space/Time - O(n)/O(n)
            if each in map:
                return False
            map[each]= 1
        return True

    def findDup_sort(self, nums):
        nums.sort()  # O(n log n)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False

if __name__=="__main__":
    testcases= [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
    obj= Solution()
    for test in testcases:
        print test, "->", obj.findDup_map(test)
