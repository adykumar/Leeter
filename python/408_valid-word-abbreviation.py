"""
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
"""

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if word=="" and abbr=="":
            return True
        i=-1
        num=0
        for each in abbr:
            if each>="0" and each<="9":
                if each=="0" and num=="0": return False
                num= 10*num+int(each)
            else:
                i= i+num+1
                print word[i], each
                if i>len(word)-1 or each!=word[i]: return False
                num=0
        if i+num==len(word)-1: return True
        return False

if __name__=="__main__":
    obj= Solution()
    print obj.validWordAbbreviation("word","w1r1")
    print obj.validWordAbbreviation("word","word")
    print obj.validWordAbbreviation("abbreviation","a10n")
