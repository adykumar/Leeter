"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

          1
      /   |   \
      3   2   4
    /   \
    5   6


We should return its max depth, which is 3.



Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children # list of nodes

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root==None:
            return 0
        res= 0
        for eachNode in root.children:
            res= max(res, self.maxDepth(eachNode))
        return res+1
