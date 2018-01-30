# Definition for a binary tree node.
"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].

"""

"""
Solution:
Time Complexity - O(n^2)...O(n) is possible
Space complexity- O(?)
"""
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):    
    def splitter(self, array):
        if len(array)<1:
            return None
        Max= -sys.maxsize
        Maxpos= -1
        for i in range(len(array)):
            if Max< array[i]:
                Max= array[i]
                Maxpos= i
        newnode= TreeNode(Max)
        newnode.left=  self.splitter( array[0:Maxpos])
        newnode.right= self.splitter( array[Maxpos+1:len(array)])
        return newnode
        
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.splitter( nums)

def display_tree(treenode):
	if treenode == None:
		print "XX", 
		return
	print treenode.val,
	display_tree(treenode.left)
	display_tree(treenode.right)

if __name__=="__main__":
	obj= Solution()
	treenode= obj.constructMaximumBinaryTree([3,2,1,6,0,5])
	display_tree(treenode)
        
