
"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""

"""
Time complexity: O(n) for scan, O(n/2) for stack check => O(n)
Space complexity: O(n) worst case
"""


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack= []
        star= []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if stack: 
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif s[i]=='*':
                star.append(i)
        if len(stack)>len(star):
            return False
        if not stack:
            return True
        while stack:
            if stack[-1]>star[-1]:
                return False
            stack.pop()
            star.pop()
        return True
        
        
if __name__== "__main__":
	obj= Solution()
	testcases= ["**((", "(*)", "(())((())()()(*)(*()(())())())()()((()())((()))(*" ]
	for test in testcases:
		print test, "->", obj.checkValidString(test)
