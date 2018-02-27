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
"""
Complexity Analysis:

The list has to be scanned twice. First for identifying the last occurence of each letter. Second for creating the batches so that same letters are in same groups
Time complexity - O(2n) or O(n)
Space - O(1)
"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
	result= []
	dict= {}
	for i in range(len(S)):
		dict[S[i]]= i   # save last occurence of each letter in dict
	limit= 0
	current= 0
	for i in range(len(S)):
		current= current+ 1
		limit= max(limit, dict[S[i]])   # set limit as last occurence for current ele being handled
		if i>= limit:
			result.append(current)  # if the current iteration reaches the limit, it means that no ele in this group occurs outside
			current= 0
	return result
				

if __name__=="__main__":
	obj= Solution()
	testcases= ["ababcbacadefegdehijhklij", "lolakutty","aaabaaa","abcdef"]
	for test in testcases:
		print test, "->", obj.partitionLabels(test)
