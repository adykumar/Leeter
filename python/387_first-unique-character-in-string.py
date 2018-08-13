"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def uniq(self, s):   # O(2n) time, O(26) space
        lis= []
        for i in range(26):
            lis.append(0)
        for each in s:
            ch= ord(each)-ord('a') # 'a'=0, 'b'=1 and so on
            if lis[ch]==0:
                lis[ch]= 1
                continue
            if lis[ch]==1:
                lis[ch]= -1

        i= 0
        for each in s:
            ch= ord(each)-ord('a')
            if lis[ch]>0:
                return i
            i+=1
        return -1

if __name__=="__main__":
    testcases= ["leetcode", "loveleetcode", "mainmani"]
    obj= Solution()
    for test in testcases:
        print test, "->", obj.uniq(test)
