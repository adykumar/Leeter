"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""

"""
Solution time complexity:
"""


class Solution(object):

    def createPalindrome(self, n, type):
        """
        """
        if type=="even":
            return n+n[::-1]
        else:
            return n+(n[0:-1])[::-1]
    
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
	l = len(n)
	left= n[0:(l+1)/2]
        opt1=""
        opt2=""
	if l%2==0:
		opt1= self.createPalindrome(left,"even")
                if n>opt1:
                        newleft= str( int(left)+1)
                        if len(newleft)!=len(left):
                                opt2= self.createPalindrome(newleft,"odd")
                        else:
                                opt2= self.createPalindrome(newleft,"even")
	else:
		opt1= self.createPalindrome(left, "odd")

		return opt1
        
        if n==opt2: return opt1
        if n==opt1: return opt2
        if  abs(int(opt2)-int(n)) < abs(int(opt1)-int(n)):
            return opt2
        return opt1

if __name__=="__main__":
	obj= Solution()
	samples= ["123","123678", "123456789", "4110099"]
	for sample in samples:
		print sample, "->", obj.nearestPalindromic(sample)
