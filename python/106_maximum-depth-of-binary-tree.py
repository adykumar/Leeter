"""

NOT WORKING

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
import Queue as queue

class TreeNode(object):
    def __init__(self,x):
        self.val= x
        self.left= None
        self.right= None

class Solution(object):
    def createTree(self, treelist):
        root= TreeNode(treelist[0])
        q= queue.Queue(maxsize= len(treelist))
        q.put = root
        i = 1
        while i<len(treelist):
            node= q.get()
            print node.val
            if treelist[i] != "null":
                node.left= TreeNode(treelist[i])
                q.put(node.left)
            i+=1
            if treelist[i] != "null":
                node.right= TreeNode(treelist[i])
                q.put(node.right)
            i+=1
        return root

    def maxDepth(self, root):
        if root==None: return 0
        return max( self.maxDepth(root.left)+1, self.maxDepth(root.right)+1 )

if __name__=="__main__":
    testcases= [[3,9,20,"null","null",15,7], [1], [1,"null", 3]]
    obj= Solution()
    for test in testcases:
        root= obj.createTree(test)
        print test, " -> ", obj.maxDepth(root)
