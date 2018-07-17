"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution(object):

    def validAnagram(self, string1, string2):
        return sorted(string1)==sorted(string2) #O(n log n)

    def validAnagram2(self, string1, string2):
        """
        TIP:
        ord('a') is 97
        chr(97) ia 'a'
        """
        string1= string1.lower()
        string2= string2.lower()
        lis= []
        for i in range(26):
            lis.append(0)
        if len(string1)!= len(string2): return False
        for i in range(len(string1)):
            a= ord(string1[i]) - ord('a')
            b= ord(string2[i]) - ord('a')
            lis[a]+=1
            lis[b]-=1
        for each in lis:
            if each!=0: return False
        return True


if __name__=="__main__":
    testcases= [ ["anagram", "nagaram"], ["rat", "car"]  ]
    obj= Solution()
    for test in testcases:
        print test, " -> ", obj.validAnagram(test[0], test[1])
    for test in testcases:
        print test, " -> ", obj.validAnagram2(test[0], test[1])
