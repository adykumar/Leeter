"""

Given a binary tree, return the inorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

import Queue as queue

class TreeNode(object):
    def __init__(self,x):
        self.val= x
        self.left= None
        self.right= None

class CreateTree(object):
    def __init__(self, treelist):
        root= TreeNode(treelist[0])
        q= queue.Queue(maxsize= len(treelist))
        q.put(root)
        i = 1
        while True:
            if i>= len(treelist): break
            node= q.get()
            if treelist[i] != None:
                node.left= TreeNode(treelist[i])
                q.put(node.left)
            i+=1
            if i>= len(treelist): break
            if treelist[i] != None:
                node.right= TreeNode(treelist[i])
                q.put(node.right)
            i+=1

        self.root= root

class Solution(object):

    def inorder(self, root):
        stack= []
        res= []
        flag= True
        curr= root
        while flag:
            if curr!= None:
                stack.append(curr)
                curr= curr.left
            else:
                if len(stack)>0:
                    curr= stack.pop()
                    res.append(curr.val)
                    curr= curr.right
                else:
                    flag= False
        return res

if __name__=="__main__":
    obj= Solution()
    testcases= [[1,None,2,3], [6,21,None,None,33], [1,None,2,3, None, 2, 45, None, 5, None, 43,9, 2], [None]]
    for test in testcases:
        tree= CreateTree(test)
        print test, " -> ", obj.inorder( tree.root )
