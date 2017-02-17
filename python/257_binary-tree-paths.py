"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
################

class Solution(object):
    def bt(self,root,cumul,lis):
        # receives root
        # cumulative string for walking along nodes
        # at leaf, accumulate into list
        if root==None: return []
        if root.left==None and root.right==None:
            lis.append(cumul+str(root.val))
        else:
            cumul=cumul+ str(root.val)+"->"
            self.bt(root.left,cumul,lis)
            self.bt(root.right,cumul,lis)
        return lis

    def binaryTreePaths(self, root):
        # function receives root
        # passes it to bt(...) for accumulating the list contents
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.bt(root,"",[])

if __name__=='__main__':
    head= TreeNode(1)
    head.left= TreeNode(2)
    head.right= TreeNode(3)
    head.left.right= TreeNode(5)
    obj= Solution()
    print obj.binaryTreePaths(head)
