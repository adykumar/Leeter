"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution(object):

    def worker(self, op, cl, st, res):
        if op>cl: return
        if op<0 or cl<0: return
        if op==0 and cl==0:
            res.append(st)
            return
        self.worker(op-1, cl, st+"(", res)
        self.worker(op, cl-1, st+")", res)

    def genParen(self, n):
        res= []
        self.worker(n, n, "", res)
        return res

if __name__=="__main__":
    testcases= [2, 3, 4]
    obj= Solution()
    for test in testcases:
        print test, " -> ", obj.genParen(test)
