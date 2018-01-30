"""
Implement wildcard pattern matching with support for '?' and '*'.

HARD

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "*") ? true
isMatch("aa", "a*") ? true
isMatch("ab", "?*") ? true
isMatch("aab", "c*a*b") ? false

"""
# works but got to understand fully


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

	st= 0 # points to s-char
	patt= 0 # points to p-char
	match= 0 # keeps track of last s-char match
	star= -1 # stores last * encountered
	
	while st<len(s):
		""" 1- if s-char and p-char match or p-char is ?, proceed to next """ 
		if patt < len(p) and ( s[st] == p[patt] or p[patt] == '?'  ):
			st=st+1
			patt=patt+1
		""" 2- if p-char is *, initiate star and match ; also move to next s-char """
		elif patt < len(p) and p[patt] == '*':
			star= patt
			match= st
			patt=patt+1
		""" 3- star was encountered before: start p-char matching right after * and update and increment match and s-char"""
		elif star > -1:	
			patt= star+1
			match= match +1
			st= match
		""" 4- any other case GTFO """
		else:
			return False
	rem_pat= p[patt:len(p)]
	for each in rem_pat:
		if each != "*":
			return False
	return True			
        
def main():
	obj= Solution()
	print "aaa","aaa","--", obj.isMatch("aaa","aaa")
	print "aa", "*", "--",obj.isMatch("aa", "*")
	print "aa", "?*", "--",obj.isMatch("aa", "?*")
	print "aab", "c*a*b", "--",obj.isMatch("aab", "c*a*b")

if __name__=="__main__":
	main()
