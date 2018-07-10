"""
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, text):
        return text[::-1]     """ Time - O(n)  """

if __name__=="__main__":
    obj= Solution()
    testcases= ["Hello", "Brian! werewolf"]
    for test in testcases:
        print test, " -> ", obj.reverseString(test)
