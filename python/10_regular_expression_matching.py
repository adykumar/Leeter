"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true

"""

class Solution(object):
    def isMatch(self, s, p):
    	"""
	:type s: str
	:type p: str
	:rtype: bool
	"""
	return True
	
def main():
	obj= Solution()
	print "ab",".*", obj.isMatch("ab",".*")
	print "aab","c*a*b", obj.isMatch("aab","c*a*b")
if __name__=="__main__":
	main()