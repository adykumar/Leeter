class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if abs(A[i]-i)>1 :
                return False
        return True

if __name__=="__main__":
    obj= Solution()
    lis= [ [1,2,0], [1,4,2,3,0], [3,0,2,1] ]
    for each in lis:
        print each, "->", obj.isIdealPermutation(each)
