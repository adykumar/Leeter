"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

"""
Core Logic:
If there is a cycle, detect it by using fast and slow pointers. Where the fast and slow pointers meet is P1, let's say.
Now if there is a travelling pointer starting from head and another one starting from P1, they will eventually meet
at the point where the cycle starts.

There is math behind this logic.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        flag= False
        slow=fast=head
        while True:
            fast= fast.next
            if fast==None:
                flag= True
                break
            fast=fast.next
            slow=slow.next
            if fast==None or slow==None:
                flag= True
                break
            if slow==fast:
                break
        if flag:
            return None
        slow= head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
