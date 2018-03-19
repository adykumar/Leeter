"""
Good morning. Here's your coding interview problem for today.
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

"""
This looks like the fibonacci series: find nth term
Using recursion here with Dynamic Programming to store a cache of solutions

Complexity:
Time- O(n) 
Space- O(n)
"""

class Solution(object):

	cache= {0:0, 1:1, 2:2}

	def ways(self, n):
		if n in self.cache:
			return self.cache[n]
		self.cache[n]= self.ways(n-1) + self.ways(n-2)
		return self.cache[n]
		


if __name__=="__main__":
	obj= Solution()
	for i in range(34):
		print i, obj.ways(i)
	
