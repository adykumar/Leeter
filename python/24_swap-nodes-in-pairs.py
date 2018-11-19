"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Keep back and front pointers.
Use a temp to feel the way ahead and update. Important to break the process if a pair of nodes not detected ahead
O(n) time, O(1) space
"""

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        back= head
        front= head.next
        res= front
        while True:
            temp= front.next
            front.next= back
            if temp==None or temp.next==None:
                back.next= temp
                break
            back.next= temp.next
            back= temp
            front= temp.next
        return res
