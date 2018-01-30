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
conversion and palin check O(l)...l is length of n
range of checks - O(10^(l/2))
So overall- O(10^l/2)
"""


class Solution(object):
    def isPalin(self,num):
	"""
	:type num: int
	:rtype: bool 
	"""
        n= str(num)
        l= len(n)
        for i in range(l/2):
            if n[i]!=n[l-1-i]: 
                return False
        return True
    
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        num= int(n)
        i = 1
        while True:
            if self.isPalin(num-i): return str(num-i)
            if self.isPalin(num+i): return str(num+i)
            i=i+1


if __name__=="__main__":
	obj= Solution()
	samples= ["123","123678", "123456789", "4110099"]
	for sample in samples:
		print sample, "->", obj.nearestPalindromic(sample)
