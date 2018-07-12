"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

class Solution(object):
    def excelColumn(self, str):
        str= str.upper()
        alpha= "abcdefghijklmnopqrstuvwxyz".upper()
        alpha_list= list(alpha)
        str_list= list(str)
        adic= {} ; i=1
        for each in alpha_list:
            adic[each]= i
            i+=1
        res= 0
        n=0
        for each in reversed(str_list):
            res+= adic[each]* (26**n)
            n+=1
        return res

if __name__=="__main__":
    testcases= ["A", "AB", "ZY"]
    obj= Solution()
    for each in testcases:
        print each, " -> ", obj.excelColumn(each)
