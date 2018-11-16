"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        This is an optimized Time-O(mn) and Space- O(n) solution
        """
        m= len(word1)
        n= len(word2)

        prev_row= [i for i in range(n+1)]

        for i in range(1, m+1):
            new_row= [-1] * (n+1)   #O(n) space used
            new_row[0]= i
            for j in range(1, n+1):  # O(m*n) time
                if word1[i-1]==word2[j-1]:
                    new_row[j]= prev_row[j-1]
                else:
                    new_row[j]= 1+ min(prev_row[j-1], new_row[j-1], prev_row[j])
            prev_row= new_row
        return prev_row[-1]
