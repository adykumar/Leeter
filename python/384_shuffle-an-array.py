"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
from random import randint
class Solution():
    def __init__(self, nums):
        self.nums= nums

    def reset(self):
        return self.nums

    def shuffle(self):
        nums= self.nums[::]
        if nums==[]: return []
        temp= []
        while len(nums)>0:
            i= randint(0, len(nums)-1)
            temp.append(nums[i])
            del nums[i]
        return temp

if __name__=="__main__":
    testcases= [ [1,2,3], [], [2,4,6,7,8,11] ]
    for test in testcases:
        obj= Solution(test)
        print "\nArray: ", test
        print "Shuffle:", obj.shuffle(), "Reset:", obj.reset(), "Shuffle:", obj.shuffle()
