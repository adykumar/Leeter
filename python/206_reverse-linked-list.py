"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

class Node(object):
    def __init__(self, x):
        self.val= x
        self.next= None


class Solution(object):
    def createLL(self, lis):
        if len(lis)<1:
            return None
        head= Node(lis[0])
        p= head
        for each in lis[1:]:
            temp= Node(each)
            p.next= temp
            p= p.next
        return head

    def printLL(self, head):
        while head!= None:
            print head.val,
            head= head.next
        print

    def reverseLL(self, head):
        if head==None or head.next==None:
            return head
        left= head
        right= head.next
        while right.next!= None:
            temp= right
            right= right.next
            temp.next= left
            left= temp
        right.next= left
        head.next= None
        return right


if __name__=="__main__":
    testcases= [ [1,2,3,4], [1], [], [2,1,34,7]   ]
    obj= Solution()
    for test in testcases:
        print "-----------\n",test
        print "Orig  LL => ",
        orig= obj.createLL(test)
        obj.printLL(orig)
        print "Reversed => ",
        rev= obj.reverseLL(orig)
        obj.printLL(rev)
