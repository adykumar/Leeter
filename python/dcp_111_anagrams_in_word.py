"""
INCOMPLETE
Given a word W and a string S, find all starting indices in S which are anagrams of W.
For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

"""
Best time : O(n) expected

"""

class Solution(object):

    #def __init__(self):
    def anagramPositions(self, word, str):
        lis= []
        l = len(word)
        for i in range(len(str) - l +1):
            part = str[i:i+l]
            if sorted(part)== sorted(word):
                lis.append(i)
        return lis




if __name__=="__main__":
    test_words = ["ab", "lol"]
    test_strings= ["abxaba", "alololol"]
    for i in range(len(test_words)):
        obj= Solution()
        print obj.anagramPositions(test_words[i], test_strings[i])
