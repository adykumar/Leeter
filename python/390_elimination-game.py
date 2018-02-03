"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""
"""
THIS IS AN INEFFICIENT SOLUTION. THERE IS A BETTER SOLUTION WITH MUCH BETTER SPACE AND TIME COMPLEXITY
HERE: space / time complexity is O(n) which is bad for large numbers. Failed with numbers approaching 1 billion
"""

class Solution(object):
    def elim(self, num, typ):
        if typ==0:
            return num[1::2]
        if typ==1 and len(num)%2==0:
            return num[::2]
        return num[1::2]
        
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        num=[]
        while i<=n:
            num.append(i)
            i=i+1
            
        while len(num)>1:
            num= self.elim(num,0)
            if len(num)==1:
                break
            num= self.elim(num,1)
        return num[0]
        


if __name__=="__main__":
	obj= Solution()
	testcases= [9, 100, 100000, 100000000]
	for test in testcases:
		print test, "->", obj.lastRemaining(test)
