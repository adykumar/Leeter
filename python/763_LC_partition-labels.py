"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
	result= []
	left
	odict= {} # for last occurence
	for j in range(len(S)):
		odict[each]= j

	for i in range(len(S)):
		if i== odict[S[i]]:
			result.append(current)
			current =1
		else:
			current= odict[S[i]]-i
			i= odict[S[i]]+1
	
if __name__=="__main__":
	obj= Solution()
	testcases= ["ababcbacadefegdehijhklij", "lolakutty","aaabaaa","abcdef"]
	for test in testcases:
		print test, "->", obj.partitionLabels(test)
