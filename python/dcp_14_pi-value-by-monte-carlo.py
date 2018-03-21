"""
Good morning. Here's your coding interview problem for today.
This problem was asked by Google.

The area of a circle is defined as r^2. Estimate  to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
from random import *

class Solution(object):
	def piValue(self, n):
		inside= 0.0
		outside= 0.0
		for i in range(n):
			x= uniform(-1,1)
			y= uniform(-1,1)
			if (x*x)+(y*y)>1:
				outside+=1
			else:
				inside+=1
		print inside, outside
		pi= (4*inside)/(inside+outside)
		return pi
			


if __name__=="__main__":
	obj= Solution()
	print obj.piValue(20000000)
