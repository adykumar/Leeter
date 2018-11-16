"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
"""
LOGIC:
G(n)- # of possible BSTs for given n nodes
F(i,n)- # of possible BSTs for given n nodes where i is root
F(i,n)= G(i-1)*G(n-i) considering the 2 subtrees on both sides
"""

class Solution(object):

    def helper(self, G, n):
        if n in G:
            return G[n]
        res= 0
        for i in range(1, n+1):
            res+= self.helper(G, i-1) * self.helper(G, n-i)
        G[n]= res
        return res

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2: return n
        G= {}
        G[0]=1
        G[1]=1
        G[2]=2
        return self.helper(G, n)
