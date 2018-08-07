"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

    4 -> 5 -> 1 -> 9
Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list
             should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list
             should become 4 -> 5 -> 9 after calling your function.
Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""
class Node(object):
    def __init__(self, x):
        self.val= x
        self.next= None


class Solution(object):
    def createLL(self, lis):
        if len(lis)<2: return
        head= Node(lis[0])
        p= head
        for each in lis[1:]:
            temp= Node(each)
            p.next= temp
            p= p.next
        print "LL => ",
        self.printLL(head)
        return head

    def printLL(self, head):
        while head!= None:
            print head.val,
            head= head.next
        print

    def giveNode(self, lis):
        head= self.createLL(lis)
        p= head
        from random import randint
        k= randint(0,len(lis)-2)
        while k:
            p= p.next
            k-=1
        print "Given => ", p.val
        return head, p

    def removeGiven(self, node):
        p= node
        while p.next.next!= None:
            p.val= p.next.val
            p= p.next
        p.val= p.next.val
        p.next= None


if __name__=="__main__":
    obj= Solution()
    testcases= [[4,5,1,9], [4,1,9]]
    for test in testcases:
        head, given= obj.giveNode(test)
        obj.removeGiven(given)
        print "Result: ",
        obj.printLL(head)
        print
