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
	:p-type n: str
	:p-type type: str ["even"/"odd"]
	:r-type str
        """
        if type==0:  # even number of digits
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
	
	opt1= self.createPalindrome(left,l%2)
	if n==opt1:
		newleft= str( int(left)+1)
		if len(newleft)!=len(left):
			if l%2==0:
               			opt1= self.createPalindrome(newleft,1)
			else:
				opt1= self.createPalindrome(newleft[0:-1],0)
		else:
			opt1= self.createPalindrome(newleft,l%2)

        if n>opt1:
                newleft= str( int(left)+1)
	else:
		newleft= str( int(left)-1)
	opt2= self.createPalindrome(newleft,l%2) 
        if n==opt2: return opt1
        if n==opt1: return opt2
        if  abs(int(opt2)-int(n)) < abs(int(opt1)-int(n)):
            return opt2
        return opt1

if __name__=="__main__":
	obj= Solution()
	samples= ["9","11","123","123678", "123456789", "4110099","99999"]
	for sample in samples:
		print sample, "--", obj.nearestPalindromic(sample)
