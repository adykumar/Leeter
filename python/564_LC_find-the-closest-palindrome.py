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
    
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
	l = len(n)
	left= n[0:(l+1)/2]
	if l%2==0:
		opt1= left+ left[::-1]
		return opt1	
	else:
		opt1= left+ (left[0:-1])[::-1]
		return opt1

if __name__=="__main__":
	obj= Solution()
	samples= ["123","123678", "123456789", "4110099"]
	for sample in samples:
		print sample, "->", obj.nearestPalindromic(sample)
