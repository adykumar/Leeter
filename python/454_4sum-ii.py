"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

class Solution(object):
    def fourSum2(self, A, B, C, D):
        ab= {}
        for a in A:
            for b in B:
                if a+b in ab:
                    ab[a+b]+=1
                else:
                    ab[a+b]=1
        res= 0
        for c in C:
            for d in D:
                if -c-d in ab:
                    res+= ab[-c-d]

        return res

if __name__=="__main__":
    testcases= [ [ [ 1, 2], [-2,-1], [-1, 2], [ 0, 2] ]   ]
    obj= Solution()
    for test in testcases:
        for arrs in test: print arrs,
        print "=> ", obj.fourSum2(test[0], test[1], test[2], test[3])
