"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def helper(self, root, res, lev):
        if root==None or (root.left==None and root.right==None):
            return
        if len(res)<= lev+1:
            res.append([])
        if root.left:
            res[lev+1].append(root.left.val)
            self.helper(root.left, res, lev+1)
        if root.right:
            res[lev+1].append(root.right.val)
            self.helper(root.right, res, lev+1)

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        res= [[root.val]]
        self.helper(root, res, 0)
        return res[::-1]
