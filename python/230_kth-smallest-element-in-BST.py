"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
"""
class TreeNode(object):
    def __init__(self, num):
        self.val= num
        self.left= None
        self.right= None

class BST(object):
    def __init__(self, nums):
        if len(nums)<1: return None
        self.head= TreeNode(nums[0])
        self.list2BST(nums)

    def helper(self, node, nums, i, l):
        if (2*i)+1 < l:
            temp1= TreeNode(nums[(2*i)+1])
            node.left= temp1
            self.helper(node.left, nums, (2*i)+1, l)
        if (2*i)+2 < l:
            temp2= TreeNode(nums[(2*i)+2])
            node.right= temp2
            self.helper(node.right, nums, (2*i)+2, l)

    def list2BST(self, nums):
        i=0
        p= self.head
        self.helper(p, nums, 0, len(nums))

class Solution(object):
    def kthSmallest(self, nums, k):
        bst= BST(nums)
        stack= []
        flag= True
        curr= bst.head
        print "--",curr.val, curr.left.val, curr.right.val
        while flag:
            if curr!= None:
                stack.append(curr)
                curr= curr.left
            else:
                if len(stack)>0:
                    curr= stack.pop()
                    k-=1
                    if k==0: return curr.val
                    curr= curr.right
                else:
                    flag= False
        return -99

if __name__=="__main__":
    testcases= [ [ [3,1,4,None,2], 1],  [ [5,3,6,2,4,None,None,1], 2  ] ]
    obj= Solution()
    for test in testcases:
        print test, "->", obj.kthSmallest(test[0], test[1])
