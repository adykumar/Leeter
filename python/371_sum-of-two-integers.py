"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Example:
Given a = 1 and b = 2, return 3.
"""

class Solution(object):
    def ninjaSum(self, a, b):
        if a==0: return b
        if b==0: return a
        if a<b:
            a,b = b,a
        if b<0 and abs(b)<abs(a):
            return -self.ninjaSum(-a, -b)
        if a==-b: return 0

        res= 0
        carry= 0
        while b!=0:
            res= a^b
            carry= (a&b)<<1
            a= res
            b= carry
        return res

if __name__=="__main__":
    testcases= [[1,2], [2,0], [1, -1], [1, -23], [12, -1]]
    obj= Solution()
    for test in testcases:
        print test, " -> ", obj.ninjaSum(test[0], test[1])
