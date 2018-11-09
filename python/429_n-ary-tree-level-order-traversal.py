"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

        1
     /  |  \
    3   2   4
  /   \
  5   6


We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children #list of nodes

class Solution(object):
    def helper(self, root, res, level):
        if root==None:
            return
        if len(res)<= level+1 and len(root.children)>0:
            res.append([])
        for eachNode in root.children:
            res[level+1].append(eachNode.val)
            self.helper(eachNode, res, level+1)

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        res= [[root.val]]
        self.helper(root, res, 0)
        return res
